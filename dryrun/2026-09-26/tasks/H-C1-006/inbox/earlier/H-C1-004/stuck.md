# Stuck: H-C1-004

For the cell as stated (d = 3 and d = 4): **none**.  Both values are settled exhaustively, both
halves, in under a second.

Where the method stalls if pushed further (relevant only beyond this cell, recorded as information):

1. The branch and bound scales as the tree, not as n!, but it still blows up.  `bnb.py 4 34 --nolb`
   (memo only, no lower bound) did not terminate in 10 minutes, so the LB is what makes it work, not
   the memo.  I did not attempt d = 5 (32 vertices, 32! bijections); the memo key alone is a subset
   of 2^32 plus a boundary vector, so the current state representation (a Python int bitmask plus a
   tuple, in a dict) would not fit in memory at the node counts this LB implies.  Nothing in this
   report claims anything about d >= 5.

2. The lower bound LB(S) drops the valley term for R entirely (it uses only `[S is empty]`).  A
   sharper bound would need to reason about how many vertices of R can still be valleys, which needs
   an argument about independent sets in the induced subgraph Q_d[R] with no placed neighbours.
   I did not develop this.

3. Simulated annealing on Q_4 hit 34 on all 20 seeds, which was a useful signal but is not evidence
   of optimality by itself; the optimality comes from the exhaustive run.  For larger d, annealing
   with transposition moves and a full recount per move is O(2^d d) per step and would need an
   incremental evaluator to be usable.

4. I have no closed-form guess to offer that is justified by this work.  Two data points
   (U(Q_3) = 14, U(Q_4) = 34) do not determine a formula, and extrapolating from them would be
   guessing, not searching.  I deliberately did not do so.
