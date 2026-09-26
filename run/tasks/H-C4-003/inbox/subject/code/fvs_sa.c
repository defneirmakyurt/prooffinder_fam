/* fvs_sa.c -- simulated annealing for a small "feedback" set S in Q_d
 * (complement T = V \ S must induce a forest), then decode to a labelling:
 * T in rooted BFS order (each tree from its smallest vertex), then S in a greedy order,
 * then a labelling-level polish (adjacent-transposition / move local search) on the exact count.
 * Output: the labelling (2^d lines, 0/1 strings, increasing label order) to the file given.
 *
 * usage: fvs_sa d seed iters mu outfile [polish_iters=200000 [init=0: S=even, 1: S=odd, 2: random]]
 *   objective during SA: (d-1)*|S| + lambda*cyc(T) + mu*e(S), cyc = e(T)-|T|+comp(T)
 * The exact count used internally is 128-bit (checked against the stdlib checker afterwards).
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <stdint.h>

typedef unsigned __int128 u128;
static int d, n;
static uint64_t rs;
static inline uint64_t rnd(void){ rs ^= rs<<13; rs ^= rs>>7; rs ^= rs<<17; return rs; }
static inline double urand(void){ return (rnd()>>11)*(1.0/9007199254740992.0); }

static int inS[512];
static int par[512];
static int findp(int x){ while(par[x]!=x){ par[x]=par[par[x]]; x=par[x]; } return x; }

/* returns cyc(T), sets *eS */
static int eval_state(int *eS, int *sz){
  int eT=0, t=0, comp=0, es=0, s=0;
  for(int v=0; v<n; v++) par[v]=v;
  for(int v=0; v<n; v++){
    if(inS[v]){ s++; for(int j=0;j<d;j++){int w=v^(1<<j); if(w>v && inS[w]) es++;} continue; }
    t++;
    for(int j=0;j<d;j++){ int w=v^(1<<j); if(w>v && !inS[w]){ eT++; int a=findp(v), b=findp(w); if(a!=b) par[a]=b; } }
  }
  for(int v=0; v<n; v++) if(!inS[v] && findp(v)==v) comp++;
  *eS=es; *sz=s;
  return eT - t + comp;
}

static u128 count_uphill(const int *order){
  static int f[512]; static u128 N[512];
  for(int i=0;i<n;i++) f[order[i]]=i;
  u128 tot=0;
  for(int i=0;i<n;i++){ int v=order[i]; int valley=1; u128 s=0;
    for(int j=0;j<d;j++){ int w=v^(1<<j); if(f[w]<i){ valley=0; s+=N[w]; } }
    N[v]=s+(valley?1:0); tot+=N[v]; }
  return tot;
}

static void print128(FILE *fp, u128 x){ char b[64]; int k=0; if(x==0){fputc('0',fp);return;} while(x){ b[k++]='0'+(int)(x%10); x/=10; } while(k) fputc(b[--k],fp); }

/* decode S (T forest assumed) to an order */
static void decode(int *order){
  int k=0; static int seen[512], q[512];
  memset(seen,0,sizeof(seen));
  for(int r=0;r<n;r++){ if(inS[r]||seen[r]) continue;
    int h=0,tl=0; q[tl++]=r; seen[r]=1;
    while(h<tl){ int v=q[h++]; order[k++]=v;
      for(int j=0;j<d;j++){ int w=v^(1<<j); if(!inS[w] && !seen[w]){ seen[w]=1; q[tl++]=w; } } } }
  /* greedy S order: place vertex minimizing (Nnow-2)*unplacedSnbrs + Nnow */
  static long long Nn[512]; static int placed[512];
  memset(placed,0,sizeof(placed));
  int ns=0; for(int v=0;v<n;v++) if(inS[v]) ns++;
  for(int it=0; it<ns; it++){
    int best=-1; long long bsc=0;
    for(int v=0;v<n;v++){ if(!inS[v]||placed[v]) continue;
      long long N=0; int up=0;
      for(int j=0;j<d;j++){ int w=v^(1<<j); if(!inS[w]) N+=1; else if(placed[w]) N+=Nn[w]; else up++; }
      long long sc=(N-2)*up*4 + N; /* tie-break smaller N */
      sc = sc*1024 + (long long)(rnd()%1024);
      if(best<0||sc<bsc){best=v;bsc=sc;}
    }
    long long N=0; for(int j=0;j<d;j++){ int w=best^(1<<j); if(!inS[w]) N+=1; else if(placed[w]) N+=Nn[w]; }
    Nn[best]=N; placed[best]=1; order[k++]=best;
  }
}

