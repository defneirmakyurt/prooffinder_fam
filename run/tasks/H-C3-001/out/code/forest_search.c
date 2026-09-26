/*
 * forest_search.c -- C version of forest_search.py (same cost, same moves), fast.
 * Local search for an independent set P of Q_d, |P| = p, with Q_d - P a forest.
 * Cost = #edges inside P + cyclomatic number of Q_d[A] (A = V - P); cost 0 = success.
 * Moves: swap x in P with y in A; Metropolis at temperature T, geometric cooling per restart.
 * On success writes the labelling of rung R4: trees of Q_d[A] in BFS order, then P.
 * Integer cost, deterministic given seed (own xorshift PRNG).
 *
 * Build: gcc -O2 -o forest_search forest_search.c -lm
 * Run:   ./forest_search d p seed steps_per_restart max_restarts out.txt
 */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

static unsigned long long s_rng;
static unsigned long long rnd(void) {
    s_rng ^= s_rng << 13; s_rng ^= s_rng >> 7; s_rng ^= s_rng << 17; return s_rng;
}
static double urand(void) { return (rnd() >> 11) * (1.0 / 9007199254740992.0); }

static int d, n;
static int inA[1024], par[1024];
static int findr(int x) { while (par[x] != x) { par[x] = par[par[x]]; x = par[x]; } return x; }

static int cost(int *comps_out) {
    int bad = 0, e = 0, nA = 0, c = 0;
    for (int v = 0; v < n; v++) par[v] = v;
    for (int v = 0; v < n; v++) {
        if (inA[v]) nA++;
        for (int j = 0; j < d; j++) {
            int w = v ^ (1 << j);
            if (w <= v) continue;
            if (!inA[v] && !inA[w]) bad++;
            else if (inA[v] && inA[w]) {
                e++;
                int a = findr(v), b = findr(w);
                if (a != b) par[a] = b;
            }
        }
    }
    for (int v = 0; v < n; v++) if (inA[v] && findr(v) == v) c++;
    if (comps_out) *comps_out = c;
    return bad + (e - nA + c);
}

int main(int argc, char **argv) {
    if (argc < 7) { fprintf(stderr, "usage: d p seed steps restarts out\n"); return 2; }
    d = atoi(argv[1]); n = 1 << d;
    int p = atoi(argv[2]);
    unsigned long long seed = strtoull(argv[3], 0, 10);
    long steps = atol(argv[4]);
    int maxr = atoi(argv[5]);
    s_rng = seed * 0x9E3779B97F4A7C15ULL + 12345; if (!s_rng) s_rng = 1;
    for (int i = 0; i < 20; i++) rnd();
    int Pl[1024], Al[1024];
    long total = 0;
    int found = 0, r;
    double T0 = 1.5, T1 = 0.08;
    for (r = 1; r <= maxr && !found; r++) {
        /* random P of size p */
        int perm[1024];
        for (int i = 0; i < n; i++) perm[i] = i;
        for (int i = n - 1; i > 0; i--) { int j = rnd() % (i + 1); int t = perm[i]; perm[i] = perm[j]; perm[j] = t; }
        for (int i = 0; i < n; i++) inA[i] = 1;
        for (int i = 0; i < p; i++) inA[perm[i]] = 0;
        int np = 0, na = 0;
        for (int v = 0; v < n; v++) { if (inA[v]) Al[na++] = v; else Pl[np++] = v; }
        int cur = cost(0), best = cur;
        for (long t = 0; t < steps; t++) {
            if (cur < best) best = cur;
            total++;
            if (cur == 0) { found = 1; break; }
            double T = T0 * pow(T1 / T0, (double)t / steps);
            int i = rnd() % np, k = rnd() % na;
            int x = Pl[i], y = Al[k];
            inA[x] = 1; inA[y] = 0;
            int nw = cost(0);
            if (nw <= cur || urand() < exp((cur - nw) / T)) {
                cur = nw; Pl[i] = y; Al[k] = x;
            } else { inA[x] = 0; inA[y] = 1; }
        }
        if (cur == 0) found = 1;
        if (getenv("VERBOSE")) fprintf(stderr, "restart %d best cost %d final %d\n", r, best, cur);
    }
    if (!found) { printf("d=%d p=%d seed=%llu NOT FOUND after %d restarts, %ld steps\n", d, p, seed, maxr, total); return 1; }
    int comps; cost(&comps);
    /* build order: BFS each tree from its smallest-index vertex... root choice randomised */
    int seen[1024] = {0}, order[1024], m = 0, ntrees = 0;
    int Av[1024], na = 0;
    for (int v = 0; v < n; v++) if (inA[v]) Av[na++] = v;
    for (int i = na - 1; i > 0; i--) { int j = rnd() % (i + 1); int t = Av[i]; Av[i] = Av[j]; Av[j] = t; }
    for (int i = 0; i < na; i++) {
        int rt = Av[i]; if (seen[rt]) continue;
        ntrees++; seen[rt] = 1; int q0 = m; order[m++] = rt;
        while (q0 < m) {
            int v = order[q0++];
            for (int j = 0; j < d; j++) { int w = v ^ (1 << j); if (inA[w] && !seen[w]) { seen[w] = 1; order[m++] = w; } }
        }
    }
    for (int v = 0; v < n; v++) if (!inA[v]) order[m++] = v;
    FILE *fo = fopen(argv[6], "w");
    for (int i = 0; i < n; i++) {
        for (int b = d - 1; b >= 0; b--) fputc((order[i] >> b) & 1 ? '1' : '0', fo);
        fputc('\n', fo);
    }
    fclose(fo);
    printf("d=%d p=%d seed=%llu FOUND restarts=%d total_steps=%ld trees=%d predicted=%d\n",
           d, p, seed, r - 1, total, ntrees, ntrees + d * (n / 2));
    return 0;
}
