/*
 * anneal.c -- simulated annealing directly on labellings of Q_d (rung R6).
 * State: order[0..n-1], order[i] = vertex with label i+1.  Score = number of uphill paths,
 * computed exactly by the recursion N(v) = [v valley] + sum_{w ~ v, f(w) < f(v)} N(w)
 * (same recursion as the provided checker; unsigned 64-bit, no overflow for d <= 6 since
 * the score is at most the number of increasing paths < 64 * 6^63 ... we cap: scores are
 * compared only after saturating at 2^62, which never matters near the optimum).
 * Moves: swap the labels of two random vertices, or move one vertex to another position.
 * Metropolis at temperature T, geometric cooling; restarts from random permutations.
 * The final artefact is re-scored by the provided checker verify.py; this is only the
 * inner-loop scorer.
 *
 * Build: gcc -O2 -o anneal anneal.c -lm
 * Run:   ./anneal d seed steps_per_restart restarts out.txt [T0 T1]
 */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

static unsigned long long s_rng;
static unsigned long long rnd(void) { s_rng ^= s_rng << 13; s_rng ^= s_rng >> 7; s_rng ^= s_rng << 17; return s_rng; }
static double urand(void) { return (rnd() >> 11) * (1.0 / 9007199254740992.0); }

static int d, n;
#define CAP (1ULL << 62)
static unsigned long long score(const int *order) {
    int f[1024]; unsigned long long N[1024], tot = 0;
    for (int i = 0; i < n; i++) f[order[i]] = i;
    for (int i = 0; i < n; i++) {
        int v = order[i]; unsigned long long s = 0; int valley = 1;
        for (int j = 0; j < d; j++) {
            int w = v ^ (1 << j);
            if (f[w] < i) { valley = 0; s += N[w]; if (s > CAP) s = CAP; }
        }
        N[v] = s + valley; tot += N[v]; if (tot > CAP) tot = CAP;
    }
    return tot;
}

int main(int argc, char **argv) {
    if (argc < 6) { fprintf(stderr, "usage: d seed steps restarts out [T0 T1]\n"); return 2; }
    d = atoi(argv[1]); n = 1 << d;
    unsigned long long seed = strtoull(argv[2], 0, 10);
    long steps = atol(argv[3]); int R = atoi(argv[4]);
    double T0 = argc > 6 ? atof(argv[6]) : 3.0, T1 = argc > 7 ? atof(argv[7]) : 0.2;
    s_rng = seed * 0x9E3779B97F4A7C15ULL + 777; if (!s_rng) s_rng = 1;
    for (int i = 0; i < 20; i++) rnd();
    int order[1024], best[1024]; unsigned long long bestsc = ~0ULL; long total = 0;
    for (int r = 1; r <= R; r++) {
        for (int i = 0; i < n; i++) order[i] = i;
        for (int i = n - 1; i > 0; i--) { int j = rnd() % (i + 1); int t = order[i]; order[i] = order[j]; order[j] = t; }
        unsigned long long cur = score(order), rb = cur;
        for (long t = 0; t < steps; t++) {
            total++;
            double T = T0 * pow(T1 / T0, (double)t / steps);
            int a = rnd() % n, b = rnd() % n; if (a == b) continue;
            int tmp[1024], mv = rnd() & 1;
            if (mv) { int x = order[a]; order[a] = order[b]; order[b] = x; }
            else {
                for (int i = 0; i < n; i++) tmp[i] = order[i];
                int x = order[a];
                if (a < b) { for (int i = a; i < b; i++) order[i] = order[i + 1]; }
                else { for (int i = a; i > b; i--) order[i] = order[i - 1]; }
                order[b] = x;
            }
            unsigned long long nw = score(order);
            double delta = (double)nw - (double)cur;
            if (nw <= cur || urand() < exp(-delta / T)) {
                cur = nw;
                if (cur < rb) rb = cur;
                if (cur < bestsc) { bestsc = cur; for (int i = 0; i < n; i++) best[i] = order[i]; }
            } else {
                if (mv) { int x = order[a]; order[a] = order[b]; order[b] = x; }
                else for (int i = 0; i < n; i++) order[i] = tmp[i];
            }
        }
        fprintf(stderr, "restart %d best-in-restart %llu global %llu\n", r, rb, bestsc);
    }
    FILE *fo = fopen(argv[5], "w");
    for (int i = 0; i < n; i++) { for (int b = d - 1; b >= 0; b--) fputc((best[i] >> b) & 1 ? '1' : '0', fo); fputc('\n', fo); }
    fclose(fo);
    printf("d=%d seed=%llu restarts=%d total_steps=%ld best=%llu\n", d, seed, R, total, bestsc);
    return 0;
}
