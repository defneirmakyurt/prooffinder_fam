/* sym_pen_sa.c -- H-C5-003.  Penalty simulated annealing for a large induced forest of Q_d whose vertex
   set is invariant under a coordinate permutation sigma (given as argument).  State: a set of sigma-orbits
   of vertices; F = union of chosen orbits.  Energy = -|F| + lambda * r(F), r(F) = e(F) - |F| + c(F) (cycle
   rank, 0 iff F induces a forest), recomputed exactly with union-find for each proposal.  Move: flip one
   random orbit.  Records the best F with r(F) = 0; final best re-checked.
   Usage: sym_pen_sa d seed iters T0 T1 lambda "p0 p1 ... p_{d-1}" outfile
     (sigma maps coordinate i to p_i; identity = no symmetry)            */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#define MAXN 1024
static int d,n; static unsigned long long rs;
static inline unsigned long long rnd(void){ rs^=rs<<13; rs^=rs>>7; rs^=rs<<17; return rs; }
static inline double urand(void){ return (rnd()>>11)*(1.0/9007199254740992.0); }
static int par_[MAXN];
static int fnd(int x){ while(par_[x]!=x){ par_[x]=par_[par_[x]]; x=par_[x]; } return x; }
static char inF[MAXN];
static int rank_of(int *sz){
  int V=0,E=0,c=0;
  for(int v=0;v<n;v++){ par_[v]=v; if(inF[v]) V++; }
  c=V;
  for(int v=0;v<n;v++) if(inF[v]) for(int j=0;j<d;j++){ int w=v^(1<<j); if(w>v&&inF[w]){ E++; int a=fnd(v),b=fnd(w); if(a!=b){ par_[a]=b; c--; } } }
  *sz=V; return E-V+c;
}
int main(int argc,char**argv){
  d=atoi(argv[1]); n=1<<d;
  rs=0x9E3779B97F4A7C15ULL^((unsigned long long)atoll(argv[2])*0x2545F4914F6CDD1DULL); if(!rs) rs=1;
  long long iters=atoll(argv[3]); double T0=atof(argv[4]),T1=atof(argv[5]),lam=atof(argv[6]);
  int p[16]; { char *s=argv[7]; for(int i=0;i<d;i++){ p[i]=(int)strtol(s,&s,10); } }
  /* orbits */
  static int orb[MAXN], orbstart[MAXN+1], orbv[MAXN]; int no=0, k=0;
  for(int v=0;v<n;v++) orb[v]=-1;
  for(int v=0;v<n;v++) if(orb[v]<0){ orbstart[no]=k; int x=v;
    while(orb[x]<0){ orb[x]=no; orbv[k++]=x; int y=0; for(int i=0;i<d;i++) if((x>>i)&1) y|=1<<p[i]; x=y; }
    no++; }
  orbstart[no]=k;
  memset(inF,0,sizeof inF);
  int sz; int r=rank_of(&sz); double Ecur=-sz+lam*r;
  static char best[MAXN]; int bestsz=0; memset(best,0,sizeof best);
  for(long long it=0;it<iters;it++){
    double T=T0*pow(T1/T0,(double)it/iters);
    int o=rnd()%no;
    for(int i=orbstart[o];i<orbstart[o+1];i++) inF[orbv[i]]^=1;
    int s2; int r2=rank_of(&s2); double E2=-s2+lam*r2;
    if(E2<=Ecur || urand()<exp((Ecur-E2)/T)){ Ecur=E2; if(r2==0 && s2>bestsz){ bestsz=s2; memcpy(best,inF,n); } }
    else for(int i=orbstart[o];i<orbstart[o+1];i++) inF[orbv[i]]^=1;
  }
  memcpy(inF,best,n); int s3; int r3=rank_of(&s3);
  if(r3!=0||s3!=bestsz){ printf("ERROR\n"); return 1; }
  FILE*fo=fopen(argv[8],"w"); for(int v=0;v<n;v++) fputc('0'+best[v],fo); fputc('\n',fo); fclose(fo);
  printf("d=%d seed=%s orbits=%d iters=%lld T0=%g T1=%g lambda=%g sigma=\"%s\" best |F|=%d |S|=%d\n",
         d,argv[2],no,iters,T0,T1,lam,argv[7],bestsz,n-bestsz);
  return 0;
}
