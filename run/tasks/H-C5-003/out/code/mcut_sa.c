/* mcut_sa.c -- simulated annealing for a large induced forest F of Q_d
   (equivalently a small decycling set S = V \ F), H-C5-003.

   Move ("multiway-cut repair"): pick a random v not in F. Group v's F-neighbours by the tree
   (component of F) they lie in. For every tree containing >= 2 of them, compute a MINIMUM set of
   tree vertices whose deletion leaves each of those neighbours in a different piece (vertex
   multiway cut in a tree, greedy bottom-up on the Steiner subtree: delete the deepest vertex
   where two live terminals meet; optimal on trees). Adding v and deleting the union of the cuts
   keeps F a forest. delta = 1 - |cuts|. With probability pnb the predecessor's move is used
   instead (keep one random neighbour per tree, evict the others). Metropolis acceptance.
   Every accepted move recomputes the BFS forest (parents, depths) from scratch.
   The final best F is re-checked to be a forest (edges == vertices - components).

   Usage: mcut_sa d seed iters T0 T1 pnb outfile [initfile]
     initfile: one line of 2^d chars '0'/'1' (1 = in F), must be a forest.
   Output: one line of 2^d chars (1 = in F) to outfile; prints best |F|, |S|. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define MAXN 4096
static int d, n;
static unsigned long long rs;
static inline unsigned long long rnd(void){ rs ^= rs<<13; rs ^= rs>>7; rs ^= rs<<17; return rs; }
static inline double urand(void){ return (rnd()>>11)*(1.0/9007199254740992.0); }

static char inF[MAXN];
static int comp[MAXN], par[MAXN], dep[MAXN], q[MAXN];

static void rebuild(void){
  for(int v=0;v<n;v++) comp[v]=-1;
  int c=0;
  for(int r=0;r<n;r++) if(inF[r] && comp[r]<0){
    int h=0,t=0; q[t++]=r; comp[r]=c; par[r]=-1; dep[r]=0;
    while(h<t){ int v=q[h++];
      for(int j=0;j<d;j++){ int w=v^(1<<j);
        if(inF[w] && comp[w]<0){ comp[w]=c; par[w]=v; dep[w]=dep[v]+1; q[t++]=w; } } }
    c++;
  }
}

static int is_forest(const char *F){
  int V=0,E=0;
  static int cc[MAXN];
  for(int v=0;v<n;v++) cc[v]=-1;
  int c=0;
  for(int r=0;r<n;r++) if(F[r] && cc[r]<0){ int h=0,t=0; q[t++]=r; cc[r]=c;
    while(h<t){ int v=q[h++]; for(int j=0;j<d;j++){ int w=v^(1<<j); if(F[w]&&cc[w]<0){cc[w]=c;q[t++]=w;} } } c++; }
  for(int v=0;v<n;v++) if(F[v]){ V++; for(int j=0;j<d;j++){ int w=v^(1<<j); if(w>v&&F[w]) E++; } }
  return E==V-c;
}

/* scratch for cut computation */
static int mark[MAXN], stamp=1, live[MAXN], isterm[MAXN], inU[MAXN];
static int Ubuf[MAXN];

/* terminals t[0..k-1] all in the same tree; append min multiway cut to cut[], return its size */
static int tree_cut(const int *t, int k, int *cut){
  /* LCA of all terminals */
  int a=t[0];
  for(int i=1;i<k;i++){ int b=t[i];
    while(dep[a]>dep[b]) a=par[a];
    while(dep[b]>dep[a]) b=par[b];
    while(a!=b){ a=par[a]; b=par[b]; } }
  int lca=a;
  stamp++;
  int m=0;
  for(int i=0;i<k;i++){ int x=t[i];
    while(1){ if(inU[x]!=stamp){ inU[x]=stamp; live[x]=0; isterm[x]=0; Ubuf[m++]=x; }
      if(x==lca) break; x=par[x]; } }
  for(int i=0;i<k;i++) isterm[t[i]]=1;
  /* sort Ubuf by depth descending (m small; insertion sort) */
  for(int i=1;i<m;i++){ int x=Ubuf[i],j=i-1; while(j>=0 && dep[Ubuf[j]]<dep[x]){ Ubuf[j+1]=Ubuf[j]; j--; } Ubuf[j+1]=x; }
  int nc=0;
  for(int i=0;i<m;i++){ int x=Ubuf[i];
    int L=live[x]+isterm[x];
    if(L>=2){ cut[nc++]=x; L=0; }
    if(x!=lca) live[par[x]]+=L; }
  return nc;
}

int main(int argc,char**argv){
  if(argc<8){ fprintf(stderr,"usage\n"); return 1; }
  d=atoi(argv[1]); n=1<<d;
  rs=0x9E3779B97F4A7C15ULL^((unsigned long long)atoll(argv[2])*0x2545F4914F6CDD1DULL); if(!rs) rs=1;
  long long iters=atoll(argv[3]); double T0=atof(argv[4]),T1=atof(argv[5]); double pnb=atof(argv[6]);
  static char best[MAXN];
  memset(inF,0,sizeof inF);
  int size=0;
  if(argc>=9){ FILE*fi=fopen(argv[8],"r"); if(!fi){fprintf(stderr,"no init\n");return 1;}
    for(int v=0;v<n;v++){ int ch=fgetc(fi); inF[v]=(ch=='1'); size+=inF[v]; } fclose(fi);
    if(!is_forest(inF)){ fprintf(stderr,"init not forest\n"); return 1; } }
  rebuild();
  int bestsz=size; memcpy(best,inF,n);
  long long acc=0;
  for(long long it=0;it<iters;it++){
    double T=T0*pow(T1/T0,(double)it/iters);
    int v=rnd()%n; if(inF[v]) continue;
    int nb[16],m=0; for(int j=0;j<d;j++){ int w=v^(1<<j); if(inF[w]) nb[m++]=w; }
    int cut[64], nc=0;
    if(urand()<pnb){
      for(int i=m-1;i>0;i--){ int k=rnd()%(i+1); int t=nb[i]; nb[i]=nb[k]; nb[k]=t; }
      int seen[16],ns=0;
      for(int i=0;i<m;i++){ int c=comp[nb[i]],dup=0; for(int k=0;k<ns;k++) if(seen[k]==c){dup=1;break;}
        if(dup) cut[nc++]=nb[i]; else seen[ns++]=c; }
    } else {
      /* group by component */
      int used[16]={0};
      for(int i=0;i<m;i++) if(!used[i]){ int grp[16],g=0; grp[g++]=nb[i]; used[i]=1;
        for(int k=i+1;k<m;k++) if(!used[k] && comp[nb[k]]==comp[nb[i]]){ grp[g++]=nb[k]; used[k]=1; }
        if(g>=2) nc+=tree_cut(grp,g,cut+nc); }
    }
    int delta=1-nc;
    if(delta>=0 || urand()<exp(delta/T)){
      for(int i=0;i<nc;i++) inF[cut[i]]=0; inF[v]=1; size+=delta; acc++;
      rebuild();
      if(size>bestsz){ bestsz=size; memcpy(best,inF,n); }
    }
  }
  if(!is_forest(best)){ printf("ERROR best not forest\n"); return 1; }
  FILE*fo=fopen(argv[7],"w"); for(int v=0;v<n;v++) fputc('0'+best[v],fo); fputc('\n',fo); fclose(fo);
  printf("d=%d seed=%s iters=%lld T0=%g T1=%g pnb=%g accepted=%lld best |F|=%d |S|=%d\n",
         d,argv[2],iters,T0,T1,pnb,acc,bestsz,n-bestsz);
  return 0;
}
