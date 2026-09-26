/*
 ifvs_ls.c -- simulated annealing for an independent feedback vertex set S of Q_d with |S| = K.

 State: an independent set S of Q_d with |S| = K (independence is kept at all times).
 Cost : r(S) = cycle rank of F = Q_d - S  =  e(F) - |F| + c(F)  (0 iff F is a forest).
        For independent S of fixed size, e(F) and |F| are constants, so r = c(F) - (K(d-1) - (d-2)2^{d-1}).
 Move : pick u in S and a vertex v not in S such that (S - u) + v is independent
        (v has no S-neighbour, or its only S-neighbour is u); accept by Metropolis rule on r.
 Exit : r = 0 -> print S (one d-bit string per line, character k = coordinate k) and stop.

 Usage: ./ifvs_ls d K seed max_seconds [T0] [T1] [init_file]
 Build: gcc -O2 -o ifvs_ls ifvs_ls.c -lm
*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <time.h>

static int d, n, K;
static unsigned char inS[1 << 12];
static int sn[1 << 12];
static int par_[1 << 12];

static unsigned long long rs;
static inline unsigned long long rnd(void) {
    rs ^= rs << 13; rs ^= rs >> 7; rs ^= rs << 17; return rs;
}
static inline double urand(void) { return (rnd() >> 11) * (1.0 / 9007199254740992.0); }

static int findp(int x) { while (par_[x] != x) { par_[x] = par_[par_[x]]; x = par_[x]; } return x; }

/* number of components of F = V \ S */
static int comps(void) {
    int c = 0;
    for (int v = 0; v < n; v++) par_[v] = v;
    for (int v = 0; v < n; v++) {
        if (inS[v]) continue;
        c++;
        for (int j = 0; j < d; j++) {
            int w = v ^ (1 << j);
            if (w < v || inS[w]) continue;
            int a = findp(v), b = findp(w);
            if (a != b) { par_[a] = b; c--; }
        }
    }
    return c;
}

static void addS(int v) { inS[v] = 1; for (int j = 0; j < d; j++) sn[v ^ (1 << j)]++; }
static void remS(int v) { inS[v] = 0; for (int j = 0; j < d; j++) sn[v ^ (1 << j)]--; }

int main(int argc, char **argv) {
    if (argc < 5) { fprintf(stderr, "usage\n"); return 1; }
    d = atoi(argv[1]); K = atoi(argv[2]); rs = 0x9E3779B97F4A7C15ULL ^ (unsigned long long)atoll(argv[3]) * 2654435761ULL;
    if (!rs) rs = 1;
    double maxsec = atof(argv[4]);
    double T0 = argc > 5 ? atof(argv[5]) : 2.0, T1 = argc > 6 ? atof(argv[6]) : 0.05;
    n = 1 << d;
    for (int i = 0; i < 20; i++) rnd();
    int target_c = K * (d - 1) - (d - 2) * (n / 2);
    memset(inS, 0, sizeof inS); memset(sn, 0, sizeof sn);
    int Sl[1 << 12], ns = 0;
    if (argc > 7) {
        FILE *fp = fopen(argv[7], "r"); char buf[64];
        while (fgets(buf, sizeof buf, fp)) {
            if ((int)strlen(buf) < d) continue;
            int v = 0; for (int k = 0; k < d; k++) if (buf[k] == '1') v |= 1 << k;
            if (!inS[v] && sn[v] == 0) addS(v);
        }
        fclose(fp);
        for (int v = 0; v < n; v++) if (inS[v]) Sl[ns++] = v;
        /* trim or extend to K */
        while (ns > K) { int i = rnd() % ns; remS(Sl[i]); Sl[i] = Sl[--ns]; }
    }
    while (ns < K) {
        /* add random vertices of even class greedily (independent) */
        int v = rnd() % n;
        if (__builtin_popcount(v) & 1) continue;   /* even class: always independent */
        if (inS[v] || sn[v]) { continue; }
        addS(v); Sl[ns++] = v;
    }
    int c = comps();
    int best = c;
    long long it = 0;
    clock_t st = clock();
    double T = T0;
    int cand[64];
    while (1) {
        it++;
        if ((it & 1023) == 0) {
            double el = (double)(clock() - st) / CLOCKS_PER_SEC;
            if (el > maxsec) break;
            double fr = el / maxsec;
            T = T0 * pow(T1 / T0, fr);
            if ((it & ((1 << 20) - 1)) == 0) { fprintf(stderr, "it=%lld t=%.0f T=%.3f c=%d best=%d target=%d\n", it, el, T, c, best, target_c); }
        }
        int i = rnd() % ns, u = Sl[i];
        int v;
        /* candidate v: with prob 1/2 a neighbour of u whose only S-neighbour is u; else random free vertex */
        int nc = 0;
        if (rnd() & 1) {
            for (int j = 0; j < d; j++) { int w = u ^ (1 << j); if (sn[w] == 1) cand[nc++] = w; }
            if (!nc) continue;
            v = cand[rnd() % nc];
        } else {
            v = rnd() % n;
            if (inS[v]) continue;
            if (sn[v] == 0) { /* ok */ }
            else if (sn[v] == 1 && __builtin_popcount(u ^ v) == 1) { /* ok */ }
            else continue;
        }
        remS(u); addS(v);
        int c2 = comps();
        int dc = c2 - c;
        if (dc <= 0 || urand() < exp(-dc / T)) {
            c = c2; Sl[i] = v;
            if (c < best) { best = c; }
            if (c == target_c) break;
        } else { remS(v); addS(u); }
    }
    double el = (double)(clock() - st) / CLOCKS_PER_SEC;
    int r = c - target_c;
    printf("RESULT d=%d K=%d seed=%s c=%d target_c=%d r=%d best_c=%d iters=%lld time=%.1fs\n", d, K, argv[3], c, target_c, r, best, it, el);
    if (r == 0 || getenv("PRINT_ALWAYS")) {
        for (int v = 0; v < n; v++) if (inS[v]) {
            for (int k = 0; k < d; k++) putchar((v >> k) & 1 ? '1' : '0');
            putchar('\n');
        }
    }
    return 0;
}
