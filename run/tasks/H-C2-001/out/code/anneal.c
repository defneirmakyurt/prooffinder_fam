/* anneal.c -- simulated annealing over labellings of Q_d (search-internal scorer only;
 * every reported score is re-checked with inbox/checker/verify.py).
 * Usage: ./anneal D SEED ITERS OUTFILE
 * Labelling = order[0..n-1]: order[i] is the vertex with label i+1.
 * Score T = sum_v N(v), N(v) = [valley] + sum_{lower nbrs w} N(w)  (saturating uint64).
 * Moves: move one vertex from position i to position j (insertion), or swap two positions.
 */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>
#include <string.h>

static int D, n;
static uint64_t rng_s;
static inline uint64_t rng(void) { rng_s ^= rng_s << 13; rng_s ^= rng_s >> 7; rng_s ^= rng_s << 17; return rng_s; }
static inline double urand(void) { return (rng() >> 11) * (1.0 / 9007199254740992.0); }

static uint64_t score(const int *order) {
    int f[1 << 10]; uint64_t N[1 << 10];
    for (int i = 0; i < n; i++) f[order[i]] = i;
    uint64_t tot = 0;
    for (int i = 0; i < n; i++) {
        int v = order[i]; uint64_t s = 0; int valley = 1;
        for (int j = 0; j < D; j++) {
            int w = v ^ (1 << j);
            if (f[w] < i) { valley = 0; s += N[w]; if (s > (1ULL << 60)) s = 1ULL << 60; }
        }
        N[v] = s + valley; tot += N[v]; if (tot > (1ULL << 61)) tot = 1ULL << 61;
    }
    return tot;
}

int main(int argc, char **argv) {
    if (argc < 5) { fprintf(stderr, "usage: anneal D SEED ITERS OUTFILE\n"); return 1; }
    D = atoi(argv[1]); n = 1 << D; rng_s = strtoull(argv[2], 0, 10) * 2654435761ULL + 88172645463325252ULL;
    long long iters = atoll(argv[3]);
    int order[1 << 10], best[1 << 10], tmp[1 << 10];
    for (int i = 0; i < n; i++) order[i] = i;
    for (int i = n - 1; i > 0; i--) { int j = rng() % (i + 1); int t = order[i]; order[i] = order[j]; order[j] = t; }
    uint64_t cur = score(order), bs = cur; memcpy(best, order, sizeof(int) * n);
    double T0 = 3.0, T1 = 0.05;
    for (long long it = 0; it < iters; it++) {
        double temp = T0 * pow(T1 / T0, (double)it / iters);
        memcpy(tmp, order, sizeof(int) * n);
        int i = rng() % n, j = rng() % n;
        if (rng() & 1) { int t = tmp[i]; tmp[i] = tmp[j]; tmp[j] = t; }
        else {
            int v = tmp[i];
            if (i < j) memmove(tmp + i, tmp + i + 1, sizeof(int) * (j - i));
            else memmove(tmp + j + 1, tmp + j, sizeof(int) * (i - j));
            tmp[j] = v;
        }
        uint64_t s = score(tmp);
        if (s <= cur || urand() < exp(-((double)s - (double)cur) / temp)) {
            memcpy(order, tmp, sizeof(int) * n); cur = s;
            if (s < bs) { bs = s; memcpy(best, order, sizeof(int) * n); }
        }
    }
    FILE *fo = fopen(argv[4], "w");
    for (int i = 0; i < n; i++) {
        for (int b = D - 1; b >= 0; b--) fputc('0' + ((best[i] >> b) & 1), fo);
        fputc('\n', fo);
    }
    fclose(fo);
    printf("seed %s iters %lld best %llu\n", argv[2], iters, (unsigned long long)bs);
    return 0;
}
