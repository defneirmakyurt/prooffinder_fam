/* maxcode.c -- exact maximum size of a set C of even-weight vertices of Q_9 such that
 *   (i) every two words of C are at Hamming distance >= 4, and
 *  (ii) every word of C is at distance >= 4 from every word of a given set K (the "cluster").
 * (ii) says the words of C lie in other clusters than K; (i) says they are pairwise in different clusters.
 * Exact branch and bound for maximum clique (greedy colouring bound, Tomita-style), bitsets over <= 256 vertices.
 * Usage: maxcode k1,k2,...   (decimal words of K; bit i = coordinate i). Empty K: maxcode -
 * Prints: region size, maximum |C|, one optimal C, and the number of search nodes.
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>

#define W 4
typedef struct { uint64_t b[W]; } bs;
static int n; static int verts[256]; static bs adj[256];
static int best = 0, cur[256], bestset[256]; static long long nodes = 0;

static int popc(int x) { return __builtin_popcount(x); }
static int bscount(const bs *s) { int c = 0; for (int i = 0; i < W; i++) c += __builtin_popcountll(s->b[i]); return c; }

static void expand(bs P, int depth) {
    nodes++;
    /* greedy colouring of P: order[] with colour bounds */
    int order[256], col[256], m = 0;
    bs U = P; int c = 0;
    while (bscount(&U) > 0) {
        c++;
        bs Q = U;
        while (bscount(&Q) > 0) {
            int v = -1;
            for (int i = 0; i < W; i++) if (Q.b[i]) { v = i * 64 + __builtin_ctzll(Q.b[i]); break; }
            Q.b[v >> 6] &= ~(1ULL << (v & 63)); U.b[v >> 6] &= ~(1ULL << (v & 63));
            for (int i = 0; i < W; i++) Q.b[i] &= ~adj[v].b[i];
            order[m] = v; col[m] = c; m++;
        }
    }
    for (int i = m - 1; i >= 0; i--) {
        if (depth + col[i] <= best) return;
        int v = order[i];
        cur[depth] = v;
        bs NP; for (int j = 0; j < W; j++) NP.b[j] = P.b[j] & adj[v].b[j];
        if (bscount(&NP) == 0) {
            if (depth + 1 > best) { best = depth + 1; memcpy(bestset, cur, sizeof(int) * best); }
        } else expand(NP, depth + 1);
        P.b[v >> 6] &= ~(1ULL << (v & 63));
    }
}

int main(int argc, char **argv) {
    int K[512], k = 0;
    if (argc > 1 && strcmp(argv[1], "-") != 0) {
        char *s = strdup(argv[1]), *tok = strtok(s, ",");
        while (tok) { K[k++] = atoi(tok); tok = strtok(NULL, ","); }
    }
    n = 0;
    for (int v = 0; v < 512; v++) {
        if (popc(v) & 1) continue;
        int ok = 1;
        for (int j = 0; j < k; j++) if (popc(v ^ K[j]) < 4) { ok = 0; break; }
        if (ok) verts[n++] = v;
    }
    for (int i = 0; i < n; i++) { memset(&adj[i], 0, sizeof(bs));
        for (int j = 0; j < n; j++) if (j != i && popc(verts[i] ^ verts[j]) >= 4) adj[i].b[j >> 6] |= 1ULL << (j & 63); }
    bs P; memset(&P, 0, sizeof(P)); for (int i = 0; i < n; i++) P.b[i >> 6] |= 1ULL << (i & 63);
    expand(P, 0);
    printf("|K|=%d region=%d max|C|=%d nodes=%lld C=", k, n, best, nodes);
    for (int i = 0; i < best; i++) printf("%d%s", verts[bestset[i]], i + 1 < best ? "," : "\n");
    /* self-check of the optimum found */
    for (int i = 0; i < best; i++) for (int j = i + 1; j < best; j++) if (popc(verts[bestset[i]] ^ verts[bestset[j]]) < 4) { printf("SELF-CHECK FAILED\n"); return 1; }
    return 0;
}
