/*
 ls3.c -- simulated annealing over arbitrary vertex sets S of Q_d, scored by the EXACT number of uphill
 paths of the labelling L(S):
     labels 1..|F| : F = V \ S in BFS order (component by component, BFS from the smallest unvisited vertex),
     labels |F|+1.. : S sorted by (number of neighbours in F) ascending, ties by vertex index.
 Counting = the same recurrence as the provided checker: N(v) = [valley] + sum N(w), w ~ v, f(w) < f(v).
 Moves: toggle a random vertex; or move an S-vertex to a random neighbour.  Metropolis on the count.
 Usage: ./ls3 d seed seconds T0 T1 init_S_file target
 Prints RESULT line; writes best labelling (hand-in format: line i = vertex with label i, char k = coordinate k)
 to stdout after the RESULT line.
 Build: gcc -O2 -o ls3 ls3.c -lm
*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <time.h>
static int d, n;
static unsigned char inS[1 << 12], bestS[1 << 12];
static int order_[1 << 12], f_[1 << 12], seen[1 << 12], dF[1 << 12];
static long long N_[1 << 12];
static unsigned long long rs;
static inline unsigned long long rnd(void) { rs ^= rs << 13; rs ^= rs >> 7; rs ^= rs << 17; return rs; }
static inline double urand(void) { return (rnd() >> 11) * (1.0 / 9007199254740992.0); }
static void build(void) {
    int k = 0;
    memset(seen, 0, sizeof(int) * n);
    for (int r = 0; r < n; r++) {
        if (inS[r] || seen[r]) continue;
        seen[r] = 1; int qs = k; order_[k++] = r;
        while (qs < k) { int u = order_[qs++];
            for (int j = 0; j < d; j++) { int w = u ^ (1 << j); if (!inS[w] && !seen[w]) { seen[w] = 1; order_[k++] = w; } } }
    }
    /* S sorted by dF ascending: counting sort */
    int cnt[64] = {0};
    for (int v = 0; v < n; v++) if (inS[v]) { int c = 0; for (int j = 0; j < d; j++) if (!inS[v ^ (1 << j)]) c++; dF[v] = c; cnt[c]++; }
    int start[64]; int s = k; for (int c = 0; c <= d; c++) { start[c] = s; s += cnt[c]; }
    for (int v = 0; v < n; v++) if (inS[v]) order_[start[dF[v]]++] = v;
}
static long long count_(void) {
    build();
    for (int i = 0; i < n; i++) f_[order_[i]] = i;
    long long tot = 0;
    for (int i = 0; i < n; i++) { int v = order_[i]; long long s = 0; int valley = 1;
        for (int j = 0; j < d; j++) { int w = v ^ (1 << j); if (f_[w] < i) { s += N_[w]; valley = 0; } }
        N_[v] = s + valley; tot += N_[v]; }
    return tot;
}
int main(int argc, char **argv) {
    d = atoi(argv[1]); rs = 0x9E3779B97F4A7C15ULL ^ (unsigned long long)atoll(argv[2]) * 2654435761ULL;
    double maxsec = atof(argv[3]), T0 = atof(argv[4]), T1 = atof(argv[5]); long long target = atoll(argv[7]);
    n = 1 << d; for (int i = 0; i < 20; i++) rnd();
    FILE *fp = fopen(argv[6], "r"); char buf[64];
    while (fgets(buf, sizeof buf, fp)) { if ((int)strlen(buf) < d) continue; int v = 0; for (int k = 0; k < d; k++) if (buf[k] == '1') v |= 1 << k; inS[v] = 1; }
    fclose(fp);
    long long cur = count_(), best = cur; memcpy(bestS, inS, n);
    long long it = 0; clock_t st = clock(); double T = T0;
    fprintf(stderr, "init count=%lld\n", cur);
    while (1) {
        it++;
        if ((it & 255) == 0) { double el = (double)(clock() - st) / CLOCKS_PER_SEC; if (el > maxsec) break; T = T0 * pow(T1 / T0, el / maxsec);
            if ((it & ((1 << 18) - 1)) == 0) fprintf(stderr, "t=%.0f T=%.2f cur=%lld best=%lld\n", el, T, cur, best); }
        int a, b = -1;
        if (rnd() & 1) { a = rnd() % n; inS[a] ^= 1; }
        else { do { a = rnd() % n; } while (!inS[a]); b = a ^ (1 << (rnd() % d)); if (inS[b]) continue; inS[a] = 0; inS[b] = 1; }
        long long c2 = count_();
        if (c2 <= cur || urand() < exp((double)(cur - c2) / T)) {
            cur = c2; if (cur < best) { best = cur; memcpy(bestS, inS, n); if (best <= target) break; }
        } else { if (b < 0) inS[a] ^= 1; else { inS[a] = 1; inS[b] = 0; } }
    }
    memcpy(inS, bestS, n); long long chk = count_();
    int ns = 0; for (int v = 0; v < n; v++) ns += inS[v];
    printf("RESULT d=%d seed=%s best=%lld recount=%lld |S|=%d iters=%lld time=%.1fs\n", d, argv[2], best, chk, ns, it, (double)(clock() - st) / CLOCKS_PER_SEC);
    for (int i = 0; i < n; i++) { int v = order_[i]; for (int k = 0; k < d; k++) putchar((v >> k) & 1 ? '1' : '0'); putchar('\n'); }
    return 0;
}
