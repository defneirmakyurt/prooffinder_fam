/* mif_sa.c -- simulated annealing for a large induced forest F of Q_d
   (equivalently a small decycling set S = V \ F).
   Move: pick random v not in F; for each component of F meeting N(v) keep one random
   neighbour, evict the others; delta = 1 - #evicted; Metropolis acceptance.
   Prints best |F| and |S|, writes best F as a 0/1 indicator line to outfile.
   Usage: mif_sa d seed iters T0 T1 outfile */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
static int d,n; static unsigned long long rs;
static inline unsigned long long rnd(void){ rs^=rs<<13; rs^=rs>>7; rs^=rs<<17; return rs; }
static inline double urand(void){ return (rnd()>>11)*(1.0/9007199254740992.0); }
static int comp[1<<12], q[1<<12];
static void components(const char *inF){
  for(int v=0;v<n;v++) comp[v]=-1;
  int c=0;
  for(int r=0;r<n;r++) if(inF[r] && comp[r]<0){ int h=0,t=0; q[t++]=r; comp[r]=c;
    while(h<t){ int v=q[h++]; for(int j=0;j<d;j++){ int w=v^(1<<j); if(inF[w]&&comp[w]<0){ comp[w]=c; q[t++]=w; } } } c++; }
}
static int is_forest(const char *inF){ int V=0,E=0; for(int v=0;v<n;v++) if(inF[v]){ V++; for(int j=0;j<d;j++){ int w=v^(1<<j); if(w>v&&inF[w]) E++; } }
  components(inF); int c=0; for(int v=0;v<n;v++) if(inF[v]&&comp[v]+1>c) c=comp[v]+1; return E==V-c; }
int main(int argc,char**argv){
  d=atoi(argv[1]); n=1<<d; rs=0x9E3779B97F4A7C15ULL^((unsigned long long)atoll(argv[2])*0x2545F4914F6CDD1DULL); if(!rs) rs=1;
  long long iters=atoll(argv[3]); double T0=atof(argv[4]),T1=atof(argv[5]);
  static char inF[1<<12], best[1<<12];
  memset(inF,0,n); int size=0, bestsz=0;
  components(inF);
  for(long long it=0;it<iters;it++){
    double T=T0*pow(T1/T0,(double)it/iters);
    int v=rnd()%n; if(inF[v]) continue;
    int nb[16],m=0; for(int j=0;j<d;j++){ int w=v^(1<<j); if(inF[w]) nb[m++]=w; }
    /* shuffle */
    for(int i=m-1;i>0;i--){ int k=rnd()%(i+1); int t=nb[i]; nb[i]=nb[k]; nb[k]=t; }
    int ev[16],ne=0, seen[16], ns=0;
    for(int i=0;i<m;i++){ int c=comp[nb[i]], dup=0; for(int k=0;k<ns;k++) if(seen[k]==c){dup=1;break;}
      if(dup) ev[ne++]=nb[i]; else seen[ns++]=c; }
    int delta=1-ne;
    if(delta>=0 || urand()<exp(delta/T)){
      for(int i=0;i<ne;i++) inF[ev[i]]=0; inF[v]=1; size+=delta; components(inF);
      if(size>bestsz){ bestsz=size; memcpy(best,inF,n); }
    }
  }
  if(!is_forest(best)){ printf("ERROR best not forest\n"); return 1; }
  FILE*fo=fopen(argv[6],"w"); for(int v=0;v<n;v++) fputc('0'+best[v],fo); fputc('\n',fo); fclose(fo);
  printf("d=%d best |F|=%d |S|=%d\n",d,bestsz,n-bestsz);
  return 0;
}
