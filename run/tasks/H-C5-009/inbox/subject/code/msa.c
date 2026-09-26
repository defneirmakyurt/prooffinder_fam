/* msa.c -- simulated annealing over sets M of even-weight vertices of Q_d (the even part of an induced forest).
   Representation (no loss of generality for forests, see runlog): F = M u (O \ Z), S = (E \ M) u Z, where
   O/E = odd/even weight vertices and Z = removed odd vertices. Only odd vertices with >= 2 M-neighbours
   ("hyperedges" h = N(o) n M) can lie on a cycle of Q_d[F]. Given M, Z is chosen greedily: hyperedges are
   processed by increasing size and kept iff their M-vertices lie in pairwise distinct components (union-find)
   of what is kept so far; the rest form Z. Then Q_d[F] is a forest (checked independently later).
   Score (estimate of the uphill-path count of the labelling "F first (BFS per tree), then Z, then E\M"):
      P_est = 2^d + (d-1)|S| + sum_{z in Z} (j_z - 2)(d - j_z),  j_z = |N(z) n M|,
   |S| = 2^{d-1} - |M| + |Z|. The true count is obtained later with build_labelling.py + checker.
   Moves: add a random even vertex; remove a random member; move a member to a random even vertex at
   distance 2. Metropolis on P_est.
   Usage: msa d seed iters T0 T1 outfile [XW]  (XW = weight of the extra term, default 1; 0 = pure size) */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
static int d, n; static long long XW=1;
static unsigned long long rs;
static inline unsigned long long rnd(void){ rs^=rs<<13; rs^=rs>>7; rs^=rs<<17; return rs; }
static inline double urand(void){ return (rnd()>>11)*(1.0/9007199254740992.0); }
static int par[1<<12];
static int fp(int x){ while(par[x]!=x){ par[x]=par[par[x]]; x=par[x]; } return x; }
static int evens[1<<11], ne;
static int inM[1<<12], cnt[1<<12];
static int Mlist[1<<11], mcount;
static int lastZ[1<<12], lastnZ;

static long long evaluate(int *nZout){
  /* hyperedges */
  static int hyp[1<<12], nh; nh=0;
  static int touched[1<<12]; int nt=0;
  for(int i=0;i<mcount;i++){ int m=Mlist[i]; for(int j=0;j<d;j++){ int o=m^(1<<j); if(cnt[o]==0) touched[nt++]=o; cnt[o]++; } }
  /* bucket by size */
  static int bysz[16][1<<11]; int nb[16]; memset(nb,0,sizeof nb);
  for(int i=0;i<nt;i++){ int o=touched[i]; if(cnt[o]>=2) bysz[cnt[o]][nb[cnt[o]]++]=o; }
  for(int i=0;i<mcount;i++) par[Mlist[i]]=Mlist[i];
  long long extra=0; int nZ=0;
  for(int s=2;s<=d;s++){
    /* shuffle within size class for diversity */
    for(int i=nb[s]-1;i>0;i--){ int k=rnd()%(i+1); int t=bysz[s][i]; bysz[s][i]=bysz[s][k]; bysz[s][k]=t; }
    for(int i=0;i<nb[s];i++){ int o=bysz[s][i]; int r[16],k=0,ok=1;
      for(int j=0;j<d;j++){ int m=o^(1<<j); if(inM[m]){ int x=fp(m); for(int t=0;t<k;t++) if(r[t]==x){ok=0;break;} if(!ok) break; r[k++]=x; } }
      if(ok){ for(int t=1;t<k;t++) par[fp(r[t])]=fp(r[0]); }
      else { lastZ[nZ++]=o; extra += XW*(long long)(s-2)*(d-s); }
    }
  }
  for(int i=0;i<nt;i++) cnt[touched[i]]=0;
  lastnZ=nZ; *nZout=nZ;
  int S = (n/2) - mcount + nZ;
  return (long long)n + (long long)(d-1)*S + extra;
}
static void addM(int v){ inM[v]=1; Mlist[mcount++]=v; }
static void remM(int idx){ int v=Mlist[idx]; inM[v]=0; Mlist[idx]=Mlist[--mcount]; }
int main(int argc,char**argv){
  if(argc<7){ fprintf(stderr,"usage\n"); return 1; }
  d=atoi(argv[1]); n=1<<d; rs=0x9E3779B97F4A7C15ULL^((unsigned long long)atoll(argv[2])*0x2545F4914F6CDD1DULL); if(!rs) rs=1;
  long long iters=atoll(argv[3]); double T0=atof(argv[4]),T1=atof(argv[5]); if(argc>7) XW=atoll(argv[7]);
  ne=0; for(int v=0;v<n;v++) if(!(__builtin_popcount(v)&1)) evens[ne++]=v;
  memset(inM,0,sizeof inM); memset(cnt,0,sizeof cnt); mcount=0;
  int nZ; long long cur=evaluate(&nZ), best=cur; static int bestM[1<<11]; int bestm=0, bestZ=0;
  for(long long it=0; it<iters; it++){
    double T=T0*pow(T1/T0,(double)it/iters);
    int mv=rnd()%3; int a=-1,b=-1,idx=-1;
    if(mv==0 || mcount==0){ a=evens[rnd()%ne]; if(inM[a]) continue; addM(a); mv=0; }
    else if(mv==1){ idx=rnd()%mcount; b=Mlist[idx]; remM(idx); }
    else { idx=rnd()%mcount; b=Mlist[idx]; int i=rnd()%d, j=rnd()%(d-1); if(j>=i) j++; a=b^(1<<i)^(1<<j); if(inM[a]) continue; remM(idx); addM(a); }
    long long nv=evaluate(&nZ);
    long long delta=nv-cur;
    if(delta<=0 || urand()<exp(-(double)delta/T)){
      cur=nv;
      if(cur<best){ best=cur; bestm=mcount; memcpy(bestM,Mlist,sizeof(int)*mcount); bestZ=nZ;
        fprintf(stderr,"it %lld best P_est=%lld |M|=%d |Z|=%d |S|=%d\n",it,best,mcount,nZ,n/2-mcount+nZ); }
    } else {
      /* undo */
      if(mv==0){ remM(mcount-1); }
      else if(mv==1){ addM(b); }
      else { remM(mcount-1); addM(b); }
    }
  }
  /* rebuild best, write forest indicator with deterministic greedy Z */
  memset(inM,0,sizeof inM); mcount=0; for(int i=0;i<bestm;i++) addM(bestM[i]);
  long long v=evaluate(&nZ);
  static char F[1<<12]; for(int x=0;x<n;x++) F[x]=(__builtin_popcount(x)&1)?1:0;
  for(int i=0;i<bestm;i++) F[bestM[i]]=1; for(int i=0;i<lastnZ;i++) F[lastZ[i]]=0;
  FILE*fo=fopen(argv[6],"w"); for(int x=0;x<n;x++) fputc('0'+F[x],fo); fputc('\n',fo); fclose(fo);
  printf("d=%d best P_est=%lld (re-eval %lld) |M|=%d |Z|=%d |S|=%d\n",d,best,v,bestm,nZ,n/2-bestm+nZ);
  return 0;
}