/* polish: local search on the order, moves = move element from position i to position j */
static u128 polish(int *order, long iters){
  u128 cur=count_uphill(order); static int tmp[512];
  for(long it=0; it<iters; it++){
    int i=rnd()%n, j=rnd()%n; if(i==j) continue;
    memcpy(tmp,order,sizeof(int)*n);
    int x=tmp[i];
    if(i<j){ memmove(tmp+i,tmp+i+1,sizeof(int)*(j-i)); } else { memmove(tmp+j+1,tmp+j,sizeof(int)*(i-j)); }
    tmp[j]=x;
    u128 c=count_uphill(tmp);
    if(c<=cur){ cur=c; memcpy(order,tmp,sizeof(int)*n); }
  }
  return cur;
}

int main(int argc, char **argv){
  if(argc<6){ fprintf(stderr,"usage: fvs_sa d seed iters mu outfile [polish_iters [init]]\n"); return 1; }
  d=atoi(argv[1]); n=1<<d; rs=strtoull(argv[2],0,10)*2654435761ULL+12345; long iters=atol(argv[3]); double mu=atof(argv[4]);
  long piters = argc>6? atol(argv[6]) : 200000;
  for(int i=0;i<20;i++) rnd();
  double lambda = d; /* penalty per independent cycle */
  int init = argc>7? atoi(argv[7]) : 0; /* 0: S = even-weight vertices, 1: S = odd-weight, 2: S = random half */
  for(int v=0;v<n;v++) inS[v] = init==2 ? (int)(rnd()&1) : (__builtin_popcount(v)%2==init%2 ? 1 : 0);
  int eS, s; int cyc=eval_state(&eS,&s);
  double cost=(d-1)*s + lambda*cyc + mu*eS;
  double best=1e18; static int bestS[512];
  double T0=2.0, T1=0.05;
  for(long it=0; it<iters; it++){
    double temp = T0*pow(T1/T0,(double)it/iters);
    int v=rnd()%n; int mv=rnd()%3; int w=-1;
    if(mv==0){ inS[v]^=1; }
    else { /* swap v with a neighbour of different status */
      int j=rnd()%d; w=v^(1<<j); if(inS[w]==inS[v]){ continue; } inS[v]^=1; inS[w]^=1; }
    int eS2,s2; int cyc2=eval_state(&eS2,&s2);
    double c2=(d-1)*s2 + lambda*cyc2 + mu*eS2;
    if(c2<=cost || urand()<exp((cost-c2)/temp)){ cost=c2; cyc=cyc2; s=s2; eS=eS2;
      if(cyc==0 && c2<best){ best=c2; memcpy(bestS,inS,sizeof(inS)); } }
    else { inS[v]^=1; if(w>=0) inS[w]^=1; }
  }
  memcpy(inS,bestS,sizeof(inS));
  cyc=eval_state(&eS,&s);
  static int order[512]; decode(order);
  u128 c0=count_uphill(order);
  u128 c1=polish(order,piters);
  fprintf(stderr,"d=%d seed=%s |S|=%d e(S)=%d cyc=%d bound=2^d+(d-1)|S|=%d decoded=",d,argv[2],s,eS,cyc,n+(d-1)*s);
  print128(stderr,c0); fprintf(stderr," polished="); print128(stderr,c1); fprintf(stderr,"\n");
  FILE *fp=fopen(argv[5],"w");
  for(int i=0;i<n;i++){ for(int j=d-1;j>=0;j--) fputc((order[i]>>j)&1?'1':'0',fp); fputc('\n',fp); }
  fclose(fp);
  return 0;
}
