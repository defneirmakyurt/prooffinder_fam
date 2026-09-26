# Stuck: B-C3-007

Parts (a) and (b), and (c) in the form "maximisers = {lambda |- T_k-1 : B^{k^2-2k-2}(lambda) = nu_k}", are proved for every k >= 4 (proof.md). None of these is stuck.

One point is open, and it is a question of reading the brief rather than a gap in the mathematics:
- The target for (c) asks for the maximiser set "as explicit functions of k". What I give is an explicit criterion: the fixed partition nu_k = (k+1,k-1,k-2,...,3,1) and the fixed depth k^2-2k-2. I do not give a closed-form list. The set grows fast (1, 6, 34, 175, 831, 3911 for k = 4..9, computed), so a closed list is unlikely to exist.
- GH (Thm 3.8 and the remark after it) found that, in the analogous triangular case, their natural necessary conditions stop being sufficient at k = 8.
- If the graders want the members listed, this needs a description of the B-preimage tree of nu_k to depth k^2-2k-2. I have not attempted that.
