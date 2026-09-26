# Problem H: report (generated 14:25 from run/board.md; statuses as gated)

- **Solved:** C1, C2, C3, C4, L1
- **Partial:** none
- **Counterexample:** none
- **Not solved:** C5
- **Not attempted:** C6, handin

| Cell | Pts | Phase | Cell status | Claim status | Robustness | Best so far | Final report |
|---|---|---|---|---|---|---|---|
| C1 | 1 | submitted; gated | SOLVED | PROVED: U(Q3)=14, U(Q4)=34 (LB = H-L1 at d=3,4; labellings checker-verified, pinned) | – | Q3 14, Q4 34 (checker re-scored) | – |
| C2 | 2 | submitted (portal: correct); gated | SOLVED | PROVED 88 (gated H-C4-001 claim C10, d=5; both referees ACCEPT C10) | – | 88 (H-C2-001, H-C2-002, H-C5-002) | – |
| C3 | 3 | submitted (portal: correct); gated | SOLVED | PROVED 204 (gated H-C4-001 claim C10, d=6; both referees ACCEPT C10) | – | 204 (H-C3-001, H-C2-002, H-C5-002) | – |
| C4 | 5 | submitted (portal: correct); gated | SOLVED | PROVED 464, 1040 (gate VALID: H-C4-002 + H-C4-003 ACCEPT) | – | Q7 464, Q8 1040 (H-C4-001, H-C2-002, H-C5-002) | – |
| C5 | 8 | closed (humans: option 1) | NOT SOLVED | BEST-FOUND 2400 (= organisers; no improvement); LB unconditional 2312 | – | 2400 (5 lineages) | – |
| C6 | 13 | - | NOT ATTEMPTED | OPEN | – | – | – |
| L1 | 0 (lemma for C1-C4) | gated | SOLVED | PROVED (gate VALID 13:21: H-L1-002 + H-L1-003 ACCEPT) | – | U(Q_d) >= d*2^(d-1)+2 for all d >= 3 (accepted/proof.md) | – |
| handin |  |  | NOT ATTEMPTED |  | – |  | – |

## Top cells for human attention
- none

## Partial cells: established / remaining gap
- none

## Contested cells
- none

## Obstacles: why the remaining cells are not solved now
- [14:01] H-C5 lower route: TRIED: parity split + clique cover (H-C5-007). STALLS AT: R9, tau(G_2[F∩E]) <= z+2 for 4 <= z <= 116. PROVED (unrefereed): forests missing <= 3 vertices of one parity have <= 279 vertices, so such labellings have >= 2376 paths. Unconditional LB still 2312. KNOWN: 225/226 <= nabla(Q_9) <= 236 (Pike 2003, Hertz 2021; H-C5-006).
- [14:04] H-C5 (H-C5-006 analyst): published 225 <= nabla(Q_9) <= 236 (Hertz 2021 Table 4, citing Pike 2003; Pike itself paywalled, unopened). No source gives a decycling set <= 235 or nabla(Q_9) >= 227. Independent decycling sets have size >= 2^(d-1) - A(d,4) = 236 (A(9,4) = 20 cited), so an upper-route S_f must contain an edge. Searches for a 277-vertex induced forest: none found.
- [14:24] H-C5 CLOSED (run 1:17): TRIED: parity/code construction + decycling SA (H-C5-002), FVS SAT+LS (H-C5-001), decycling local search (H-C5-003), symmetric SAT (H-C5-004), recursive product (H-C5-005), lower-route parity split (H-C5-007), literature (H-C5-006). STALLS AT: a decycling set of Q_9 with <= 235 vertices (upper) or nabla(Q_9) >= 233 (lower). NEEDS: improving the published 225 <= nabla(Q_9) <= 236 (Pike 2003; Hertz 2021).

## Accepted artefacts (sha256-pinned)
- C1:
  - `097e5c92f62f4ecf8ddc2e2fbbf3b615105ee16cb9d10dbde0bf8ef6a7b97661  Q3.txt`
  - `912383bc03d769999ff7a1dce2aef7f8afa7e343249647928425bfe2f6d77603  Q4.txt`
- C2:
  - `dc4d05f3d52abadaab3f4122f223b7da920f5497ecdc3b11a4957118fe4ad519  Q5.txt`
- C3:
  - `98273905469c676dc582fbc1ae66c2d82c3cc14096e515dd65afaa60fd354e35  Q6.txt`
- C4:
  - `bf0b3db202968a757e1e65ebaf68c88d877f7257403e6ffb6da653d78ac5e1c8  Q7.txt`
  - `57244044982f79bc208b1ef8af60c291f278f695917eea784a7c15776fac694a  Q8.txt`
  - `ba6745d4bbcfef4c63483555ed8de97e5361790a6f983eba793f55047738ca31  claims.md`
  - `f60a89444da27fc1798c6a7cbca2669b666423522216227d4de3ee39793408ca  lb_forest.py`
  - `69819131c363c9bfbaa62d3652fa63f622c778e18a91733c5f9895bda71bb21c  crosscheck_F5_sat.py`
- L1:
  - `74ffd75fcad9d078ed441aa23ab9ccede8b76f3c92f80498721a019e0d29409d  proof.md`
  - `96e47cfb276d762004866b135b3d7e5b5370bb72756c2d866aa0b8075ccba66e  claims.md`
  - `a74b2fe94e55979851280df421c7afc2aeaa42671c7007f0a66ee81f5b84f98e  sanity.py`
