/* qls2.c -- simulated annealing for a large induced forest in a 9-regular multigraph given by
 * adjacency lists (a covering quotient of Q_9 by a free group action).  Exploratory search only;
 * results are re-verified exactly in Python (lift + direct acyclicity check in Q_9) and the final
 * labelling is scored by inbox/checker/verify.py.
 * Build: gcc -O2 -o qls2 qls2.c -lm
 * Usage: ./qls2 graph.txt seed iters T0 T1 outfile [init.txt]
 * graph.txt: first line n, then n lines 'deg w_1 .. w_deg' (deg <= 9) (repeated index = parallel edge;
 * no loops).  Move: add a vertex v not in F; drop every F-neighbour joined to v by a parallel
 * edge, and for each tree of F with >= 2 of v's neighbours keep one random neighbour and drop
 * the others; Metropolis acceptance on delta = 1 - dropped. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#define MAXN 4096
static int n, deg[MAXN], nb[MAXN][9], mult[MAXN][9];
static int inF[MAXN], comp[MAXN], stackv[MAXN];
static unsigned long long rs;
static unsigned long long rnd(void){ rs ^= rs << 13; rs ^= rs >> 7; rs ^= rs << 17; return rs; }
static double urand(void){ return (rnd() >> 11) * (1.0/9007199254740992.0); }
static void components(void){
  for (int v = 0; v < n; v++) comp[v] = -1;
  int c = 0;
  for (int s = 0; s < n; s++) if (inF[s] && comp[s] < 0){
    int sp = 0; stackv[sp++] = s; comp[s] = c;
    while (sp){ int v = stackv[--sp];
      for (int j = 0; j < deg[v]; j++){ int w = nb[v][j]; if (inF[w] && comp[w] < 0){ comp[w] = c; stackv[sp++] = w; } } }
    c++;
  }
}
int main(int argc, char **argv){
  if (argc < 7){ fprintf(stderr, "usage\n"); return 1; }
  FILE *fg = fopen(argv[1], "r"); if (fscanf(fg, "%d", &n) != 1) return 1;
  for (int v = 0; v < n; v++){ int raw[9], dv; deg[v] = 0;
    if (fscanf(fg, "%d", &dv) != 1 || dv > 9) return 1;
    for (int j = 0; j < dv; j++){ if (fscanf(fg, "%d", &raw[j]) != 1) return 1; }
    for (int j = 0; j < dv; j++){ int f = -1; for (int t = 0; t < deg[v]; t++) if (nb[v][t] == raw[j]) f = t;
      if (f < 0){ nb[v][deg[v]] = raw[j]; mult[v][deg[v]] = 1; deg[v]++; } else mult[v][f]++; } }
  fclose(fg);
  rs = strtoull(argv[2], 0, 10) * 2654435761ULL + 88172645463325252ULL;
  long iters = atol(argv[3]); double T0 = atof(argv[4]), T1 = atof(argv[5]);
  memset(inF, 0, sizeof inF);
  int size = 0, best = 0; static int bestF[MAXN];
  if (argc > 7){ FILE *fi = fopen(argv[7], "r"); int v; while (fscanf(fi, "%d", &v) == 1){ inF[v] = 1; size++; } fclose(fi); best = size; memcpy(bestF, inF, sizeof inF); }
  components();
  int nbuf[9], cbuf[9], rem[9];
  for (long it = 0; it < iters; it++){
    double T = T0 * pow(T1 / T0, (double)it / iters);
    int v = rnd() % n; if (inF[v]) continue;
    int cnt = 0, nrem = 0;
    for (int j = 0; j < deg[v]; j++){ int w = nb[v][j]; if (inF[w]){ if (mult[v][j] > 1) rem[nrem++] = w; else { nbuf[cnt] = w; cbuf[cnt] = comp[w]; cnt++; } } }
    for (int a = 0; a < cnt; a++){ if (nbuf[a] < 0) continue;
      int grp[9], g = 0; for (int b = a; b < cnt; b++) if (nbuf[b] >= 0 && cbuf[b] == cbuf[a]) grp[g++] = b;
      int keep = rnd() % g; for (int t = 0; t < g; t++){ if (t != keep) rem[nrem++] = nbuf[grp[t]]; nbuf[grp[t]] = -1; } }
    int delta = 1 - nrem;
    if (delta >= 0 || urand() < exp(delta / T)){
      for (int t = 0; t < nrem; t++) inF[rem[t]] = 0;
      inF[v] = 1; size += delta;
      components();
      if (size > best){ best = size; memcpy(bestF, inF, sizeof inF); }
    }
  }
  FILE *fo = fopen(argv[6], "w");
  for (int v = 0; v < n; v++) if (bestF[v]) fprintf(fo, "%d\n", v);
  fclose(fo);
  printf("best=%d\n", best);
  return 0;
}
