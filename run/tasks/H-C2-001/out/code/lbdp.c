/* lbdp.c -- exact layered DP deciding whether some labelling of Q_D has excess X <= LIMIT,
 * where X = T - E  (T = number of uphill paths, E = D*2^(D-1) edges).
 *
 * Identity used (proof in ../claims.md / proof.md):
 *   T = sum_v N(v),  N(v) = [v valley] + sum_{w ~ v, f(w) < f(v)} N(w),
 *   X = T - E = sum_v cost(v),  cost(v) = [v valley] + (N(v) - 1) * up(v),
 *   up(v) = number of neighbours with larger label.
 * Placing vertices in increasing label order, cost(v) is fully determined at the moment v is
 * placed: up(v) = number of unplaced neighbours, N(v) from its (already placed) lower nbrs.
 *
 * State after placing a set S: for each vertex a code in 0..15:
 *   0  = unplaced;  15 = placed, all neighbours placed ("interior", its N never used again);
 *   1..14 = placed with >= 1 unplaced neighbour, value = N(v).
 * (If such a v had N(v) - 1 > LIMIT its own cost would exceed LIMIT, so N(v) <= LIMIT+1 <= 14.)
 * Future costs depend only on this state, so keeping the minimum cost per state is exact.
 *
 * Pruning (admissible): prune if cost_so_far + h(state) > LIMIT, where
 *   h = CB * (size of a greedy matching in the graph induced on F),
 *   F = unplaced vertices whose placed neighbours have N-sum >= 2 (N(w) >= 2 is forced),
 *   CB = min_{r=1..D-1} (max(2, D-r) - 1) * r  (min cost of a non-valley vertex with N >= 2, up >= 1).
 * Optional symmetry: SYM=1 merges states in the same orbit under Aut(Q_D) (coordinate
 * permutations composed with translations), via a canonical orbit representative (see canon()).  SYM=0: only vertex 0 is forced to get label 1.
 *
 * Usage: ./lbdp D LIMIT SYM [HEUR]   (HEUR=0 disables the matching bound h, default 1); prints per-layer state counts and the minimal complete X (if <= LIMIT).
 */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>

static int D, n, LIMIT, SYM, CB, HEUR = 1;
typedef struct { uint64_t a, b; } key_t2;           /* 32 nibbles (D <= 5) */

static inline int getc4(const key_t2 *k, int v) { return v < 16 ? (int)((k->a >> (4 * v)) & 15) : (int)((k->b >> (4 * (v - 16))) & 15); }
static inline void setc4(key_t2 *k, int v, int c) {
    if (v < 16) { k->a &= ~(15ULL << (4 * v)); k->a |= (uint64_t)c << (4 * v); }
    else { k->b &= ~(15ULL << (4 * (v - 16))); k->b |= (uint64_t)c << (4 * (v - 16)); }
}

/* ---- hash table: key -> min cost ---- */
typedef struct { key_t2 k; int8_t c; uint8_t used; } ent;
typedef struct { ent *t; size_t cap, cnt; } table;
static void tinit(table *T, size_t cap) { T->cap = cap; T->cnt = 0; T->t = calloc(cap, sizeof(ent)); if (!T->t) { fprintf(stderr, "oom\n"); exit(2); } }
static inline uint64_t hsh(key_t2 k) { uint64_t h = k.a * 0x9E3779B97F4A7C15ULL ^ (k.b + 0x632BE59BD9B4E019ULL) * 0xC2B2AE3D27D4EB4FULL; return h ^ (h >> 29); }
static void tput(table *T, key_t2 k, int c);
static void tgrow(table *T) {
    table N2; tinit(&N2, T->cap * 2);
    for (size_t i = 0; i < T->cap; i++) if (T->t[i].used) tput(&N2, T->t[i].k, T->t[i].c);
    free(T->t); *T = N2;
}
static void tput(table *T, key_t2 k, int c) {
    if (T->cnt * 2 > T->cap) tgrow(T);
    size_t i = hsh(k) & (T->cap - 1);
    while (T->t[i].used) {
        if (T->t[i].k.a == k.a && T->t[i].k.b == k.b) { if (c < T->t[i].c) T->t[i].c = c; return; }
        i = (i + 1) & (T->cap - 1);
    }
    T->t[i].used = 1; T->t[i].k = k; T->t[i].c = c; T->cnt++;
}

