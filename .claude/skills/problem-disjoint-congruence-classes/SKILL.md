---
name: problem-disjoint-congruence-classes
description: Problem skill for "Disjoint congruence classes" (D), whether k pairwise disjoint congruence classes must have two moduli with gcd at least k. Holds the verbatim statement (official text), six cells, hand-in format with the exhaustiveness certificate, cell typing, ladders, checker spec, angle bank, pitfalls, Part S seeds and branch notes. Load when opening problem D in a Proof Pursuit run.
---

# Problem D: Disjoint congruence classes

Letter code: `D` (cell ids `D-C1` … `D-C6`). Ledger: `run/D/`. Official source: `sources/problem_description_disjoint_congruence_classes.tex`.

> **Source notes for the humans:**
> 1. **Cell 1** was missing from the first transcription ("not visible in the provided screenshots"). Its verbatim text was supplied from a screenshot on 2026-09-26 and is in §1 and in `sources/`.
> 2. The exhaustiveness certificate is introduced with "all four" in the original but lists **five** requirements (the transcriber noted this in a comment in the `.tex`). This skill keeps all five.
> 3. The statement itself contains literature claims (an asymptotic bound "is known"; the group form "is known for \(k\le5\)"). They are part of the verbatim text, so every worker sees them. They are not gated facts: nothing may use them as an ASSUMPTION unless it passes the gate or the humans say so.

## 1. Verbatim statement

If congruence classes are pairwise disjoint, must two of their moduli share a large common factor?

**Definition (Congruence class).** For integers \(a\) and \(m\ge1\), write
\[
a \pmod m=\{\,a+mt: t\in\mathbb{Z}\,\}
\]
for the *congruence class* of \(a\) modulo \(m\).

**Definition (Pairwise disjoint).** A finite family of classes
\[
a_1\pmod{m_1},\;\ldots,\;a_k\pmod{m_k}
\]
is *pairwise disjoint* if
\[
\bigl(a_i\pmod{m_i}\bigr)\cap\bigl(a_j\pmod{m_j}\bigr)=\varnothing\qquad\text{whenever } i<j.
\]
Nothing is assumed about the moduli beyond \(m_i\ge1\): they may repeat, and the residues \(a_i\) may repeat as well.

By the Chinese remainder theorem, two classes meet if and only if the congruences
\[
x\equiv a_i\pmod{m_i},\qquad x\equiv a_j\pmod{m_j}
\]
are compatible, that is,
\[
\bigl(a_i\pmod{m_i}\bigr)\cap\bigl(a_j\pmod{m_j}\bigr)\neq\varnothing
\quad\Longleftrightarrow\quad
\gcd(m_i,m_j)\mid(a_i-a_j).\tag{$*$}
\]

The question of this column is how large the moduli of a disjoint family must be forced to overlap in the gcd sense.

**Question.** Let \(k\ge2\) and let
\[
a_1\pmod{m_1},\;\ldots,\;a_k\pmod{m_k}
\]
be pairwise disjoint. Must there be a pair \(i<j\) with
\[
\gcd(m_i,m_j)\ge k?
\]

This is believed to be true for every \(k\). It is sharp: the \(k\) classes
\[
1\pmod k,\;2\pmod k,\;\ldots,\;k\pmod k
\]
are pairwise disjoint (their differences have absolute value less than \(k\), so \(k\) divides none of them) and every pairwise gcd equals exactly \(k\). So \(k\) could not be replaced by \(k+1\) in the statement.

**Example.** The three classes
\[
0\pmod 2,\qquad 1\pmod 4,\qquad 3\pmod 8
\]
are pairwise disjoint by \((*)\), and their pairwise gcds are \(2,2,4\); the largest is \(4\ge3\), as the question predicts for \(k=3\).

By contrast, \(0\pmod2\) and \(0\pmod3\) have coprime moduli and do meet, at \(0\).

