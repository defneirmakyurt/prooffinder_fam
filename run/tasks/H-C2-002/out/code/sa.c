/* Simulated annealing for few uphill paths on Q_d.
   Usage: sa d seed iters T0 T1 outfile
   State: order[i] = vertex with label i+1. Moves: swap two positions, or move one
   vertex to another position (insertion). Score computed exactly by the recurrence
   N(v) = [valley] + sum_{w~v, f(w)<f(v)} N(w) using unsigned 64-bit with saturation
   (saturation only matters for terrible labellings; final score re-checked by verify.py). */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
typedef unsigned long long u64;
static int d, n;
static int ord[1024], f[1024];
static u64 N[1024];
static u64 rng_s;
static u64 rnd(void){ rng_s ^= rng_s<<13; rng_s ^= rng_s>>7; rng_s ^= rng_s<<17; return rng_s; }
static const u64 CAP = (u64)1<<60;
static u64 score(void){
  for(int i=0;i<n;i++) f[ord[i]]=i;
  u64 tot=0;
  for(int i=0;i<n;i++){ int v=ord[i]; u64 s=0; int val=1;
    for(int j=0;j<d;j++){ int w=v^(1<<j); if(f[w]<i){ val=0; s+=N[w]; if(s>CAP) s=CAP; } }
    N[v]=s+val; tot+=N[v]; if(tot>CAP) tot=CAP; }
  return tot;
}
int main(int argc,char**argv){
  d=atoi(argv[1]); n=1<<d; rng_s=strtoull(argv[2],0,10)*2654435761ULL+12345; 
  long iters=atol(argv[3]); double T0=atof(argv[4]), T1=atof(argv[5]);
  for(int i=0;i<n;i++) ord[i]=i;
  for(int i=n-1;i>0;i--){ int j=rnd()%(i+1); int t=ord[i]; ord[i]=ord[j]; ord[j]=t; }
  u64 cur=score(), best=cur; int bestord[1024]; memcpy(bestord,ord,sizeof(int)*n);
  int tmp[1024];
  for(long it=0; it<iters; it++){
    double T = T0*pow(T1/T0,(double)it/iters);
    memcpy(tmp,ord,sizeof(int)*n);
    int a=rnd()%n, b=rnd()%n; if(a==b) continue;
    if(rnd()&1){ int t=ord[a]; ord[a]=ord[b]; ord[b]=t; }
    else { int v=ord[a]; if(a<b){ memmove(ord+a,ord+a+1,sizeof(int)*(b-a)); } else { memmove(ord+b+1,ord+b,sizeof(int)*(a-b)); } ord[b]=v; }
    u64 s=score();
    if(s<=cur || exp(-((double)s-(double)cur)/T) > (rnd()%1000000)/1e6){ cur=s; if(s<best){best=s; memcpy(bestord,ord,sizeof(int)*n);} }
    else memcpy(ord,tmp,sizeof(int)*n);
  }
  FILE*fo=fopen(argv[6],"w");
  for(int i=0;i<n;i++){ for(int j=d-1;j>=0;j--) fputc('0'+((bestord[i]>>j)&1),fo); fputc('\n',fo);} fclose(fo);
  printf("d=%d seed=%s best=%llu\n",d,argv[2],best);
  return 0;
}
