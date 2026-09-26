# Checklist: H-C6

## Part G (generic; shared with every agent, blind ones included)
- G1 The statement proved is exactly the cell's: no extra hypotheses, no weaker inequality, the full parameter range.
- G2 Every step justified. No unexplained "clearly", "similarly", "routine", "obviously", "by symmetry".
- G3 Base cases, edge and degenerate cases, exceptional parameter values handled.
- G4 Every claimed invariant is preserved; every claimed decrease is strict where strictness is needed.
- G5 Every construction works for every claimed parameter value, not only the tested ones.
- G6 No circularity, and no citation that is the statement itself.
- G7 Any computation is exact or interval-based, code included, under 10 minutes; a finite check proves
     nothing beyond its range; a computer-assisted step has a written reduction to exactly the set searched.
- G8 Cited results separated from new work, with precise references.
- G9 The proof says what is established and what is not.

## Part S (specific; referees and the gate only, NEVER shown to blind agents)
- S1 Exact statement and the quantities to be bounded: <from target.md>
- S2 Equality / extremal configurations where any valid proof must be tight: <from the statement or gated cells; else "unknown">
- S3 Cases the proof must cover: <parities, whole parameter ranges, degenerate inputs>
- S4 Known traps: <problem-skill pitfalls; failure modes seen in lower cells; each labelled source>
- S5 Consistency with other cells: <verified cells this must agree with, exact statements>
- S6 Small explicit instances with known optimum, and numerical checks any proof must pass: <from statement or gated results only>