**Trivial Bounds.** Two observations are immediate and you should assume they are already on the table; presenting either as progress counts for nothing.
1. If \(\gcd(m_i,m_j)=1\), then by \((*)\) the two classes meet. Hence in any pairwise disjoint family every pairwise gcd is at least \(2\). This answers the question for \(k=2\), and for a family of size \(k\) that fails the question it confines every pairwise gcd to the range
\[
2\le\gcd(m_i,m_j)\le k-1.
\]
2. The class \(a\pmod m\) has density \(1/m\), so a pairwise disjoint family satisfies
\[
\sum_{i=1}^{k}\frac1{m_i}\le1.
\]
In particular, some modulus satisfies \(m_i\ge k\).

Observation 2 bounds a single modulus from below; it says nothing about any gcd, and the two together settle no size \(k\ge3\). Every cell below needs a genuinely new argument.

### Cells

| Cell | Title | Points | Checking |
|---|---|---|---|
| C1 | Three Classes | 1 | judged (written proof) |
| C2 | Four Classes | 2 | written proof |
| C3 | Every \(k\) up to 8 | 3 | written proof |
| C4 | Every \(k\) up to 12 | 5 | written proof + per-\(k\) report for \(9\le k\le16\) |
| C5 | The Certified Boundary | 8 | written proof + certificate (i)–(v) |
| C6 | Beyond the Boundary | 13 | **open question** |

**C1: Three Classes (verbatim).** The first size that the two trivial observations above do not settle. Prove the statement for \(k=3\): any three pairwise disjoint classes have \(\gcd(m_i,m_j)\ge 3\) for some \(i<j\).

**C2: Four Classes (verbatim).** The same question for four classes. Prove the statement for \(k=4\).

**C3: Every \(k\) up to 8 (verbatim).** A first range of sizes: after C1 and C2, the sizes \(k=5,6,7\) and \(8\) remain. Prove the statement for every \(k\le8\).

**C4: Every \(k\) up to 12 (verbatim).** A longer range, and a precise account of your method at the sizes just beyond it. Prove the statement for every \(k\le12\).

Then, for each \(k\) from \(9\) to \(16\) in turn, report exactly what your method leaves undecided at that \(k\): if nothing, say so and prove it; if something, exhibit it in full.

If that disagrees with any source you consulted, say which of the two is right and why. An answer that reports agreement with a source it did not test will be marked wrong.

**C5: The Certified Boundary (verbatim).** The main certification cell: an initial range of sizes as long as you can make it, plus two isolated sizes further out.

Determine the largest \(k\) for which you can certify the statement for all sizes up to and including \(k\), and certify it. The range you claim must be contiguous, and if your argument at a given size assumes that all smaller sizes have already been settled you must say so.

Then decide the two isolated sizes \(k=24\) and \(k=30\): show that neither is the least size at which the statement can fail.

For this cell the exhaustiveness certificate of the hand-in rules is not enough on its own. Add:
- (i) **A demonstration that your method is not vacuous.** Construct a case in which an admissible configuration genuinely exists, run your machinery on it unmodified, and show it returns that configuration. A method that reports "nothing survives" at every size it is pointed at is indistinguishable from a method with a bug, and will be graded as one.
- (ii) **For every object your pruning leaves undecided, at every \(k\) you claim** (not a sample) an individual decision, plus the smallest part of that object which already forces the decision, plus a proof that no smaller part does.
- (iii) **The exact list**, not merely the count, of what survives at each \(k\).
- (iv) **Every pruning rule you use beyond those you have proved, proved.** If your search needs a rule you invented to finish a size, that rule is part of your claim: state it, prove it, and show the survivor list is unchanged when you switch it off. A size that only closes with an unproved rule is not certified.
- (v) **A second implementation, written independently of your first, that differs in method** (not the same algorithm twice) and the two survivor lists compared elementwise at every \(k\) you claim. Report any difference rather than reconciling it silently: a disagreement means one of them is wrong, and finding which is part of the cell.

