# Stuck: H-L1-001

Mathematical: none. The TARGET is proved for every d >= 3 in out/proof.md (Steps 1-11).

Check of the earlier Remark (inbox/earlier-proof.md, closing Remark): its extension to all d >= 3 is
**correct and complete** in substance. Points where it was only sketched, now written out in full:
1. "2^{d-1}(d-2)+1 = 0 mod (d-1) iff 2^{d-1} = 1 mod (d-1)": proof.md Step 10 gives the explicit
   identity 2^(d-1) - 1 = (d-1)(2^(d-1) - m).
2. "the multiplicative order of 2 mod p divides both n and p-1": the Remark uses (implicitly) Fermat's
   little theorem for "divides p-1" and the order-divides-exponent lemma without proof. proof.md Step 8
   avoids Fermat: it only needs order <= p-1 (pigeonhole) and order | k (division algorithm), then
   minimality of p.
3. "n is odd" and "p | 1" are made explicit (Step 8 (1), (6)).
4. Step 6 of the earlier proof needs "no isolated vertex" and was applied to Q_d for d in {3,4}; for
   general d the needed facts (d-regular, no isolated vertex, |E| = d 2^(d-1)) are proved in Step 9.
No value of d >= 3 escapes the argument; d = 2 genuinely escapes (Q_2 has equality labellings, sanity
check D), which is consistent with the TARGET's exclusion of d = 1, 2.

Non-mathematical: no reference could be opened in this run (egress blocked for every domain tried;
see sources.md). This does not affect the proof, which cites nothing.
