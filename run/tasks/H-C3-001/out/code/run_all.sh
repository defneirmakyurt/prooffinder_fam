#!/bin/sh
# Rebuild and rerun everything the claims depend on (< 1 minute total on a laptop).
set -e
cd "$(dirname "$0")"
B=${BUILD:-/tmp/h_c3_build}; mkdir -p $B
gcc -O2 -o $B/exhaust_general exhaust_general.c
gcc -O2 -o $B/exhaust_forest exhaust_forest.c
gcc -O2 -o $B/anneal anneal.c -lm
gcc -O2 -o $B/forest_search forest_search.c -lm
echo "== checker on hand-ins"; for f in ../Q6.txt ../best.txt ../Q6_alt1.txt ../Q6_alt2.txt; do python3 verify.py $f --d 6; done
echo "== lower bound (headline, exhaustive, no symmetry, no size window)"
$B/exhaust_general 6 0 11 0 64 | tail -1
$B/exhaust_general 6 1 7 0 64 | tail -1
$B/exhaust_general 6 2 3 0 64 | tail -1
echo "== controls"
$B/exhaust_general 6 0 12 0 64 | tail -1
$B/exhaust_general 6 1 12 0 64 | tail -1
$B/exhaust_forest 5 13; $B/exhaust_forest 6 26; $B/exhaust_forest 6 27; $B/exhaust_forest 6 28
echo "== regenerate artefacts"
$B/anneal 6 1 2000000 4 $B/Q6_anneal_s1.txt 3.0 0.2 2>/dev/null; python3 verify.py $B/Q6_anneal_s1.txt --d 6
$B/forest_search 6 28 5 200000 20 $B/Q6_forest_p28_s5.txt; python3 verify.py $B/Q6_forest_p28_s5.txt --d 6