**C6: Beyond the Boundary (verbatim).** **Open question.** Three directions beyond the certified range; any one of them counts. Any of the following.
- (a) Decide a size \(k\ge25\).
- (b) **The asymptotic form.** It is known that a pairwise disjoint family of size \(k\) always has a pair with
\[
\gcd(m_i,m_j)\ge k\cdot\exp\!\left(-(2+o(1))\sqrt{\frac{\log k}{\log\log k}}\right),
\]
which is \(k^{1-o(1)}\) but not linear in \(k\). Prove the statement in full, or prove the weaker bound
\[
\gcd(m_i,m_j)\ge ck
\]
for some absolute constant \(c>0\), or improve the exponential factor above.
- (c) **The group form.** Let \(G\) be a group, let \(G_1,\ldots,G_k\) be subgroups of finite index
\[
n_i=[G:G_i],
\]
and let \(x_1G_1,\ldots,x_kG_k\) be pairwise disjoint cosets. Is there a pair \(i<j\) with
\[
\gcd(n_i,n_j)\ge k?
\]
This is known for \(k\le5\) and open for every \(k\ge6\); settling \(k=6\) counts as progress.

## 2. Definitions and notation (exactly as given)

- \(a\pmod m=\{a+mt:t\in\mathbb{Z}\}\), for integers \(a\) and \(m\ge1\).
- *Pairwise disjoint:* \((a_i\bmod m_i)\cap(a_j\bmod m_j)=\varnothing\) for all \(i<j\). **Moduli may repeat; residues may repeat.** Only \(m_i\ge1\) is assumed.
- \((*)\): the classes meet iff \(\gcd(m_i,m_j)\mid(a_i-a_j)\) (stated in the problem, via the Chinese remainder theorem).
- *The statement at size \(k\)* ("the statement for \(k\)"): every pairwise disjoint family of \(k\) classes has a pair \(i<j\) with \(\gcd(m_i,m_j)\ge k\).
- *Group form* (C6(c)): cosets \(x_iG_i\) of finite-index subgroups \(G_i\le G\), \(n_i=[G:G_i]\).

## 3. Hand-in format

Official "What to Hand In" (verbatim): "For each cell you attempt, hand in a written proof.
- **Computation.** You may use a computer to explore. A proof may rely on a computation only if you include the code, it runs in under 10 minutes on a laptop, and the computation is exhaustive over a finite set that your own argument has reduced the problem to.
- **Exhaustiveness certificate.** A computational cell is accepted only with an *exhaustiveness certificate*, meaning all [five]:
  1. An exact description of the finite set your search enumerates, together with the proof that nothing outside it can be a counterexample.
  2. Every pruning rule you use, stated precisely, each with the proof that it discards only objects that cannot be completed to a counterexample.
  3. The node count of the search at each size you claim, and the wall clock.
  4. A rerun that reproduces those counts.
  5. If anything at all survives your pruning at a size you claim, a separate decision for **every** survivor (not a sample) together with, for each one, the **smallest** part of it that already forces the decision, and your proof that no smaller part does. A survivor you cannot decide means the size is not certified.

  A run that reports "I searched and found nothing" without 1–5 is not a certificate and scores nothing.
- **Unfinished searches.** If a search does not finish at some size, report it as unfinished and do not claim that size; a partial search is a legitimate partial result and should be handed in as one, with the counts it reached.
- **Boundaries.** Where a cell asks you to determine a boundary, state the exact value you claim. Claim only what you have verified: an unfinished size, or one certified under an assumption you have not verified, must be reported as such.
- **Status.** Say clearly which cells you consider solved and which are partial.
- **Citations.** Citing a published result for the statement you are asked to prove does not count as a solution; a proof written out in full does, whatever its source. If you rely on a published argument, you are responsible for it: check it yourself, and report it if it does not hold up."

