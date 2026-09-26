/* Referee's independent exact branch-and-bound for F_d = max induced forest of Q_d (d <= 6).
   Vertices processed in order 0..n-1; each is excluded or included. Including v: its already-
   decided neighbours are v^(1<<j) with bit j set in v (they are < v). Union-find (no path
   compression, union by size, with undo stack) detects a cycle: two included lower neighbours
   in the same component, i.e. including v closes a cycle -> branch rejected.
   Prune: included + (n - i) <= best  (cannot beat current best). Exact integers only.
   Output: F_d and a witness. Soundness: every subset of V(Q_d) is either explored or lies in a
   pruned branch that is either cyclic (all supersets cyclic) or cannot exceed best. */
#include <stdio.h>
#include <stdlib.h>
static int d, n, best = 0;
static int par[64], sz[64];
static int inT[64], bestT[64];
static long long nodes = 0;
static int find(int x) { while (par[x] != x) x = par[x]; return x; }
static void rec(int i, int cnt) {
    nodes++;
    if (cnt + (n - i) <= best) return;
    if (i == n) { best = cnt; for (int k = 0; k < n; k++) bestT[k] = inT[k]; return; }
    /* include i */
    int roots[8], nr = 0, ok = 1;
    for (int j = 0; j < d && ok; j++) if (i >> j & 1) {
        int w = i ^ (1 << j);
        if (!inT[w]) continue;
        int r = find(w);
        for (int k = 0; k < nr; k++) if (roots[k] == r) { ok = 0; break; }
        roots[nr++] = r;
    }
    if (ok) {
        /* union i with all roots; record changes for undo */
        int ch[8], nch = 0; int ri = i; par[i] = i; sz[i] = 1;
        for (int k = 0; k < nr; k++) {
            int a = find(ri), b = roots[k];
            if (sz[a] < sz[b]) { int t = a; a = b; b = t; }
            par[b] = a; sz[a] += sz[b]; ch[nch++] = b; ri = a;
        }
        inT[i] = 1;
        rec(i + 1, cnt + 1);
        inT[i] = 0;
        for (int k = nch - 1; k >= 0; k--) { int b = ch[k]; int a = par[b]; sz[a] -= sz[b]; par[b] = b; }
    }
    /* exclude i */
    rec(i + 1, cnt);
}
int main(int argc, char **argv) {
    d = atoi(argv[1]); n = 1 << d;
    best = argc > 2 ? atoi(argv[2]) : 0; /* optional: start with best = given lower value */
    for (int k = 0; k < n; k++) { par[k] = k; sz[k] = 1; inT[k] = 0; bestT[k] = 0; }
    int start = best;
    rec(0, 0);
    if (best == start && argc > 2) printf("d=%d: no induced forest with more than %d vertices (nodes=%lld)\n", d, start, nodes);
    else {
        printf("d=%d: F_d = %d, nodes=%lld, witness:", d, best, nodes);
        for (int k = 0; k < n; k++) if (bestT[k]) printf(" %d", k);
        printf("\n");
    }
    return 0;
}
