/* clusters.c -- exact, exhaustive enumeration (up to symmetry) of distance-2-connected sets K of
 * even-weight vertices of Q_9, with the exact cluster value net(K) = |K| - tau(K), where
 *   A_K    = odd vertices with >= 2 neighbours in K ("witnesses"),
 *   tau(K) = min |Z|, Z subset of A_K, such that Q_9[K u (A_K \ Z)] is a forest.
 * (Odd vertices with <= 1 neighbour in K are leaves and never lie on a cycle, so restricting the
 *  deletions to A_K loses nothing; see claims.md, V2.)
 *
 * Symmetry group: G = { x -> pi(x) xor t : pi a coordinate permutation, t of even weight }.
 * Every g in G is an automorphism of Q_9 preserving weight parity, so tau and net are G-invariant.
 * Canonical key: max over t in K of the max over row orders of the row-major matrix of
 * (K xor t) \ {0} after sorting the 9 columns in decreasing order (branch and bound, exact).
 * Soundness written out in claims.md (R3).
 *
 * Growth: level k+1 = canonical closure of { K0 u {w} : K0 a level-k representative, w a D-neighbour
 * of some vertex of K0, w not in K0 }  (D = distance-2 graph on even words).
 *
 * Usage: clusters kmax [maxtau_extra]
 * Output per size k: #classes, histogram of net(K) (values <= 0 lumped as "<=0"), and every class
 * with net >= 2 (words in decimal, bit i = coordinate i), with |N(K)| (odd neighbourhood) and |A_K|.
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef unsigned __int128 u128;
#define D 9
#define NV 512

static int popc(int x) { return __builtin_popcount(x); }

/* ---------------- canonical form ---------------- */
static int best[16];
static int m_rows;
static int rows[16];


static void dfs(int depth, const int *cols, int used, int greater) {
    if (depth == m_rows) return;
    int w[16], nc[16][D];
    int wmax = -1;
    for (int r = 0; r < m_rows; r++) {
        if (used >> r & 1) { w[r] = -1; continue; }
        int tmp[D];
        /* nc[r][i]: prefix of original column i (rows chosen so far, first row most significant) */
        for (int i = 0; i < D; i++) nc[r][i] = (cols[i] << 1) | ((rows[r] >> i) & 1);
        memcpy(tmp, nc[r], sizeof(tmp));
        for (int a = 1; a < D; a++) {          /* insertion sort, decreasing; copy only used to read off the key row */
            int x = tmp[a], b = a - 1;
            while (b >= 0 && tmp[b] < x) { tmp[b + 1] = tmp[b]; b--; }
            tmp[b + 1] = x;
        }
        int word = 0;
        for (int p = 0; p < D; p++) word |= (tmp[p] & 1) << (D - 1 - p);
        w[r] = word;
        if (word > wmax) wmax = word;
    }
    if (!greater) {
        if (wmax < best[depth]) return;
        if (wmax > best[depth]) greater = 1;
    }
    if (greater) best[depth] = wmax;
    for (int r = 0; r < m_rows; r++) {
        if (w[r] != wmax) continue;
        dfs(depth + 1, nc[r], used | (1 << r), greater);
        greater = 0;
    }
}

/* K: k words (distinct, even). Returns key; writes canonical representative into rep (sorted, rep[0]=0). */
static u128 canon(const int *K, int k, int *rep) {
    m_rows = k - 1;
    int first = 1;
    for (int ti = 0; ti < k; ti++) {
        int t = K[ti], c = 0;
        for (int j = 0; j < k; j++) if (j != ti) rows[c++] = K[j] ^ t;
        int cols[D] = {0};
        if (first) { for (int i = 0; i < 16; i++) best[i] = -1; }
        dfs(0, cols, 0, first);
        first = 0;
    }
    u128 key = 0;
    for (int i = 0; i < m_rows; i++) key = (key << D) | (u128)best[i];
    if (rep) {
        rep[0] = 0;
        for (int i = 0; i < m_rows; i++) rep[i + 1] = best[i];
    }
    return key;
}

/* ---------------- tau ---------------- */
static int inK[NV];
static int wit[NV], nwit;        /* witness list */
static int witidx[NV];
static int deleted[NV];
static int Kw[32], kk;

