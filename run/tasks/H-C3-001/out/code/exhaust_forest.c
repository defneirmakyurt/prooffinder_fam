/*
 * exhaust_forest.c -- EXHAUSTIVE count of the sets P of vertices of Q_d with
 *     |P| = p,  P independent,  Q_d - P a forest (acyclic induced subgraph).
 * Used with d = 5, p = 13 (rung R9): a count of 0 rules out 194 uphill paths on Q_6
 * (reduction in out/lower_bound.md).  Sanity: d = 3, p = 3 and d = 4, p = 6 and
 * d = 5, p = 14 must give positive counts (labellings built from such sets were found).
 *
 * Method: backtracking over the vertices 0..2^d-1 in increasing integer order; each
 * vertex is put in P or in A = complement.  A branch is cut only when it cannot be
 * completed:
 *   (i)   v put in P while an earlier neighbour is in P  (P would not be independent;
 *         adding more vertices never removes that edge);
 *   (ii)  v put in A while two of its earlier A-neighbours lie in the same component of
 *         the forest induced on the earlier A-vertices (this closes a cycle; the cycle
 *         stays inside Q_d[A] for every completion, because A only grows);
 *   (iii) |P| would exceed p, or |P| + (#undecided vertices) < p.
 * Every leaf reached has |P| = p, P independent, Q_d[A] a forest, and is counted.
 * Components are kept in a union-find with union by size and an undo stack (no path
 * compression), so backtracking restores it exactly.  Integer arithmetic only.
 *
 * Build: gcc -O2 -o exhaust_forest exhaust_forest.c
 * Run:   ./exhaust_forest d p
 * Output: "d=.. p=.. solutions=S nodes=K"
 */
#include <stdio.h>
#include <stdlib.h>

static int d, n, p;
static int side[1 << 10];          /* -1 undecided, 0 in A, 1 in P */
static int par[1 << 10], sz[1 << 10];
static int stk[1 << 12], top;      /* undo stack: root that got attached */
static long long sols, nodes;

static int findr(int x) { while (par[x] != x) x = par[x]; return x; }
static void unite(int a, int b) {  /* a, b roots, distinct */
    if (sz[a] < sz[b]) { int t = a; a = b; b = t; }
    par[b] = a; sz[a] += sz[b]; stk[top++] = b;
}
static void undo_to(int t) {
    while (top > t) { int b = stk[--top]; int a = par[b]; sz[a] -= sz[b]; par[b] = b; }
}

static void rec(int v, int np) {
    nodes++;
    if (np > p || np + (n - v) < p) return;                 /* (iii) */
    if (v == n) { sols++; return; }
    /* option P */
    int ok = 1;
    for (int j = 0; j < d; j++) { int w = v ^ (1 << j); if (w < v && side[w] == 1) { ok = 0; break; } }
    if (ok && np < p) { side[v] = 1; rec(v + 1, np + 1); side[v] = -1; }   /* (i) */
    /* option A */
    int t = top, roots[16], nr = 0, cyc = 0;
    for (int j = 0; j < d && !cyc; j++) {
        int w = v ^ (1 << j);
        if (w < v && side[w] == 0) {
            int r = findr(w);
            for (int k = 0; k < nr; k++) if (roots[k] == r) { cyc = 1; break; }
            roots[nr++] = r;
        }
    }
    if (!cyc) {                                                              /* (ii) */
        for (int k = 0; k < nr; k++) { int a = findr(v), b = findr(roots[k]); if (a != b) unite(a, b); }
        side[v] = 0; rec(v + 1, np); side[v] = -1;
        undo_to(t);
    }
}

int main(int argc, char **argv) {
    if (argc < 3) { fprintf(stderr, "usage: d p\n"); return 2; }
    d = atoi(argv[1]); p = atoi(argv[2]); n = 1 << d;
    for (int i = 0; i < n; i++) { side[i] = -1; par[i] = i; sz[i] = 1; }
    rec(0, 0);
    printf("d=%d p=%d solutions=%lld nodes=%lld\n", d, p, sols, nodes);
    return 0;
}
