# Plan: B-C1-002 (BLIND, Phase 1)

Notation: cells of a sequence c=(c_1..c_m) of positive integers: C(c)={(j,h):1<=j<=m,1<=h<=c_j}.
Diagonal D_d={(j,h): j,h>=1, j+h-1=d}, |D_d|=d. Weight E(c)=sum_{(j,h) in C(c)} (j+h-1).
U(lambda)=(s, lambda_1-1, ..., lambda_t-1), t=#{j: lambda_j>=2} (unsorted shift); B(lambda)=sort(U(lambda)).
R: (j,h)->(j+1,h-1) if h>=2, (1,j) if h=1 (map on N_{>=1}^2).

Ladder:
- R1 B maps partitions of n to partitions of n; every orbit reaches a cyclic partition. (deps: none) — PROVED
- R2 C(U(lambda)) = R(C(lambda)) and E(U(lambda)) = E(lambda). (deps: none) — PROVED
- R3 Sorting lemma: E(sort(c)) <= E(c), equality iff c weakly decreasing. (deps: none) — PROVED
- R4 E(B(lambda)) <= E(lambda), equality iff B(lambda)=U(lambda); on a cycle equality at every step, so C(B^t lambda)=R^t(C(lambda)). (R2,R3) — PROVED
- R5 R preserves D_d and acts on it as a cyclic rotation of order d. (def) — PROVED
- R6 Key lemma: lambda cyclic, D_d not inside C(lambda) => D_{d+1} disjoint from C(lambda). (R4,R5, CRT with gcd(d,d+1)=1) — PROVED
- R7 Structure: lambda cyclic of n=T_{k-1}+r => D_1..D_{k-1} in C(lambda) subset D_1..D_k, |C(lambda) cap D_k|=r; i.e. lambda=lambda(eps). (R6) — PROVED
- R8 Converse: B(lambda(eps)) = lambda(rho eps) (rho = cyclic shift), so each lambda(eps) is cyclic; eps->lambda(eps) injective. (def) — PROVED
- R9 (ii)(a): cyclic partitions of n = {lambda(eps): eps in {0,1}^k, |eps|=r}. (R7,R8) — PROVED
- R10 (ii)(b): number of cycles = number of rho-orbits on words = (1/k) sum_{d | gcd(k,r)} phi(d) C(k/d, r/d). (R8,R9, orbit-counting lemma proved inline) — PROVED
- R11 (i): r=k gives only delta_k cyclic; with R1 every lambda reaches delta_k. (R1,R9) — PROVED

Sanity check (not load-bearing): out/code/check_c1.py brute force n<=45 — CHECKED (see README).