/* find a cycle among kept witnesses + K; return number of witnesses on it (into cyc), 0 if forest */

static int adjK[NV][D], degK[NV];

static int find_cycle(int *cyc) {
    /* 4-cycles first: pair a,b in K at distance 2, both common neighbours kept */
    for (int i = 0; i < kk; i++) for (int j = i + 1; j < kk; j++) {
        int x = Kw[i] ^ Kw[j];
        if (popc(x) != 2) continue;
        int lo = x & -x, hi = x ^ lo;
        int c1 = Kw[i] ^ lo, c2 = Kw[i] ^ hi;
        if (!deleted[c1] && !deleted[c2]) { cyc[0] = c1; cyc[1] = c2; return 2; }
    }
    /* general: DFS on the bipartite graph K u kept witnesses; in an undirected DFS every non-tree
       edge goes to an ancestor, so the first such edge closes a cycle along the parent pointers. */
    static int vis[NV], parent[NV], depthv[NV];
    for (int i = 0; i < kk; i++) vis[Kw[i]] = 0;
    for (int i = 0; i < nwit; i++) vis[wit[i]] = 0;
    for (int s = 0; s < kk; s++) {
        if (vis[Kw[s]]) continue;
        int stack[NV], it[NV], sp = 0;
        stack[sp] = Kw[s]; it[sp] = 0; sp++; vis[Kw[s]] = 1; parent[Kw[s]] = -1; depthv[Kw[s]] = 0;
        while (sp > 0) {
            int v = stack[sp - 1];
            /* neighbours of v in the kept graph */
            int nbr[D], nn = 0;
            if (inK[v]) { for (int b = 0; b < D; b++) { int u = v ^ (1 << b); if (witidx[u] >= 0 && !deleted[u]) nbr[nn++] = u; } }
            else { for (int b = 0; b < degK[v]; b++) nbr[nn++] = adjK[v][b]; }
            if (it[sp - 1] >= nn) { sp--; continue; }
            int u = nbr[it[sp - 1]++];
            if (u == parent[v]) continue;
            if (vis[u]) {
                /* back edge v-u, u ancestor of v: cycle u .. v */
                int c = 0;
                for (int x = v; ; x = parent[x]) { if (!inK[x]) cyc[c++] = x; if (x == u) break; }
                return c;
            }
            vis[u] = 1; parent[u] = v; depthv[u] = depthv[v] + 1;
            stack[sp] = u; it[sp] = 0; sp++;
        }
    }
    return 0;
}

static long long nodes;
static int Rkept, tmaxw;   /* Rkept = sum over kept witnesses of (t_w - 1); tmaxw = max t_w - 1 */
static int solve(int budget) {
    nodes++;
    /* necessary condition: a forest on K u W' has at most |K| + |W'| - 1 edges, i.e. sum_{W'} (t_w - 1) <= |K| - 1;
       each further deletion lowers the sum by at most tmaxw */
    if (Rkept - (kk - 1) > budget * tmaxw) return 0;
    int cyc[64];
    int c = find_cycle(cyc);
    if (c == 0) return 1;
    if (budget == 0) return 0;
    for (int i = 0; i < c; i++) {
        deleted[cyc[i]] = 1; Rkept -= degK[cyc[i]] - 1;
        int ok = solve(budget - 1);
        deleted[cyc[i]] = 0; Rkept += degK[cyc[i]] - 1;
        if (ok) return 1;
    }
    return 0;
}

/* returns tau if tau <= cap, else cap+1. Also |N(K)| and |A_K|. */
static int tau_of(const int *K, int k, int cap, int *nN, int *nA) {
    int cnt[NV] = {0};
    for (int i = 0; i < k; i++) inK[K[i]] = 1;
    kk = k; memcpy(Kw, K, k * sizeof(int));
    for (int i = 0; i < k; i++) for (int b = 0; b < D; b++) cnt[K[i] ^ (1 << b)]++;
    nwit = 0; int nn = 0;
    for (int v = 0; v < NV; v++) {
        witidx[v] = -1; deleted[v] = 0;
        if (cnt[v] >= 1) nn++;
        if (cnt[v] >= 2) {
            witidx[v] = nwit; wit[nwit++] = v; degK[v] = 0;
            for (int b = 0; b < D; b++) if (inK[v ^ (1 << b)]) adjK[v][degK[v]++] = v ^ (1 << b);
        }
    }
    *nN = nn; *nA = nwit;
    Rkept = 0; tmaxw = 0;
    for (int i = 0; i < nwit; i++) { Rkept += degK[wit[i]] - 1; if (degK[wit[i]] - 1 > tmaxw) tmaxw = degK[wit[i]] - 1; }
    int res = cap + 1;
    for (int b = 0; b <= cap; b++) if (solve(b)) { res = b; break; }
    for (int i = 0; i < k; i++) inK[K[i]] = 0;
    return res;
}

