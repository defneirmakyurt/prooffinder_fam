#!/usr/bin/env bash
# run_classes.sh K TIMEOUT [first N classes] : run sym_forest_sat.py on each prime-order class rep (tmp/classes.txt)
P=/home/user/bainsahackathon/.venv/bin/python3
D=$(cd "$(dirname "$0")"/.. && pwd)
K=$1; TO=$2; NMAX=${3:-999}
head -n "$NMAX" "$D/tmp/classes.txt" | while read orbs order label g; do
  s=$(date +%s.%N)
  r=$(timeout "$TO" $P "$D/code/sym_forest_sat.py" 9 "$K" "$g" --out "$D/tmp/forest_${label//:/_}.txt" 2>&1 | grep -E 'UNSAT|SAT after|ERROR|STOPPED' | tail -1)
  [ -z "$r" ] && r="TIMED OUT at ${TO}s"
  e=$(date +%s.%N)
  printf "%s orbits=%s g=%s K=%s : %s [wall %.1fs]\n" "$label" "$orbs" "$g" "$K" "$r" "$(echo "$e - $s" | bc)"
done