("[five]": the source reads "all four" but lists five items; see the source notes.)

| Cell | Artefact files | Judges require |
|---|---|---|
| C1 | `submission.md`; code + certificate 1–5 if computational | proof for \(k=3\) |
| C2 | `submission.md`; code + certificate 1–5 if computational | proof for \(k=4\) |
| C3 | `submission.md`; code + certificate 1–5 per size if computational | proof for every \(k\le8\) |
| C4 | `submission.md`; code + certificate 1–5 per size | proof for every \(k\le12\); for each \(k=9..16\), exactly what the method leaves undecided (nothing, with proof, or the undecided objects in full); any disagreement with a consulted source resolved |
| C5 | `submission.md`; two independent implementations; survivor lists per \(k\); rerun logs | the claimed contiguous range, with any dependence on smaller sizes stated; \(k=24\) and \(k=30\) shown not to be the least failing size; certificate 1–5 plus (i)–(v) |
| C6 | `submission.md` (+ code if any) | one of (a), (b), (c) |

## 4. Cell typing and exact targets

"Prove the statement for \(k\)" (the statement at size \(k\), §2) is a universal statement over every pairwise disjoint family of \(k\) classes: every modulus \(m_i\ge1\), every residue, repetitions allowed. A computer-assisted proof needs both halves of the gate: a refereed reduction to exactly the finite set searched, and the checked, re-run search with certificate 1–5.

| Cell | Type | Tier guess + reason | Exact target |
|---|---|---|---|
| C1 | prove a stated lemma (finite \(k\)) | T0/T1: 1 pt, smallest open size | The statement at \(k=3\): every pairwise disjoint family of three classes has a pair \(i<j\) with \(\gcd(m_i,m_j)\ge3\). |
| C2 | prove a stated lemma (finite \(k\)) | T1: 2 pts, one size | The statement at \(k=4\). |
| C3 | prove a stated lemma, a range of sizes | T2: 3 pts, four new sizes | The statement at every \(k\le8\) (\(k\ge2\), since the Question fixes \(k\ge2\)). |
| C4 | prove a range + report method limits | T2: 5 pts | The statement at every \(k\le12\); plus, for each \(k\in\{9,\ldots,16\}\), the exact set of objects the method leaves undecided (empty, with proof, or listed in full). |
| C5 | lower bound / certification | T2/T3: 8 pts, heavy certificate | The largest \(K\) with the statement certified for every \(k\le K\) (contiguous); plus \(k=24\) and \(k=30\) each shown not to be the least size at which the statement fails; certificate 1–5 and (i)–(v). |
| C6 | open | T3: marked open | Any one of: (a) decide a size \(k\ge25\); (b) the statement for all \(k\), or \(\gcd\ge ck\) for an absolute \(c>0\), or an improved exponential factor; (c) the group form, e.g. \(k=6\). |

## 5. Decomposition ladders (hypotheses, not facts)

C2–C5 are the same statement over growing ranges of \(k\); C4 and C5 add increasingly strict accounts of the method. C6 leaves the finite range.

### C1 / C2 / C3
- R1 (hypothesis): a reduction that bounds the moduli or their prime structure in a hypothetical counterexample of size \(k\), using only \((*)\) and the two trivial bounds as the starting point (the trivial bounds alone count for nothing).
- R2 (hypothesis): after R1, the remaining finite set is small enough to settle by hand or by an exhaustive search with certificate 1–5.
- Feeds: the same machinery, pushed further, is C4 and C5.

### C4
- R1 (hypothesis): the C3 method extended to \(k\le12\).
- R2 (hypothesis): run unchanged at \(k=9..16\), recording every undecided object per \(k\).
- R3: the Literature agent's sources for the same sizes, compared object by object (the cell penalises reported agreement with an untested source).