/* ---------------- enumeration ---------------- */
typedef struct { u128 key; } Rec;
/* decode a key (k-1 rows of 9 bits, first row most significant) into the representative set {0} u rows */
static void decode(u128 key, int k, int *w) { w[0] = 0; for (int i = k - 1; i >= 1; i--) { w[i] = (int)(key & 511); key >>= D; } }
static int cmprec(const void *a, const void *b) {
    const Rec *x = a, *y = b;
    return x->key < y->key ? -1 : x->key > y->key ? 1 : 0;
}

int main(int argc, char **argv) {
    int kmax = argc > 1 ? atoi(argv[1]) : 6;
    int dnb[NV][36], nd = 0;
    (void)nd;
    for (int v = 0; v < NV; v++) { int c = 0; for (int i = 0; i < D; i++) for (int j = i + 1; j < D; j++) dnb[v][c++] = v ^ (1 << i) ^ (1 << j); }
    /* level 1: {0} */
    Rec *lev = malloc(sizeof(Rec)); lev[0].key = 0; long long nlev = 1;
    for (int k = 1; k <= kmax; k++) {
        /* evaluate level k */
        long long hist[40] = {0}; long long hneg = 0; int bestnet = -100;
        for (long long i = 0; i < nlev; i++) {
            int nN, nA, W[16]; decode(lev[i].key, k, W);
            int t = tau_of(W, k, k - 1, &nN, &nA);
            int net = k - t;               /* if t == k (cap exceeded) then net <= 0 */
            if (t > k - 1) { hneg++; continue; }
            hist[net]++;
            if (net > bestnet) bestnet = net;
            if (net >= 2) {
                printf("  NET%d k=%d |N(K)|=%d |A_K|=%d tau=%d K=", net, k, nN, nA, t);
                for (int j = 0; j < k; j++) printf("%d%s", W[j], j + 1 < k ? "," : "\n");
            }
        }
        printf("size %d: %lld classes; net histogram:", k, nlev);
        for (int v = 1; v < 40; v++) if (hist[v]) printf(" net=%d:%lld", v, hist[v]);
        if (hneg) printf(" net<=0:%lld", hneg);
        printf("; best net %d; tau-search nodes so far %lld\n", bestnet, nodes);
        fflush(stdout);
        if (k == kmax) break;
        /* grow */
        long long cap = nlev * (long long)k * 36, n2 = 0;
        Rec *nx = malloc(sizeof(Rec) * cap);
        if (!nx) { fprintf(stderr, "oom\n"); return 1; }
        int in[NV];
        memset(in, 0, sizeof(in));
        for (long long i = 0; i < nlev; i++) {
            int W[16]; decode(lev[i].key, k, W);
            for (int j = 0; j < k; j++) in[W[j]] = 1;
            for (int j = 0; j < k; j++) for (int a = 0; a < 36; a++) {
                int w = dnb[W[j]][a];
                if (in[w]) continue;
                int K2[16]; memcpy(K2, W, k * sizeof(int)); K2[k] = w;
                nx[n2].key = canon(K2, k + 1, NULL);
                n2++;
            }
            for (int j = 0; j < k; j++) in[W[j]] = 0;
        }
        qsort(nx, n2, sizeof(Rec), cmprec);
        long long u = 0;
        for (long long i = 0; i < n2; i++) if (u == 0 || nx[i].key != nx[u - 1].key) nx[u++] = nx[i];
        free(lev); lev = nx; nlev = u;
        fprintf(stderr, "grown to size %d: %lld candidates, %lld classes\n", k + 1, n2, nlev);
    }
    return 0;
}
