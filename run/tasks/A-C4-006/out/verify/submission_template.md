# Submission: Cell 4, "Five Lines in R^3, Six in R^4" (5 points)

**Cell status: SOLVED.**
**Claim status: PROVED** (both instances, (a) and (b)).

Everything mathematical in this document comes from the team's accepted artefacts `proof.md` and `claims.md`, pinned by `MANIFEST.sha256`. All three files ship unchanged in `submission/`. The Scribe added no mathematics and did not edit the proof. Section 4 reproduces it byte for byte.

---

## 1. Statement (verbatim)

The cell as it appears in the problem description (LaTeX source, unchanged):

```latex
@@CELL@@
```

The definitions the cell relies on, from the same document (unchanged):

```latex
@@DEFS@@
```

The general requirement that applies to every cell, from the same document (unchanged):

```latex
@@GENERAL@@
```

The hand-in rules, from the same document (unchanged):

```latex
@@HANDIN@@
```

The exact target proved, as fixed for the team (unchanged):

> @@TARGET@@

---

## 2. Status

- **Cell status:** SOLVED
- **Claim status:** PROVED

Both required inequalities are proved, for every configuration of lines. Repetitions are allowed and the lines may span any subspace (`claims.md`, rows (a) and (b); `proof.md`, 9.3 and 10.1):

- (a) any 5 lines in R^3 satisfy S <= 4pi. PROVED (`proof.md`, Steps 0-9, conclusion in 9.3).
- (b) any 6 lines in R^4 satisfy S <= 13pi/2. PROVED (`proof.md`, Steps 0-9, conclusion in 9.3).

No step of the proof relies on a computer (`proof.md`, 10.1).

---

## 3. Cited vs. ours

**Cited.** No published result is cited, and no problem-specific result is cited. In particular, nothing is cited for the statement being proved. The proof uses only the textbook tools listed in `proof.md`, lines 6-9:

- the extreme value theorem on a compact set;
- the intermediate value theorem;
- the rank of a Gram matrix equals the dimension of the span of the vectors;
- a function that is continuous on a closed interval and has non-positive second derivative inside is concave;
- a concave function lies above its chords;
- elementary trigonometric identities.

(`proof.md` 4.2 also includes its own proof of the fact that a graph of maximum degree <= 2 has components that are vertices, paths or cycles.)

**Ours.** The whole argument, `proof.md` Steps 0-9, is the team's own work. The header of `claims.md` attributes it to task A-C4-003. Its components, as listed in `claims.md`:

@@CLAIMS@@

The inbox shipped to this Scribe task contains no literature-search record. This document therefore makes no statement about whether this argument, or parts of it, appear in the literature.

---

## 4. Proof

The accepted proof is reproduced below byte for byte, including the team's internal step labels ("rung R1" ... "rung R9") and one reference to a code folder (see Section 6). Section 5 gives a stdlib-only command that checks this block is identical to the pinned `proof.md`.

Reading guide. The step map is `claims.md`, reproduced in Section 3. The logical order is:

- Step 0 reduces both inequalities to (*): D(x) = sum_{i<j} arcsin|<x_i,x_j>| >= pi.
- Steps 1-3 pick a maximiser with the most orthogonal pairs and derive its local structure (Lemma A).
- Steps 4-5 show every component of that maximiser's non-orthogonality graph is an isolated vertex, a coincident pair, or a cycle of length m <= 6 whose span has dimension m - 2.
- Steps 6-8 prove D(K) >= pi for such cycles with m = 3, 4, 5, 6.
- Step 9 assembles the pieces.

<!-- BEGIN EMBEDDED proof.md -->
````text
@@PROOF@@````
<!-- END EMBEDDED proof.md -->

---

## 5. How to verify

**Mathematics.** The proof is a written, computer-free argument, so it is verified by reading Section 4 (equivalently `submission/proof.md`). No computation is load-bearing (`proof.md`, 10.1). The hand-in rule on computation (code included, under 10 minutes, rigorous arithmetic) therefore does not apply to any step.

**Integrity of the shipped files.** These commands only confirm byte identity; they do not check any mathematics. Run them from the directory that contains this `submission.md`. The Scribe ran both in its copy under `out/` and recorded the real output and time.

1. The shipped artefacts match the pinned hashes:

   ```
   cd submission && /usr/bin/time -p shasum -a 256 -c MANIFEST.sha256
   ```

   Expected output:

   ```
   proof.md: OK
   claims.md: OK
   ```

   Measured runtime: @@T1@@ (log: `verify/logs/01_manifest_check.txt`).

2. The proof embedded in Section 4 is byte-identical to `submission/proof.md` and to the pinned hash. The script `verify/check_embedded.py` uses the Python standard library only:

   ```
   /usr/bin/time -p python3 verify/check_embedded.py submission.md submission/proof.md 66449ec26e2a5bfc1f0c5fc00d2980aeb1dd3c1d791364a3a80af3b8ab289518
   ```

   Expected output:

   ```
   embedded proof sha256: 66449ec26e2a5bfc1f0c5fc00d2980aeb1dd3c1d791364a3a80af3b8ab289518
   proof.md       sha256: 66449ec26e2a5bfc1f0c5fc00d2980aeb1dd3c1d791364a3a80af3b8ab289518
   embedded == proof.md: OK
   embedded == pinned hash: OK
   ```

   Measured runtime: @@T2@@ (log: `verify/logs/02_embedded_check.txt`). @@PYNOTE@@

The Scribe re-ran both checks on the final version of this file, with identical output (logs `verify/logs/04_embedded_check_final.txt` and `verify/logs/05_manifest_check_final.txt`). Both runtimes are far below the 10-minute limit.

---

## 6. Limitations

- **Only (a) and (b) are established.** The general case N = d + 2 for every d >= 2 (Cell 5) is **not** established. `proof.md` 10.3 marks its scope remark as "not claimed". Steps 1-5 and 9 use only N = d + 2, but the cycle inequality (Steps 6-8) is proved only for cycles of length m <= 6. That is exactly what d in {3, 4} needs.
- **Sharpness** (`proof.md` 10.2) is noted, not required. The configurations e1,e1,e2,e2,e3 and e1,e1,e2,e2,e3,e4 attain the two bounds.
- **Code referenced but not shipped.** `proof.md` 10.1 mentions "the code in out/code/", and `claims.md` lists `code/check_cycles.py`, `code/random_search.py` and `code/check_identities.py`. Those rows have status CHECKED, which means evidence or support only, not load-bearing. This code was not among the accepted artefacts shipped to this Scribe task. It is therefore not included in this submission and was not re-run by the Scribe. No step of the proof depends on it (`proof.md` 10.1).
- **Internal labels kept.** The embedded proof keeps the team's internal labels ("rung R1" ... "R9") and the path "out/code/", because it is reproduced byte for byte. These labels carry no mathematical content.
- **What the verification commands show.** They confirm file integrity only. The correctness of the result rests on the written proof in Section 4. The statuses SOLVED / PROVED are copied from the team's brief and have not been upgraded.
- The Scribe flagged no step of the proof as reading wrong, and made no edits to it.
