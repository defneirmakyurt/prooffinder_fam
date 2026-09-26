/* sa_forest.c -- exploratory heuristic (NOT part of any proof).
   Simulated annealing for large induced forests of Q_9: maximise |F| - lam*cyc(F),
   cyc = e(F) - |F| + c(F) (cyclomatic number), lam > 1 so optima are forests.
   Usage: sa_forest seed iters T0 T1 lam outfile
   Writes the best forest found (a line of 512 0/1 chars, char v = 1 iff v in F). */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdint.h>
#define D 9
#define N 512
static int in[N], par[N];
static uint64_t rs;
static inline uint64_t rnd(void){ rs ^= rs<<13; rs ^= rs>>7; rs ^= rs<<17; return rs; }
static double urand(void){ return (rnd()>>11)*(1.0/9007199254740992.0); }
static int fnd(int x){ while(par[x]!=x){ par[x]=par[par[x]]; x=par[x]; } return x; }
static int cyc(void){ /* cyclomatic number of Q[F] */
  int c=0; for(int v=0;v<N;v++) par[v]=v;
  for(int v=0;v<N;v++) if(in[v]) for(int i=0;i<D;i++){ int w=v^(1<<i); if(w>v && in[w]){
      int a=fnd(v), b=fnd(w); if(a==b) c++; else par[a]=b; } }
  return c; }
int main(int argc,char**argv){
  if(argc<7){fprintf(stderr,"usage\n");return 1;}
  rs = 88172645463325252ULL ^ (uint64_t)atoll(argv[1])*2654435761ULL; for(int i=0;i<20;i++) rnd();
  long iters=atol(argv[2]); double T0=atof(argv[3]), T1=atof(argv[4]), lam=atof(argv[5]);
  for(int v=0;v<N;v++) in[v]=(rnd()%2);
  int size=0; for(int v=0;v<N;v++) size+=in[v];
  int cy=cyc(); double obj=size-lam*cy; int best=0;
  for(long it=0; it<iters; it++){
    double T = T0*pow(T1/T0,(double)it/iters);
    int v=rnd()%N; in[v]^=1; int ns=size+(in[v]?1:-1); int nc=cyc(); double no=ns-lam*nc;
    if(no>=obj || urand()<exp((no-obj)/T)){ size=ns; cy=nc; obj=no;
      if(cy==0 && size>best){ best=size; FILE*f=fopen(argv[6],"w"); for(int u=0;u<N;u++) fputc('0'+in[u],f); fputc('\n',f); fclose(f);} }
    else in[v]^=1;
  }
  printf("seed %s best %d\n",argv[1],best); return 0; }
