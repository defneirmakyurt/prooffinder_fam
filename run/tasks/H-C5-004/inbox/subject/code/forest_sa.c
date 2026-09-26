/* forest_sa.c -- simulated annealing over induced forests F of Q_d.
   Labelling built from F: each component of F in BFS order from a root (roots = valleys),
   then S = V \ F greedily (repeatedly the unplaced S-vertex with smallest current
   N = sum of N over already-placed neighbours; ties -> most unplaced S-neighbours).
   Objective = exact number of uphill paths of that labelling (same DP as verify.py:
   N(v) = [valley] + sum_{lower nbrs w} N(w); total = sum N(v)), 64-bit ints.
   Moves: flip a random vertex; S->F additions that close cycles evict F-neighbours.
   Writes the best labelling found to outfile (line i = vertex with label i).
   Usage: forest_sa d seed iters T0 T1 outfile [initfile]
   initfile (optional): a labelling file; F is initialised as {N(v)==1 vertices}. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

static int d, n;
static unsigned long long rs;
static inline unsigned long long rnd(void){ rs ^= rs<<13; rs ^= rs>>7; rs ^= rs<<17; return rs; }
static inline double urand(void){ return (rnd()>>11)*(1.0/9007199254740992.0); }

static int par[1<<12];
static int findp(int x){ while(par[x]!=x){ par[x]=par[par[x]]; x=par[x]; } return x; }

/* evaluate: inF -> order, returns total */
static long long evaluate(const char *inF, int *order){
  static int placed[1<<12], lab[1<<12], q[1<<12];
  static long long N[1<<12], cur[1<<12];
  int k=0;
  memset(placed,0,sizeof(int)*n);
  for(int r=0;r<n;r++) if(inF[r] && !placed[r]){
    int h=0,t=0; q[t++]=r; placed[r]=1;
    while(h<t){ int v=q[h++]; order[k++]=v;
      for(int j=0;j<d;j++){ int w=v^(1<<j); if(inF[w] && !placed[w]){ placed[w]=1; q[t++]=w; } } }
  }
  /* greedy S */
  int nS=0; static int Sl[1<<12];
  for(int v=0;v<n;v++) if(!inF[v]){ Sl[nS++]=v; cur[v]=0; for(int j=0;j<d;j++) if(inF[v^(1<<j)]) cur[v]+=1; }
  /* note: cur uses N=1 for F vertices (true for BFS-ordered forest) */
  int rem=nS;
  while(rem>0){
    int bi=-1; long long bN=0; int bu=-1;
    for(int i=0;i<rem;i++){ int v=Sl[i]; int un=0;
      for(int j=0;j<d;j++){ int w=v^(1<<j); if(!inF[w] && !placed[w]) un++; }
      long long c=cur[v]; if(c==0) c=1;
      if(bi<0 || c<bN || (c==bN && un>bu)){ bi=i; bN=c; bu=un; } }
    int v=Sl[bi]; Sl[bi]=Sl[--rem]; placed[v]=1; order[k++]=v;
    long long Nv=cur[v]; if(Nv==0) Nv=1; /* valley */
    for(int j=0;j<d;j++){ int w=v^(1<<j); if(!inF[w] && !placed[w]) cur[w]+=Nv; }
  }
  /* exact DP */
  for(int i=0;i<n;i++) lab[order[i]]=i;
  long long tot=0;
  for(int i=0;i<n;i++){ int v=order[i]; long long s=0; int valley=1;
    for(int j=0;j<d;j++){ int w=v^(1<<j); if(lab[w]<i){ s+=N[w]; valley=0; } }
    N[v]=s+valley; tot+=N[v]; }
  return tot;
}

static int is_forest(const char *inF){
  for(int v=0;v<n;v++) par[v]=v;
  for(int v=0;v<n;v++) if(inF[v]) for(int j=0;j<d;j++){ int w=v^(1<<j); if(w>v && inF[w]){
    int a=findp(v), b=findp(w); if(a==b) return 0; par[a]=b; } }
  return 1;
}