/* ---- automorphisms ---- */
static int naut; static uint8_t (*aut)[32];          /* aut[g][v] = image of v */
static void gen_aut(void) {
    int perm[5]; for (int i = 0; i < D; i++) perm[i] = i;
    int nf = 1; for (int i = 2; i <= D; i++) nf *= i;
    aut = malloc(sizeof(*aut) * nf * n); naut = 0;
    /* enumerate permutations by Heap-free simple method: all D-tuples that are perms */
    int idx[5];
    int total = 1; for (int i = 0; i < D; i++) total *= D;
    for (int t = 0; t < total; t++) {
        int x = t, ok = 1, seen = 0;
        for (int i = 0; i < D; i++) { idx[i] = x % D; x /= D; if (seen >> idx[i] & 1) ok = 0; seen |= 1 << idx[i]; }
        if (!ok) continue;
        for (int a = 0; a < n; a++) {
            for (int v = 0; v < n; v++) {
                int w = 0; for (int i = 0; i < D; i++) if (v >> i & 1) w |= 1 << idx[i];
                aut[naut][v] = (uint8_t)(w ^ a);
            }
            naut++;
        }
    }
    (void)perm;
}
/* canonical form of a state = the lexicographically smallest pair (placed-mask image, code vector)
 * over all automorphisms g, where for g the image state is img[g(v)] = code[v], its placed mask is
 * the 32-bit set {g(v) : code[v] != 0} compared as an unsigned integer, and code vectors are compared
 * position by position 0..n-1.  This is a minimum of a total order over the whole orbit, hence the
 * same for every state of an orbit (a valid orbit representative).  The mask image is computed as
 * coordinate permutation (per-byte tables) followed by translations enumerated in Gray-code order
 * (each step XORs indices by one unit vector = one bit-block swap of the mask). */
static int nperm; static uint32_t (*ptab)[4][256];      /* ptab[p][byte][x]: coordinate-permutation image of mask bits */
static const uint32_t XM[5] = {0x55555555u, 0x33333333u, 0x0F0F0F0Fu, 0x00FF00FFu, 0x0000FFFFu};
static inline uint32_t xswap(uint32_t m, int j) { int s = 1 << j; return ((m >> s) & XM[j]) | ((m & XM[j]) << s); }
static void gen_mtab(void) {
    nperm = naut / n;                         /* aut index g = p*n + a, aut[g][v] = pi_p(v) XOR a */
    ptab = malloc(sizeof(*ptab) * nperm);
    for (int p = 0; p < nperm; p++) for (int byte = 0; byte < 4; byte++) for (int x = 0; x < 256; x++) {
        uint32_t m = 0;
        for (int bb = 0; bb < 8; bb++) if (x >> bb & 1) { int v = byte * 8 + bb; if (v < n) m |= 1u << aut[p * n][v]; }
        ptab[p][byte][x] = m;
    }
}
static key_t2 canon(key_t2 k) {
    if (!SYM) return k;
    int code[32]; uint32_t mask = 0;
    for (int v = 0; v < n; v++) { code[v] = getc4(&k, v); if (code[v]) mask |= 1u << v; }
    uint32_t mmin = 0xFFFFFFFFu;
    static int *gl = 0; if (!gl) gl = malloc(sizeof(int) * naut);
    int ng = 0;
    for (int p = 0; p < nperm; p++) {
        uint32_t m = ptab[p][0][mask & 255] | ptab[p][1][(mask >> 8) & 255] | ptab[p][2][(mask >> 16) & 255] | ptab[p][3][mask >> 24];
        for (int k = 0; k < n; k++) {          /* Gray code over translations a_k = k ^ (k >> 1) */
            if (k) m = xswap(m, __builtin_ctz(k));
            if (m < mmin) { mmin = m; ng = 0; }
            if (m == mmin) gl[ng++] = p * n + (k ^ (k >> 1));
        }
    }
    int best[32]; int have = 0;
    for (int t = 0; t < ng; t++) {
        int g = gl[t]; int img[32];
        for (int v = 0; v < n; v++) img[aut[g][v]] = code[v];
        if (!have) { memcpy(best, img, sizeof(int) * n); have = 1; continue; }
        for (int v = 0; v < n; v++) { if (img[v] != best[v]) { if (img[v] < best[v]) memcpy(best, img, sizeof(int) * n); break; } }
    }
    key_t2 r = {0, 0}; for (int v = 0; v < n; v++) setc4(&r, v, best[v]);
    return r;
}

