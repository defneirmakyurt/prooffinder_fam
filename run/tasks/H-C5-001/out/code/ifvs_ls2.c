/*
 ifvs_ls2.c -- variable-size simulated annealing for an independent feedback vertex set of Q_d.
 (compiled with -DNOINDEP: plain feedback vertex set, independence NOT required -> binary fvs_ls)
 State: independent set S (kept independent).  Cost Phi = (d-1)|S| + W * r,  r = cycle rank of Q_d - S.
 Moves: add a vertex with no S-neighbour; remove a vertex of S; swap (remove u, add v, v's only S-nbr is u
        or v free).  Metropolis acceptance on Phi.  Records states with r = 0 and |S| <= K (prints first found).
 Usage: ./ifvs_ls2 d K seed seconds W T0 T1 [init: 0 = empty, 1 = random even-class of size K]
 Output: "RESULT ..." line, then S (one d-bit string per line, char k = coordinate k) if a state with r=0,|S|<=K was hit.
 Build: gcc -O2 -o ifvs_ls2 ifvs_ls2.c -lm
*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <time.h>
static int d, n, K;
static unsigned char inS[1 << 12];
static int sn[1 << 12], par_[1 << 12], pos[1 << 12], Sl[1 << 12], ns;
static unsigned long long rs;
static inline unsigned long long rnd(void) { rs ^= rs << 13; rs ^= rs >> 7; rs ^= rs << 17; return rs; }
static inline double urand(void) { return (rnd() >> 11) * (1.0 / 9007199254740992.0); }
static int findp(int x) { while (par_[x] != x) { par_[x] = par_[par_[x]]; x = par_[x]; } return x; }
static int rank_(void) { /* cycle rank e - v + c of F */
    int c = 0, e = 0, v_ = 0;
    for (int v = 0; v < n; v++) par_[v] = v;
    for (int v = 0; v < n; v++) {
        if (inS[v]) continue;
        v_++; c++;
        for (int j = 0; j < d; j++) {
            int w = v ^ (1 << j);
            if (w < v || inS[w]) continue;
            e++;
            int a = findp(v), b = findp(w);
            if (a != b) { par_[a] = b; c--; }
        }
    }
    return e - v_ + c;
}
static void addS(int v) { inS[v] = 1; for (int j = 0; j < d; j++) sn[v ^ (1 << j)]++; pos[v] = ns; Sl[ns++] = v; }
static void remS(int v) { inS[v] = 0; for (int j = 0; j < d; j++) sn[v ^ (1 << j)]--; int i = pos[v]; Sl[i] = Sl[--ns]; pos[Sl[i]] = i; }
int main(int argc, char **argv) {
    d = atoi(argv[1]); K = atoi(argv[2]); rs = 0x9E3779B97F4A7C15ULL ^ (unsigned long long)atoll(argv[3]) * 2654435761ULL;
    double maxsec = atof(argv[4]); double W = atof(argv[5]); double T0 = atof(argv[6]), T1 = atof(argv[7]);
    int init = argc > 8 ? atoi(argv[8]) : 0;
    n = 1 << d; for (int i = 0; i < 20; i++) rnd();
    if (init == 1) { while (ns < K) { int v = rnd() % n; if (__builtin_popcount(v) & 1) continue; if (!inS[v]) addS(v); } }
    int r = rank_();
    double phi = (d - 1) * ns + W * r, best = 1e18; int bestS = 0, bestr = 0;
    long long it = 0; clock_t st = clock(); double T = T0; int found = 0;
    while (1) {
        it++;
        if ((it & 1023) == 0) {
            double el = (double)(clock() - st) / CLOCKS_PER_SEC;
            if (el > maxsec) break;
            T = T0 * pow(T1 / T0, el / maxsec);
            if ((it & ((1 << 22) - 1)) == 0) fprintf(stderr, "t=%.0f T=%.2f |S|=%d r=%d phi=%.0f best=%.0f (|S|=%d r=%d)\n", el, T, ns, r, phi, best, bestS, bestr);
        }
        int typ = rnd() % 3, u = -1, v = -1;
        if (typ == 0) { v = rnd() % n; if (inS[v]) continue;
#ifndef NOINDEP
            if (sn[v]) continue;
#endif
            addS(v); }
        else if (typ == 1) { if (!ns) continue; u = Sl[rnd() % ns]; remS(u); }
        else {
            if (!ns) continue; u = Sl[rnd() % ns];
            if (rnd() & 1) { int j = rnd() % d; v = u ^ (1 << j);
#ifdef NOINDEP
                if (inS[v]) continue;
#else
                if (sn[v] != 1) continue;
#endif
            }
            else { v = rnd() % n; if (inS[v]) continue;
#ifndef NOINDEP
                if (!(sn[v] == 0 || (sn[v] == 1 && __builtin_popcount(u ^ v) == 1))) continue;
#endif
            }
            remS(u); addS(v);
        }
        int r2 = rank_();
        double phi2 = (d - 1) * ns + W * r2;
        if (phi2 <= phi || urand() < exp((phi - phi2) / T)) {
            phi = phi2; r = r2;
            if (phi < best) { best = phi; bestS = ns; bestr = r; }
            if (r == 0 && ns <= K) { found = 1; break; }
        } else {
            if (typ == 0) remS(v); else if (typ == 1) addS(u); else { remS(v); addS(u); }
        }
    }
    double el = (double)(clock() - st) / CLOCKS_PER_SEC;
    int ev = 0; for (int i = 0; i < ns; i++) if (!(__builtin_popcount(Sl[i]) & 1)) ev++;
    printf("RESULT d=%d K=%d seed=%s W=%.1f found=%d |S|=%d r=%d even=%d odd=%d best_phi=%.0f(|S|=%d r=%d) iters=%lld time=%.1fs\n",
           d, K, argv[3], W, found, ns, r, ev, ns - ev, best, bestS, bestr, it, el);
    if (found || getenv("PRINT_ALWAYS")) for (int v = 0; v < n; v++) if (inS[v]) { for (int k = 0; k < d; k++) putchar((v >> k) & 1 ? '1' : '0'); putchar('\n'); }
    return 0;
}