/* add v to F, evicting F-neighbours that would close cycles */
static void add_vertex(char *inF, int v){
  for(int tries=0; tries<64; tries++){
    inF[v]=0;
    for(int x=0;x<n;x++) par[x]=x;
    for(int x=0;x<n;x++) if(inF[x]) for(int j=0;j<d;j++){ int w=x^(1<<j); if(w>x && inF[w]){ int a=findp(x),b=findp(w); if(a!=b) par[a]=b; } }
    int nb[16], rt[16], m=0, clash=-1;
    for(int j=0;j<d;j++){ int w=v^(1<<j); if(inF[w]){ nb[m]=w; rt[m]=findp(w); m++; } }
    for(int a=0;a<m && clash<0;a++) for(int b=a+1;b<m;b++) if(rt[a]==rt[b]){ clash = (rnd()&1)? nb[a]:nb[b]; break; }
    if(clash<0){ inF[v]=1; return; }
    inF[clash]=0;
  }
  inF[v]=1; /* fallback, caller checks */
}

int main(int argc, char **argv){
  if(argc<7){ fprintf(stderr,"usage\n"); return 1; }
  d=atoi(argv[1]); n=1<<d; rs=0x9E3779B97F4A7C15ULL ^ (unsigned long long)atoll(argv[2])*0x2545F4914F6CDD1DULL; if(!rs) rs=1;
  long long iters=atoll(argv[3]); double T0=atof(argv[4]), T1=atof(argv[5]);
  static char inF[1<<12], best[1<<12], trial[1<<12];
  static int order[1<<12], border[1<<12];
  memset(inF,0,n);
  if(argc>7){ /* init from labelling: F = {v : N(v)==1} */
    FILE *fh=fopen(argv[7],"r"); char buf[64]; int i=0; static int lab[1<<12]; static long long N[1<<12];
    while(fgets(buf,sizeof buf,fh) && i<n){ int v=(int)strtol(buf,NULL,2); order[i]=v; lab[v]=i; i++; }
    fclose(fh);
    for(int i2=0;i2<n;i2++){ int v=order[i2]; long long s=0; int valley=1;
      for(int j=0;j<d;j++){ int w=v^(1<<j); if(lab[w]<i2){ s+=N[w]; valley=0; } }
      N[v]=s+valley; inF[v]=(N[v]==1); }
  } else { /* start: odd-weight vertices */
    for(int v=0;v<n;v++) inF[v]=__builtin_popcount(v)&1;
  }
  if(!is_forest(inF)){ fprintf(stderr,"init not forest\n"); return 1; }
  long long cur=evaluate(inF,order), bestv=cur; memcpy(best,inF,n); memcpy(border,order,sizeof(int)*n);
  fprintf(stderr,"init %lld\n",cur);
  for(long long it=0; it<iters; it++){
    double T = T0*pow(T1/T0,(double)it/iters);
    memcpy(trial,inF,n);
    int v=rnd()%n;
    if(trial[v]) trial[v]=0; else add_vertex(trial,v);
    if(urand()<0.3){ int u=rnd()%n; if(trial[u]) trial[u]=0; else add_vertex(trial,u); }
    if(!is_forest(trial)) continue;
    long long val=evaluate(trial,order);
    if(val<=cur || urand()<exp((cur-val)/T)){ memcpy(inF,trial,n); cur=val;
      if(val<bestv){ bestv=val; memcpy(best,trial,n); memcpy(border,order,sizeof(int)*n);
        fprintf(stderr,"it %lld best %lld |S|=%d\n",it,bestv,(int)(n-({int c=0; for(int x=0;x<n;x++) c+=best[x]; c;}))); } }
  }
  FILE *fo=fopen(argv[6],"w");
  for(int i=0;i<n;i++){ for(int b=d-1;b>=0;b--) fputc('0'+((border[i]>>b)&1),fo); fputc('\n',fo); }
  fclose(fo);
  printf("best %lld\n",bestv);
  return 0;
}