static int heur(const int *code) {
    int inF[32] = {0};
    for (int w = 0; w < n; w++) if (code[w] == 0) {
        int s = 0;
        for (int j = 0; j < D; j++) { int u = w ^ (1 << j); int c = code[u]; if (c) s += (c == 15 ? 0 : c); }
        /* a placed nbr of an unplaced vertex is never interior, so c != 15 here */
        if (s >= 2) inF[w] = 1;
    }
    int matched[32] = {0}, m = 0;
    for (int w = 0; w < n; w++) if (inF[w] && !matched[w])
        for (int j = 0; j < D; j++) { int u = w ^ (1 << j); if (inF[u] && !matched[u]) { matched[u] = matched[w] = 1; m++; break; } }
    return CB * m;
}

int main(int argc, char **argv) {
    if (argc < 4) { fprintf(stderr, "usage: lbdp D LIMIT SYM\n"); return 1; }
    D = atoi(argv[1]); LIMIT = atoi(argv[2]); SYM = atoi(argv[3]); n = 1 << D;
    if (argc > 4) HEUR = atoi(argv[4]);
    if (D < 2 || D > 5 || LIMIT > 13) { fprintf(stderr, "need 2<=D<=5, LIMIT<=13\n"); return 1; }
    CB = 1 << 30;
    for (int r = 1; r <= D - 1; r++) { int l = D - r; int c = ((l > 2 ? l : 2) - 1) * r; if (c < CB) CB = c; }
    printf("D=%d n=%d LIMIT=%d SYM=%d HEUR=%d CB=%d\n", D, n, LIMIT, SYM, HEUR, CB);
    if (SYM) { gen_aut(); gen_mtab(); printf("automorphisms: %d\n", naut); }
    table cur, nxt; tinit(&cur, 1 << 10);
    /* layer 1: vertex 0 gets label 1 (vertex-transitivity via translations); it is a valley, cost 1 */
    key_t2 k0 = {0, 0}; setc4(&k0, 0, 1); tput(&cur, canon(k0), 1);
    unsigned long long total_states = 1;
    printf("layer 1: %zu states\n", cur.cnt);
    for (int layer = 1; layer < n; layer++) {
        tinit(&nxt, 1 << 10);
        for (size_t i = 0; i < cur.cap; i++) if (cur.t[i].used) {
            key_t2 k = cur.t[i].k; int c0 = cur.t[i].c;
            int code[32]; for (int v = 0; v < n; v++) code[v] = getc4(&k, v);
            for (int w = 0; w < n; w++) if (code[w] == 0) {
                int s = 0, lower = 0, upc = 0;
                for (int j = 0; j < D; j++) { int u = w ^ (1 << j); if (code[u]) { lower++; s += code[u]; } else upc++; }
                int valley = (lower == 0);
                int Nw = valley ? 1 : s;
                int cost = valley + (Nw - 1) * upc;
                int c1 = c0 + cost;
                if (c1 > LIMIT) continue;
                int nc[32]; memcpy(nc, code, sizeof(int) * n);
                nc[w] = (upc == 0) ? 15 : Nw;
                for (int j = 0; j < D; j++) {
                    int u = w ^ (1 << j);
                    if (nc[u] && nc[u] != 15) {
                        int allp = 1; for (int jj = 0; jj < D; jj++) if (!nc[u ^ (1 << jj)]) { allp = 0; break; }
                        if (allp) nc[u] = 15;
                    }
                }
                if (HEUR && c1 + heur(nc) > LIMIT) continue;
                key_t2 nk = {0, 0}; for (int v = 0; v < n; v++) setc4(&nk, v, nc[v]);
                tput(&nxt, canon(nk), c1);
            }
        }
        free(cur.t); cur = nxt; total_states += cur.cnt;
        printf("layer %d: %zu states\n", layer + 1, cur.cnt); fflush(stdout);
        if (cur.cnt == 0) { printf("RESULT: no labelling of Q_%d has X <= %d (T <= %d); states visited %llu\n", D, LIMIT, LIMIT + D * (n / 2), total_states); return 0; }
    }
    int mn = 99; for (size_t i = 0; i < cur.cap; i++) if (cur.t[i].used && cur.t[i].c < mn) mn = cur.t[i].c;
    printf("RESULT: minimal X = %d, i.e. U(Q_%d) = %d  (since %d <= LIMIT); states visited %llu\n", mn, D, mn + D * (n / 2), mn, total_states);
    return 0;
}
