# Target pin: B-C3-001 (Space, Phase 2S)

Objects: partitions lambda of n (weakly decreasing positive parts, s parts); B(lambda) = positive (lambda_i - 1) plus part s.
cyclic: B^i(lambda)=lambda for some i>=1. d_B(lambda)=min{i>=0: B^i(lambda) cyclic}; D_B(n)=max over lambda |- n.
T_k=k(k+1)/2; rank k: T_{k-1} < n <= T_k.

(a) UNIVERSAL: for all k>=4, all n with T_{k-1}<n<T_k, all lambda |- n: d_B(lambda) <= k^2-2k-1.
(b) EXTREMAL VALUE: F(k)=D_B(T_k-1); needs upper bound over all lambda |- T_k-1 AND explicit attaining lambda(k), for a stated
    k-range; small k given separately. (Note: (a) at n=T_k-1 already gives the upper bound for k>=4.)
(c) CLASSIFICATION: the exact set E_k = {lambda |- T_k-1 : d_B(lambda)=D_B(T_k-1)}, explicit in k, with proof of both inclusions.
Hand-in: written LaTeX proof; computation only as exhaustive check over a finite set the argument reduces to (<10 min).

Readings chosen: k-range for (b),(c) is "as many k>=1 as possible"; k=1 gives T_1-1=0 which is not a valid n (n>=1), so (b) covers k>=2.
Quantifier order in (a): k first, then n, then lambda; the bound is uniform in n within the rank block.
Goal type: (a) universal/bound; (b) extremal value (bound + construction); (c) classification.
