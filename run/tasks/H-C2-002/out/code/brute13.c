/* brute13.c -- independent cross-check of "Q_5 has no 13-vertex decycling set".
   Enumerates ALL 13-subsets D of V(Q_5) = {0..31} containing vertex 0 (Gosper's hack over the
   other 31 vertices choose 12; justified by vertex-transitivity, proof.md Step 8(ii)), and tests
   whether F = V \ D induces a forest via  #edges(F) == |F| - #components(F)  (bitmask BFS).
   Uses neither the edge-identity cut nor incremental union-find.  Also counts, as a control,
   all 14-subsets containing 0 that ARE decycling (must be > 0) when run with argument 14. */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
static uint32_t M[5];
static int edges(uint32_t F){ int e=0; for(int j=0;j<5;j++) e+=__builtin_popcount(F & (F>>(1<<j)) & M[j]); return e; }
static uint32_t nb(uint32_t X){ uint32_t r=0; for(int j=0;j<5;j++){ int s=1<<j; r |= ((X&M[j])<<s) | ((X&~M[j])>>s);} return r; }
static int comps(uint32_t F){ int c=0; while(F){ uint32_t X=F&(-F), Y; do{ Y=X; X|=nb(X)&F; }while(X!=Y); F&=~X; c++; } return c; }
int main(int argc,char**argv){
  int k = argc>1 ? atoi(argv[1]) : 13;
  for(int j=0;j<5;j++){ M[j]=0; for(int v=0;v<32;v++) if(!((v>>j)&1)) M[j]|=1u<<v; }
  /* choose k-1 of the 31 vertices 1..31: bit i of x <-> vertex i+1 */
  uint64_t x=(1ull<<(k-1))-1, lim=1ull<<31, cnt=0, found=0;
  while(x<lim){
    uint32_t D = 1u | ((uint32_t)x<<1), F=~D;
    int nF = 32-k;
    if(edges(F) < nF && edges(F) == nF - comps(F)) { found++; if(found==1){ printf("example D mask %08x\n",D);} }
    cnt++;
    uint64_t c=x&(-x), r=x+c; x=(((r^x)>>2)/c)|r;
  }
  printf("k=%d subsets checked=%llu decycling found=%llu\n",k,(unsigned long long)cnt,(unsigned long long)found);
  return 0;
}