### C5
- R1 (hypothesis): the largest contiguous range the method certifies within the 10-minute limit.
- R2 (hypothesis): for \(k=24\) and \(k=30\), an argument that a counterexample at that size forces one at a smaller size. How is for the workers.
- R3: the certificate items (i)–(v) as separate rungs: a non-vacuity demonstration, per-survivor decisions with minimal forcing parts, exact survivor lists, proofs of every pruning rule with an on/off comparison, and an independent second implementation of a different method.

### C6
- R1 (hypothesis): (a) the C5 machinery at one size \(k\ge25\).
- R2 (hypothesis): (b) a density or structural argument giving a linear bound.
- R3 (hypothesis): (c) the group form at \(k=6\), starting from what the integer case's arguments use.

## 6. Checker spec (families; certificate comparison)

- **Input format:** a text file; first line `k`; then \(k\) lines `a m` (integers, \(m\ge1\); \(a\) any integer).
- **Validation:** exactly \(k\) lines, integers only, \(m\ge1\), \(k\ge2\).
- **Output:** `VERIFIED <max pairwise gcd>` when the family is pairwise disjoint (exit 0), followed by `COUNTEREXAMPLE` if that maximum is \(<k\); otherwise `FAILED: classes i and j meet (gcd g divides a_i-a_j)` (exit 1).
- **Score:** the maximum over \(i<j\) of \(\gcd(m_i,m_j)\), for a pairwise disjoint family.
- **Exactness:** Python integers. Test disjointness by \((*)\) **and**, independently, by an explicit common solution: for a meeting pair, print a witness \(x\) in both classes, checked by direct division.
- **Runtime:** instant for \(k\le100\).
- **Survivor-list comparison (C4, C5 (v)):** the head fixes a canonical line format once the method's objects are known; the checker sorts two lists and compares them elementwise, printing every difference.
- **Random input generator:** random families with moduli from small smooth numbers and random residues; plus the sharp family \(1,\ldots,k\pmod k\) and the official example.
- **Hand-checkable cases:**
  - \(0\bmod2,\,1\bmod4,\,3\bmod8\): disjoint, pairwise gcds \(2,2,4\), max \(4\) (official example).
  - \(0\bmod2,\,0\bmod3\): meet at \(0\) (official example).
  - \(1,\ldots,k\pmod k\): disjoint, every pairwise gcd \(k\) (official sharpness family).

## 7. Angle bank (one per FRESH / CONTRARIAN brief)

