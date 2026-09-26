# Sources and searches

## Searches (WebSearch)
1. "Bulgarian solitaire D_B(n) upper bound k^2 - 2k - 1 non-triangular n Griggs Ho conjecture" -> pointers to Griggs-Ho, Drensky survey, Eriksson-Jonsson, survey 2607.17194.
2. "\"Bulgarian solitaire\" \"k^2-2k-1\" ... improved upper bound" -> ResearchGate snippet (misattributed to Eriksson-Jonsson; traced to Griggs-Ho abstract).
3. "Eriksson Jonsson Level sizes of the Bulgarian solitaire game tree arXiv" -> FQ PDF.
4. "Griggs Ho The cycling of partitions and compositions under repeated shifts abstract" -> author preprint PDF.
5. OEIS search 6,34,175,831,3911 (|E_k|, k=5..9) -> no match.

## Sources opened
- [GH] J.R. Griggs, C.-C. Ho, The cycling of partitions and compositions under repeated shifts, Adv. Appl. Math. 21 (1998) 205-227;
  preprint https://people.math.sc.edu/griggs/cycling.pdf (opened, full text extracted). CONTAINS ARGUMENTS:
  Thm 2.1 (Brandt's cyclic characterisation via (0,1)-array, diagonal rotation + left shift) PROVED;
  Thm 3.1/3.7 D_B(T_k)=k^2-k PROVED (seq_B/diagram_B, Prop 3.2 incl. Sandwich Property, Lemmas 3.3-3.6);
  Thm 3.8 necessary array conditions for T_k extremizers PROVED; converse COMPUTER-VERIFIED k=4..7, FALSE at k=8 (9 of 1276);
  Thm 4.1 (Akin-Davis comparison: lambda <= mu entrywise => B(lambda) <= B(mu)) PROVED; Thm 4.2 D_B(n)<=k^2-k PROVED;
  Thm 4.4 (1) D_B(n)<=k^2-2k-1 for 1<=r<k, k>=4 PROVED, with k=4 taken from the computer table Fig. 1 (COMPUTER-VERIFIED);
  Thm 4.4 (2) equality for r=k-1 via explicit lambda, argument only sketched ("imitating the proof of Thm 3.1");
  Thm 4.5 lower bounds for all r PROVED (sketched); Conj 4.7 (D_B equals the Thm 4.5 lower bound) CONJECTURED, checked n<=36;
  Sec. 5 Carolina solitaire (compositions): D_C(T_k)=k^2-1, D_C(n)<=k^2-k-2 non-triangular k>=4 PROVED.
  Extremizers of T_k-1 are NOT characterised in GH (only T_k, and only necessary conditions).
- [EJ] H. Eriksson, M. Jonsson, Level sizes of the Bulgarian solitaire game tree, Fibonacci Quart. 55(3) (2017) 243-251,
  https://www.fq.math.ca/Papers1/55-3/ErikssonJonsson03112017.pdf (opened). Reversed game (delete row i, add as column; legal
  iff lambda_i >= N(lambda)-1); quasi-infinite tree; levels <= floor(k/2) counted by F_{2m} (PROVED). Triangular n only.
  States the maximal sequence length for general n is conjectured by GH.
- [HN] A.J. Harris, S. Nguyen, Bulgarian Solitaire: a new representation for depth generating functions, arXiv:2308.05321
  (abstract + TOC opened). Orbits <-> necklaces; new representation; level (depth) generating functions for necklaces P^l as
  l->infinity (PROVED two cases of Pham's conjecture). Limit regime, not max depth.
- [P] N. Pham, Combinatorics of Bulgarian Solitaire, U. Minnesota senior thesis,
  https://www-users.cse.umn.edu/~reiner/HonorsTheses/NhungPham_thesis.pdf (abstract, TOC, necklace section opened).
  Orbits <-> necklaces (Brandt); orbit sizes and distance generating functions for (BW)^k, (BWW)^k, (BBW)^k (PROVED); conjectures.
- [S26] A short survey of the game Bulgarian solitaire and related games, arXiv:2607.17194 (HTML opened). Cites Igusa 1985,
  Etienne 1991 (general-n generalisation, Thm 5.1), GH 1998; focuses on cyclic partitions; nothing on T_k-1 extremizers.
- [HJ] B. Hopkins, M.A. Jones, Shift-induced dynamical systems on partitions and compositions, Electron. J. Combin. 13 (2006) R80,
  https://www.combinatorics.org/ojs/index.php/eljc/article/view/v13i1r80 (abstract opened). Garden of Eden partitions counted
  (PROVED); nothing on max depth in the abstract.
- [F26] Floridian Solitaire, arXiv:2608.08313 (abstract opened): variant; no D_B / T_k-1 content in abstract.
- Not opened (cited only via GH/S26/EJ): Igusa, Math. Mag. 58 (1985); Etienne, JCTA 58 (1991); Akin-Davis, Amer. Math.
  Monthly 92 (1985); Brandt, PAMS 85 (1982); Bentz (1987); Hobby-Knuth; Drensky arXiv:1503.00885 (PDF not parseable by fetch).
