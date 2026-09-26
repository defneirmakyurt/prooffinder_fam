/* qls.c -- simulated annealing for a large induced forest in a Cayley multigraph
 * Cay(F_2^k, {g_1..g_9}) (a covering quotient Q_9/C).  Exploratory search only; every
 * result is re-verified exactly in Python (quotients.is_forest_multi, lift + is_forest_qd)
 * and the final labelling is scored by inbox/checker/verify.py.
 * Build: gcc -O2 -o qls qls.c -lm
 * Usage: ./qls k g1 g2 ... g9 seed iters T0 T1 outfile
 * Move: pick v not in F, add it; for every tree of F containing >= 2 of v's F-neighbours (or a
 * neighbour joined to v by a parallel edge) remove all but one random such neighbour (the parallel
 * one is always removed); accept by Metropolis on delta = 1 - removed. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

static int k, n, gens[9], DEG;
static int nb[4096][9];
static int mult[4096][9];     /* multiplicity of edge v - nb[v][j] (>=2 means parallel) */
static int inF[4096], comp[4096];
static unsigned long long rs;
static unsigned long long rnd(void){ rs ^= rs << 13; rs ^= rs >> 7; rs ^= rs << 17; return rs; }
static double urand(void){ return (rnd() >> 11) * (1.0/9007199254740992.0); }

static int stackv[4096];
static void components(void){
  for (int v = 0; v < n; v++) comp[v] = -1;
  int c = 0;
  for (int s = 0; s < n; s++) if (inF[s] && comp[s] < 0){
    int sp = 0; stackv[sp++] = s; comp[s] = c;
    while (sp){ int v = stackv[--sp];
      for (int j = 0; j < 9 && nb[v][j] >= 0; j++){ int w = nb[v][j]; if (w != v && inF[w] && comp[w] < 0){ comp[w] = c; stackv[sp++] = w; } } }
    c++;
  }
}
/* exact acyclicity check of F: edges - vertices + components == 0 and no parallel pair / loop */
static int check(void){
  long e = 0; int vs = 0;
  for (int v = 0; v < n; v++) if (inF[v]){ vs++;
    for (int j = 0; j < DEG; j++){ int w = nb[v][j]; if (w == v) return 0; if (inF[w]){ if (mult[v][j] > 1) return 0; e++; } } }
  e /= 2; /* each simple edge counted twice (distinct neighbours listed once each) */
  components();
  int c = 0; for (int v = 0; v < n; v++) if (inF[v] && comp[v] + 1 > c) c = comp[v] + 1;
  return e == vs - c;
}

int main(int argc, char **argv){
  if (argc < 16){ fprintf(stderr, "usage\n"); return 1; }
  k = atoi(argv[1]); n = 1 << k;
  for (int i = 0; i < 9; i++) gens[i] = atoi(argv[2+i]);
  rs = strtoull(argv[11], 0, 10) * 2654435761ULL + 88172645463325252ULL;
  long iters = atol(argv[12]); double T0 = atof(argv[13]), T1 = atof(argv[14]);
  /* distinct neighbour lists with multiplicity */
  int deg = 0; (void)0;
  int dg[9], ml[9];
  for (int i = 0; i < 9; i++){ int f = -1; for (int j = 0; j < deg; j++) if (dg[j] == gens[i]) f = j;
    if (f < 0){ dg[deg] = gens[i]; ml[deg] = 1; deg++; } else ml[f]++; }
  for (int v = 0; v < n; v++) for (int j = 0; j < 9; j++){ if (j < deg){ nb[v][j] = v ^ dg[j]; mult[v][j] = ml[j]; } else { nb[v][j] = v; mult[v][j] = 0; } }
  /* for padding entries nb = v itself with mult 0: treat as absent */
  DEG = deg;
  for (int v = 0; v < n; v++) for (int j = deg; j < 9; j++) nb[v][j] = -1;
  /* rewrite loops over nb to skip -1 */
  memset(inF, 0, sizeof inF);
  int size = 0, best = 0; static int bestF[4096];
  components();
  int nbuf[9], cbuf[9], rem[9];
  for (long it = 0; it < iters; it++){
    double T = T0 * pow(T1 / T0, (double)it / iters);
    int v = rnd() % n; if (inF[v]) continue;
    int cnt = 0, bad = 0;
    for (int j = 0; j < deg; j++){ int w = nb[v][j]; if (inF[w]){ if (mult[v][j] > 1) { rem[bad++] = w; } else { nbuf[cnt] = w; cbuf[cnt] = comp[w]; cnt++; } } }
    /* group by component: keep one random per component */
    int nrem = bad;
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
  memcpy(inF, bestF, sizeof inF);
  /* fix nb -1 for check */
  for (int v = 0; v < n; v++) for (int j = deg; j < 9; j++){ nb[v][j] = v; }
  int ok = check();
  FILE *fo = fopen(argv[15], "w");
  for (int v = 0; v < n; v++) if (inF[v]) fprintf(fo, "%d\n", v);
  fclose(fo);
  printf("best=%d check=%d\n", best, ok);
  return 0;
}
