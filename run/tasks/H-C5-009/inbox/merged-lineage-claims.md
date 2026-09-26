# Claims: H-C5-003 (UPPER route of H-C5; target NOT reached)

Headline: no labelling of Q_9 with <= 2399 uphill paths was found. Best checker score 2400 (matches the
organisers' upper bound, earns nothing). The target claim "U(Q_9) <= 2399" is SEARCH-FOUND-NOTHING.

| # | claim | status | where shown |
|---|---|---|---|
| C1 | out/Q9.txt (= out/best.txt) is a labelling of Q_9 with 2400 uphill paths | CHECKED (provided checker: VERIFIED 2400) | runlog.md "Labellings" |
| C2 | out/Q9_alt.txt is a different labelling with 2400; both differ from the subject's Q9.txt, and their deleted set is 235 odd + 1 even word, not the parity construction | CHECKED (checker VERIFIED 2400; sha256 differ; check_forest.py stats) | runlog.md |
| C3 | The multiway-cut annealer finds induced forests with \|S\| = 14, 28, 56, 112 for d = 5..8 and 236 for d = 9, never \|S\| <= 235 (7 runs at d = 9, 2e7..4e8 moves) | CHECKED as run output. For d = 9 <= 235 this is SEARCH-FOUND-NOTHING: heuristic, NOT exhaustive, no lower bound | runlog.md, tmp/run_*.log |
| C4 | Cluster reduction (below): for every induced forest F of Q_9, \|S\| = 256 - (\|M\| - \|Z\|) <= 256 - sum_K net(K) over the <= 20 clusters K of M; so \|S\| <= 235 requires a cluster with net(K) >= 2 | PROVED (argument below), GIVEN the cited classical value A(9,4) = 20 (step 5 only; not re-proved) | this file |
| C5 | Every cluster with at most 6 words has net(K) <= 1 | CHECKED: exhaustive over all G2-connected sets of <= 6 even words of Q_9, up to translation by an even word and coordinate permutation (soundness below) | code/clusters.py, runlog.md (32.2 s) |
| C6 | The 8 even words of a Q_4 subcube form a cluster with net 2 (delta = 6) | CHECKED (clusters.delta) | runlog.md |
| C7 | With that Q_4 cluster, the other clusters fit in the 128 even words whose outer 5 coordinates have weight >= 3 (outer distance >= 3 is needed for distance >= 4 to all 8 cluster words). The largest distance-4 code there has 16 words, so Q_4 cluster + singletons gives |M| - |Z| <= 18 | ">= 16" CHECKED (SAT model); "<= 16" is only a solver UNSAT verdict (no DRAT), GAP | runlog.md |
| C8 | If every deleted witness of a cluster K has exactly 2 neighbours in K, then net(K) <= 1 | PROVED (stuck.md, bullet 3: each distance-2 pair needs its own deleted witness, so \|Z_K\| >= \|E_2(K)\| >= \|K\| - 1) | stuck.md |
| C10 | Inside one Q_5 subcube, the G2-connected sets of <= 8 even words with net >= 2 are exactly the 8 even words of a Q_4 subcube (5 sets containing 0, all with support of size 4); net >= 2 sets also exist with 9, 10, 14, 15, 16 words (types not analysed) | CHECKED: exhaustive over all subsets containing 0 of the 16 even words of the subcube (WLOG argument in the code docstring: coordinate permutations and even translations are parity-preserving automorphisms) | code/clusters_q5.py, runlog.md |
| C11 | The symmetric penalty annealer (forests invariant under a coordinate permutation of order 3 or 2) reaches \|S\| = 237 and 236 | CHECKED run output; heuristic, restricted class, not exhaustive | runlog.md |
| C9 | U(Q_9) <= 2399, or even nabla(Q_9) <= 235 | SEARCH-FOUND-NOTHING (classes: multiway-cut SA runs of C3; clusters of <= 6 words; one Q_4 cluster + code) | runlog.md |

## C4: the cluster reduction, written out
Let F be an induced forest of Q_9 and S = V \ F. Let E and O be the even- and odd-weight words, M = F n E
and Z = S n O.
1. |S| = |S n E| + |S n O| = (256 - |M|) + |Z|.
2. Let G2 be the graph on M joining two words at Hamming distance exactly 2. A cluster is a connected
   component of G2. Two words of M in different clusters are not at distance 2 (else they would be joined
   in G2). They are distinct and both even, so their distance is even and nonzero, hence >= 4.
3. Call an odd vertex o with >= 2 neighbours in M a witness. Two M-neighbours m, m' of o satisfy
   d(m, m') <= d(m, o) + d(o, m') = 2, and d = 2 because they are distinct and of equal parity. So all
   M-neighbours of a witness lie in one cluster K, and o is a witness of K and of no other cluster.
4. G[F] is bipartite with sides M and O \ Z. Take a cycle C in G[F]. It alternates between words of M and
   odd vertices. Each odd vertex of C has two M-neighbours on C, so it is a witness, and by step 3 its two
   cycle neighbours are in one cluster. Walking around C, all M-words of C lie in one cluster K, and all
   odd vertices of C are witnesses of K not in Z. So C is a cycle of the incidence graph I_K between K and
   the witnesses of K outside Z. Conversely, I_K is a subgraph of G[F] (incidence = adjacency). Hence G[F]
   is a forest iff every I_K is a forest. Let delta(K) be the minimum number of witnesses of K whose
   deletion makes I_K a forest. Then |Z n W_K| >= delta(K), where W_K is the witness set of K. The W_K are
   pairwise disjoint (step 3), so |Z| >= sum_K delta(K). With step 1:
   |S| >= 256 - sum_K (|K| - delta(K)) = 256 - sum_K net(K).
5. Take one word from each cluster. By step 2 these are even words pairwise at distance >= 4. So the number
   of clusters is at most the largest size of a binary code of length 9 and minimum distance 4, which is
   A(9,4) = 20 (classical value from the standard code tables; cited, not re-proved here).
6. So if |S| <= 235 then sum_K net(K) >= 21 over at most 20 clusters, and some cluster has net(K) >= 2.
   (The same holds with E and O exchanged.)

## C5: soundness of the symmetry reduction in code/clusters.py
Group used: translations x -> x xor t with t in K (t is even, so the map sends E to E and O to O and puts 0
in the image of K), and coordinate permutations. Both are automorphisms of Q_9 that preserve Hamming
distance and weight parity. So they map a cluster to a cluster, its witness set to the witness set of the
image, and the incidence graph I_K to an isomorphic one. Hence delta and net are invariant.

Completeness of the growth: every G2-connected set of s+1 words has a word w whose removal leaves it
G2-connected (a leaf of a spanning tree of its G2 graph). So it equals K u {w}, with K G2-connected of size s
and w at distance 2 from some k in K. If the stored representative K0 = phi(K) for a group element phi,
then phi(K u {w}) = K0 u {phi(w)}, and phi(w) is at distance 2 from phi(k) in K0. The program generates this
extension from K0. So every class of size s+1 is generated.

Canonical key: the minimum, over t in K and over orderings of the rows K xor t \ {0}, of the
lexicographically sorted list of columns. Equivalent sets get the same key: an equivalence composes a
translation and a coordinate permutation, the minimum already ranges over all translations by members,
and sorting the columns removes the coordinate permutation. Equal keys give equivalent sets: the key lists
the rows of K xor t \ {0} with coordinates permuted, so it determines K up to translation and coordinate
permutation. So deduplicating by key drops no class.

delta(K) is computed exactly by trying all witness subsets in increasing size. The acyclicity test is
union-find on the incidence graph.
