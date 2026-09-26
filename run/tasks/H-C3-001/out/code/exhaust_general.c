/*
 * exhaust_general.c -- EXHAUSTIVE search behind the lower bound U(Q_6) >= 204
 * (reduction and proof in out/lower_bound.md).
 *
 * For a set S of vertices of Q_d ("special" vertices, removed), count the sets P of
 * vertices of Q_d - S such that
 *     P independent,  A = V - S - P induces a forest in Q_d,  c(A) <= cmax,
 *     plo <= |P| <= phi,
 * where c(A) = number of connected components of Q_d[A].
 * mode 0: S empty.  mode 1: every S = {s}, s over all 2^d vertices.
 * mode 2: every S = {s1, s2}, s1 < s2, over all pairs of vertices.
 * No symmetry reduction is used: every S of the given size is searched.
 *
 * Backtracking over vertices 0..2^d-1 in increasing order, each vertex not in S goes to
 * P or to A.  A branch is cut only when no completion can be counted:
 *   (i)   v put in P with an earlier neighbour in P (edge inside P stays forever);
 *   (ii)  v put in A while two of its earlier A-neighbours are in the same component of
 *         the (forest) induced on earlier A-vertices: a cycle is closed, and it stays in
 *         Q_d[A] for every completion because A only grows;
 *   (iii) |P| > phi, or |P| + (#undecided vertices not in S) < plo.
 * At a leaf, c(A) is known exactly (components counter: +1 per A-vertex, -1 per union)
 * and the leaf is counted iff c(A) <= cmax.
 *
 * Build: gcc -O2 -o exhaust_general exhaust_general.c
 * Run:   ./exhaust_general d mode cmax plo phi
 * Output: one line per S with a solution (if any), then a summary line
 *         "d=.. mode=.. cmax=.. plo=.. phi=.. sets_S=.. solutions=.. nodes=.."
 */
#include <stdio.h>
#include <stdlib.h>

static int d, n, plo, phi, cmax;
static int side[1 << 10];          /* -1 undecided, 0 in A, 1 in P, 2 in S */
static int par[1 << 10], sz[1 << 10];
static int stk[1 << 12], top;
static long long sols, nodes;
static int rem_after[(1 << 10) + 1];   /* # non-S vertices with index >= v */

static int findr(int x) { while (par[x] != x) x = par[x]; return x; }
static void unite(int a, int b) {
    if (sz[a] < sz[b]) { int t = a; a = b; b = t; }
    par[b] = a; sz[a] += sz[b]; stk[top++] = b;
}
static void undo_to(int t) {
    while (top > t) { int b = stk[--top]; int a = par[b]; sz[a] -= sz[b]; par[b] = b; }
}

static void rec(int v, int np, int comps) {
    nodes++;
    if (np > phi || np + rem_after[v] < plo) return;           /* (iii) */
    if (v == n) { if (comps <= cmax) sols++; return; }
    if (side[v] == 2) { rec(v + 1, np, comps); return; }
    int ok = 1;
    for (int j = 0; j < d; j++) { int w = v ^ (1 << j); if (w < v && side[w] == 1) { ok = 0; break; } }
    if (ok) { side[v] = 1; rec(v + 1, np + 1, comps); side[v] = -1; }   /* (i) */
    int t = top, roots[16], nr = 0, cyc = 0;
    for (int j = 0; j < d && !cyc; j++) {
        int w = v ^ (1 << j);
        if (w < v && side[w] == 0) {
            int r = findr(w);
            for (int k = 0; k < nr; k++) if (roots[k] == r) { cyc = 1; break; }
            roots[nr++] = r;
        }
    }
    if (!cyc) {                                                          /* (ii) */
        int c = comps + 1;
        for (int k = 0; k < nr; k++) { int a = findr(v), b = findr(roots[k]); if (a != b) { unite(a, b); c--; } }
        side[v] = 0; rec(v + 1, np, c); side[v] = -1;
        undo_to(t);
    }
}

static long long run_S(void) {
    for (int i = 0; i < n; i++) { if (side[i] != 2) side[i] = -1; par[i] = i; sz[i] = 1; }
    top = 0;
    rem_after[n] = 0;
    for (int v = n - 1; v >= 0; v--) rem_after[v] = rem_after[v + 1] + (side[v] != 2);
    long long before = sols;
    rec(0, 0, 0);
    return sols - before;
}

int main(int argc, char **argv) {
    if (argc < 6) { fprintf(stderr, "usage: d mode cmax plo phi\n"); return 2; }
    d = atoi(argv[1]); int mode = atoi(argv[2]); cmax = atoi(argv[3]);
    plo = atoi(argv[4]); phi = atoi(argv[5]); n = 1 << d;
    long long nS = 0;
    for (int i = 0; i < n; i++) side[i] = -1;
    if (mode == 0) { nS = 1; run_S(); }
    else if (mode == 1) {
        for (int s = 0; s < n; s++) {
            for (int i = 0; i < n; i++) side[i] = -1;
            side[s] = 2; nS++;
            long long k = run_S(); if (k) printf("S={%d} solutions=%lld\n", s, k);
        }
    } else {
        for (int s1 = 0; s1 < n; s1++) for (int s2 = s1 + 1; s2 < n; s2++) {
            for (int i = 0; i < n; i++) side[i] = -1;
            side[s1] = 2; side[s2] = 2; nS++;
            long long k = run_S(); if (k) printf("S={%d,%d} solutions=%lld\n", s1, s2, k);
        }
    }
    printf("d=%d mode=%d cmax=%d plo=%d phi=%d sets_S=%lld solutions=%lld nodes=%lld\n",
           d, mode, cmax, plo, phi, nS, sols, nodes);
    return 0;
}
