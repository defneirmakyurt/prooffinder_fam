/* fixsize_sa.c -- H-C5-006 (literature/analyst). Fixed-size penalty search for an induced forest of Q_d.
   State: a vertex set F with |F| = K exactly. Objective r(F) = e(F) - |F| + comp(F) (cycle rank of Q_d[F]);
   r(F) = 0 iff Q_d[F] is a forest. Move: swap u in F out, v not in F in (v uniform; u uniform in F with
   prob 1/2, else a uniform F-neighbour of v if any). Metropolis acceptance on r at temperature T
   (geometric schedule T0 -> T1). Every accepted state's r is recomputed exactly by union-find.
   Different from the earlier H-C5-002 mif_sa.c (which grows a forest and keeps it acyclic): here the size
   is fixed at the target and cycles are penalised. A found r = 0 set is written as a 0/1 indicator line
   (char v = '1' iff v in F) and must be re-checked independently (check_forest_Q9.py).
   Usage: fixsize_sa d K seed iters T0 T1 outfile [init: 0 random | 1 parity+code greedy]           */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
static int d, n; static unsigned long long rs;
static inline unsigned long long rnd(void){ rs^=rs<<13; rs^=rs>>7; rs^=rs<<17; return rs; }
static inline double urand(void){ return (rnd()>>11)*(1.0/9007199254740992.0); }
static int par[1<<12];
static int findr(int x){ while(par[x]!=x){ par[x]=par[par[x]]; x=par[x]; } return x; }
static int cyclerank(const char *inF){ /* number of edges closing a cycle = e - |F| + comp */
  int r=0; for(int v=0;v<n;v++) par[v]=v;
  for(int v=0;v<n;v++) if(inF[v]) for(int j=0;j<d;j++){ int w=v^(1<<j); if(w>v && inF[w]){ int a=findr(v),b=findr(w); if(a==b) r++; else par[a]=b; } }
  return r; }
int main(int argc,char**argv){
  if(argc<8){ fprintf(stderr,"usage\n"); return 1; }
  d=atoi(argv[1]); n=1<<d; int K=atoi(argv[2]);
  rs=0x9E3779B97F4A7C15ULL^((unsigned long long)atoll(argv[3])*0x2545F4914F6CDD1DULL); if(!rs) rs=1;
  long long iters=atoll(argv[4]); double T0=atof(argv[5]),T1=atof(argv[6]); const char *out=argv[7];
  int init = argc>8 ? atoi(argv[8]) : 0;
  static char inF[1<<12]; static int Fl[1<<12], Sl[1<<12], pos[1<<12];
  memset(inF,0,n);
  if(init==1){ /* all odd vertices + greedy random even vertices pairwise at distance >= 4, then random fill */
    for(int v=0;v<n;v++) if(__builtin_popcount(v)&1) inF[v]=1;
    for(int t=0;t<20000;t++){ int v=rnd()%n; if(__builtin_popcount(v)&1) continue; if(inF[v]) continue;
      int ok=1; for(int w=0;w<n&&ok;w++) if(inF[w] && !(__builtin_popcount(w)&1) && __builtin_popcount(v^w)<4) ok=0;
      if(ok) inF[v]=1; }
  }
  int sz=0; for(int v=0;v<n;v++) sz+=inF[v];
  while(sz<K){ int v=rnd()%n; if(!inF[v]){ inF[v]=1; sz++; } }
  while(sz>K){ int v=rnd()%n; if(inF[v]){ inF[v]=0; sz--; } }
  int nf=0, ns=0; for(int v=0;v<n;v++){ if(inF[v]){ pos[v]=nf; Fl[nf++]=v; } else { pos[v]=ns; Sl[ns++]=v; } }
  int r=cyclerank(inF), best=r;
  for(long long it=0; it<iters && r>0; it++){
    double T=T0*pow(T1/T0,(double)it/iters);
    int v=Sl[rnd()%ns]; int u;
    if(rnd()&1){ u=Fl[rnd()%nf]; }
    else { int nb[16],m=0; for(int j=0;j<d;j++){ int w=v^(1<<j); if(inF[w]) nb[m++]=w; } if(!m) continue; u=nb[rnd()%m]; }
    inF[u]=0; inF[v]=1; int r2=cyclerank(inF); int delta=r2-r;
    if(delta<=0 || urand()<exp(-delta/T)){
      r=r2; int pu=pos[u], pv=pos[v]; Fl[pu]=v; pos[v]=pu; Sl[pv]=u; pos[u]=pv;
      if(r<best){ best=r; }
    } else { inF[u]=1; inF[v]=0; }
  }
  printf("d=%d K=%d |S|=%d final_r=%d best_r=%d\n", d, K, n-K, r, best);
  if(r==0){ FILE*f=fopen(out,"w"); for(int v=0;v<n;v++) fputc(inF[v]?'1':'0',f); fputc('\n',f); fclose(f); printf("FOREST FOUND -> %s\n",out); }
  return 0; }
