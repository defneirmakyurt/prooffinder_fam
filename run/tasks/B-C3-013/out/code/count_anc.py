#!/usr/bin/env python3
"""Counts A_k = { lambda : B^{M_k-2k-1}(lambda) = P_k } by backward search with the
conjugate preimage rule. Unconditionally A_k is a subset of E_k whenever d_B(P_k)=2k+1."""
import sys
from check_Ek import ancestors, Pk
for k in map(int, sys.argv[1:]):
    M = k*k - 2*k - 1
    A = ancestors(Pk(k), M - 2*k - 1)
    print(f"k={k} |A_k|={len(A)}", flush=True)
