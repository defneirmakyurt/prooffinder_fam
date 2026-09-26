/* fsa.c -- simulated annealing for a large induced forest F of Q_9 inside a restricted class:
 * vertices listed in a "fixed" file are forced (in or out); all other vertices are free.
 * Heuristic only (never a proof of anything). Output: indicator line (char v = '1' iff v in F).
 *
 * Move: pick a free vertex v not in F, add it; while Q_9[F] has a cycle through v, pick two F-neighbours of v
 * in the same tree, and delete a random free vertex of the tree path between them (or the path through v).
 * Metropolis acceptance on delta|F| at temperature T (geometric cooling from T0 to T1).
 *
 * Usage: fsa fixedfile seed moves T0 T1 out.txt
 *   fixedfile: one line of 512 chars: '1' forced in, '0' forced out, '.' free   (or "-" for all free)
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define D 9
#define NV 512
static int inF[NV], fixedv[NV]; /* fixedv: -1 free, 0 forced out, 1 forced in */
static unsigned long long rs;
static unsigned long long rnd(void) { rs ^= rs << 13; rs ^= rs >> 7; rs ^= rs << 17; return rs; }
static double urand(void) { return (rnd() >> 11) * (1.0 / 9007199254740992.0); }

/* BFS in F from s, avoiding vertex 'avoid'; parent pointers; returns 1 if t reached */
static int par[NV], mark[NV], stamp = 0;
static int bfs_path(int s, int t, int avoid) {
    static int q[NV];
    stamp++;
    int h = 0, tl = 0; q[tl++] = s; mark[s] = stamp; par[s] = -1;
    while (h < tl) {
        int x = q[h++];
        if (x == t) return 1;
        for (int b = 0; b < D; b++) {
            int y = x ^ (1 << b);
            if (!inF[y] || y == avoid || mark[y] == stamp) continue;
            mark[y] = stamp; par[y] = x; q[tl++] = y;
        }
    }
    return 0;
}

static int nF = 0;
static int changed[NV], nch; static int chval[NV];
static void setF(int v, int val) { changed[nch] = v; chval[nch] = inF[v]; nch++; inF[v] = val; nF += val ? 1 : -1; }

/* after adding v, repair cycles through v; returns 0 if impossible (only forced vertices on a cycle) */
static int repair(int v) {
    for (int guard = 0; guard < 100; guard++) {
        int nb[D], r = 0;
        for (int b = 0; b < D; b++) { int y = v ^ (1 << b); if (inF[y]) nb[r++] = y; }
        int found = 0;
        for (int i = 0; i < r && !found; i++) for (int j = i + 1; j < r && !found; j++) {
            if (bfs_path(nb[i], nb[j], v)) {
                /* cycle: v, nb[i], ..., nb[j], v. candidates: free vertices on it */
                int cand[NV], c = 0;
                for (int x = nb[j]; x != -1; x = par[x]) if (fixedv[x] < 0) cand[c++] = x;
                if (fixedv[v] < 0) cand[c++] = v;
                if (c == 0) return 0;
                int z = cand[rnd() % c];
                setF(z, 0);
                if (z == v) return 1;
                found = 1;
            }
        }
        if (!found) return 1;
    }
    return 0;
}

static int check_forest(void) {
    int p[NV]; for (int i = 0; i < NV; i++) p[i] = i;
    for (int v = 0; v < NV; v++) if (inF[v]) for (int b = 0; b < D; b++) { int w = v ^ (1 << b);
        if (w > v && inF[w]) { int a = v, c = w; while (p[a] != a) a = p[a]; while (p[c] != c) c = p[c]; if (a == c) return 0; p[a] = c; } }
    return 1;
}

int main(int argc, char **argv) {
    if (argc < 7) { fprintf(stderr, "usage\n"); return 1; }
    rs = 88172645463325252ULL ^ (unsigned long long)atoll(argv[2]) * 2654435761ULL; for (int i = 0; i < 10; i++) rnd();
    long long moves = atoll(argv[3]); double T0 = atof(argv[4]), T1 = atof(argv[5]);
    for (int v = 0; v < NV; v++) fixedv[v] = -1;
    if (strcmp(argv[1], "-") != 0) {
        FILE *f = fopen(argv[1], "r"); char buf[1024]; if (!f || !fgets(buf, sizeof buf, f)) { fprintf(stderr, "bad fixed file\n"); return 1; }
        for (int v = 0; v < NV; v++) fixedv[v] = buf[v] == '1' ? 1 : buf[v] == '0' ? 0 : -1;
        fclose(f);
    }
    for (int v = 0; v < NV; v++) inF[v] = 0;
    nF = 0; nch = 0;
    for (int v = 0; v < NV; v++) if (fixedv[v] == 1) setF(v, 1);
    if (!check_forest()) { printf("forced-in set is not a forest\n"); return 1; }
    int freev[NV], nfree = 0; for (int v = 0; v < NV; v++) if (fixedv[v] < 0) freev[nfree++] = v;
    int best = nF, bestF[NV]; memcpy(bestF, inF, sizeof(inF));
    for (long long it = 0; it < moves; it++) {
        double T = T0 * pow(T1 / T0, (double)it / moves);
        int v = freev[rnd() % nfree];
        if (inF[v]) continue;
        nch = 0; int before = nF;
        setF(v, 1);
        int ok = repair(v);
        int delta = nF - before;
        if (ok && (delta >= 0 || urand() < exp(delta / T))) {
            if (nF > best) { best = nF; memcpy(bestF, inF, sizeof(inF)); }
        } else {
            for (int i = nch - 1; i >= 0; i--) { inF[changed[i]] = chval[i]; }
            nF = before;
        }
    }
    memcpy(inF, bestF, sizeof(inF));
    int okf = check_forest();
    FILE *fo = fopen(argv[6], "w"); for (int v = 0; v < NV; v++) fputc(inF[v] ? '1' : '0', fo); fputc('\n', fo); fclose(fo);
    printf("best |F|=%d |S|=%d forest_recheck=%s\n", best, NV - best, okf ? "ok" : "FAIL");
    return 0;
}