- `gcd-graph` (angle): the complete graph on the classes, each edge labelled by \(\gcd(m_i,m_j)\); constraints from \((*)\).
- `prime-structure` (angle): which primes and prime powers divide the pairwise gcds of a hypothetical counterexample.
- `density-sharpen` (angle): strengthen observation 2 using the gcd constraints of a hypothetical counterexample.
- `lcm-model` (angle): work in \(\mathbb{Z}/L\) with \(L=\operatorname{lcm}(m_i)\); the family is a set of disjoint residue sets.
- `reduce-to-smaller` (angle): from a counterexample at size \(k\), derive one at a smaller size (relevant to C5's \(k=24,30\)).
- `exhaustive-certified` (angle): an exhaustive search with every pruning rule proved, node counts logged, survivors listed.
- `second-method` (angle): an independent search of a different kind (e.g. SAT/ILP vs. branch-and-bound) for C5 (v).
- `nonvacuity-first` (angle): build the C5 (i) demonstration before any claimed size.
- `obstruction-first` (angle): what a family with all pairwise gcds in \([2,k-1]\) must look like.

## 8. Pitfalls

- **Repetitions allowed:** moduli may repeat, and residues may repeat. A proof must not assume distinct moduli.
- **The trivial bounds count for nothing.** A cell answer resting only on observations 1 and 2 scores nothing ("presenting either as progress counts for nothing").
- **"The statement for \(k\)" is universal** over every modulus \(\ge1\), not over moduli up to some bound. A search must come with a proof that nothing outside its finite set can be a counterexample (certificate item 1).
- **Unfinished searches:** a size whose search did not finish is not claimed; it is handed in as a partial result with its counts.
- **Survivors:** every survivor at a claimed size needs its own decision with a minimal forcing part and a proof of minimality. One undecided survivor means the size is not certified.
- **C4's source clause:** reporting agreement with a source the team did not test is marked wrong.
- **C5's range is contiguous,** and any dependence on smaller sizes must be stated.
- **C5's isolated sizes:** "show that neither is the least size at which the statement can fail" is the wording; record exactly which claim is proved at \(k=24\) and \(k=30\).
- **C5 (iv):** a size that closes only with an unproved pruning rule is not certified; show the survivor list is unchanged with the rule switched off.
- **C5 (v):** the second implementation must differ in method, not only in code; report disagreements, never reconcile them silently.
- **The literature facts in the statement** (C6(b) "it is known…", C6(c) "known for \(k\le5\)") are not gated; don't use them as assumptions.
- **C1 is the first size the trivial bounds don't settle** (\(k=3\)); an answer resting only on observations 1 and 2 scores nothing there either.

## 9. Problem-specific rules

- Citing a published result for the statement you are asked to prove does not count; a proof written out in full does, whatever its source. If you rely on a published argument, check it yourself, and report it if it doesn't hold up.
- Computation: code included, < 10 minutes on a laptop, exhaustive over a finite set your own argument has reduced the problem to, with the exhaustiveness certificate (all five items).
- Boundaries: state the exact value claimed; claim only what was verified.
- Say clearly which cells are solved and which are partial.

## 10. Run notes

This skill is frozen during the run; the head doesn't edit it. New pitfalls, clarifications and problem-specific lessons go to `run/D/lessons.md`, which is copied into briefs for problem D only.

## 11. Checklist Part S seeds and branch notes

Part S seeds (from the statement only; referees and gate only):
- **S2 extremal configurations:** the sharpness family \(1,\ldots,k\pmod k\) (pairwise disjoint, every pairwise gcd exactly \(k\)) shows the bound \(k\) cannot be raised; any proof must be consistent with it (it must not prove \(\gcd\ge k+1\)).
- **S3 cases to cover:** every pairwise disjoint family of the given size: all moduli \(m_i\ge1\) (unbounded), repeated moduli, repeated residues, \(m_i=1\) included; every size in the claimed range.
- **S4 known traps (from the statement):** resting on the trivial bounds alone; an exhaustive search without a proof that nothing outside its finite set is a counterexample; an unproved pruning rule; an undecided survivor; a vacuous method (C5 (i)); a second implementation that is the same algorithm twice (C5 (v)).
- **S5 consistency:** the statement at \(k\) is required for C1 (\(k=3\)), C2 (\(k=4\)), C3 (\(k\le8\)), C4 (\(k\le12\)); a proved range must contain every smaller claimed size; C4's per-\(k\) report at \(k=9..12\) must be consistent with its own proof there (nothing undecided at a proved size).
- **S6 checkable values:** the official example (\(0\bmod2,1\bmod4,3\bmod8\): disjoint, gcds \(2,2,4\)); \(0\bmod2,0\bmod3\) meet; the sharpness family.

Branch notes (angles, each only into its own 2B lens):
- ALGEBRAIC (angle): classes as cosets of subgroups \(m\mathbb{Z}\le\mathbb{Z}\); the link to C6(c)'s group form.
- TOPOLOGICAL (angle): classes as clopen sets of the profinite integers, with density as the measure.
- ANALYSIS (angle): densities \(\sum 1/m_i\le1\) and how the gcd constraints tighten it.
- NUMBER-THEORY (angle): prime factorisations of the moduli; \((*)\) and the CRT.
- DISCRETE (angle): the gcd-labelled complete graph on the classes; exhaustive search with proved pruning.
