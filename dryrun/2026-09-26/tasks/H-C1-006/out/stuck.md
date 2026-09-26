# Stuck: H-C1-006

For the cell as stated (the integers U(Q_3), U(Q_4), each with an attaining labelling): **none**.
Both lower bounds are proved by hand in out/proof.md with no computation; both upper bounds are
explicit labellings, each scored twice by independent counters (out/code/uphill.py).

Where the work is incomplete or would stall next:

1. **Two references not opened.** The AoPS Wiki page for 2022 IMO P6 returns HTTP 403 to the fetch
   tool, and Evan Chen's IMO 2022 notes PDF could not be decoded offline (no pdftotext / mutool /
   pypdf available). Neither is relied on; the Bajnok report supplies the same argument and was
   read verbatim. If a second independent write-up of the IMO lower bound is wanted, these are the
   two to open.
2. **On-site MathOverflow / math.stackexchange search was not done**, only search-engine queries;
   and the DuckDuckGo and Google endpoints were blocked (CAPTCHA, consent redirect). So my
   "not found" for the hypercube question rests on a narrower sweep than I would like.
3. **The method's reach.** Step 6 characterises only the equality case P = |E| + 1. To settle
   U(Q_d) for d >= 5 one would have to characterise P = |E| + c for c = 2, 3, ..., and the
   bookkeeping grows: at level c one must control the multiset of "excesses" N(v) - 1 weighted by
   up(v), together with the number of valleys, and the down-degree count becomes an inequality
   rather than an identity. I did not attempt this. My Remark gives only
   U(Q_d) >= d*2^{d-1} + 2, which for d = 9 reads U(Q_9) >= 2306 -- far below the 2368 the cell's
   statement quotes as known. So nothing here helps cells C2-C6.
4. **No literature target exists to compare against for the cube.** I found no source stating any
   value of U(Q_d). That means the only external check on 14 and 34 is the agreement of three
   independent runs plus a hand proof; there is no published number to confirm them.
