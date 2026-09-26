#!/bin/bash
P=/home/user/bainsahackathon/.venv/bin/python3
cd /home/user/bainsahackathon/run/tasks/H-C5-001/out
run() { name=$1; shift; echo "== $name $*"; ( time timeout 75 $P code/ifvs_sat.py --d 9 --K 235 --timeout 70 --out tmp/S_sym_$name.txt "$@" | tail -1 ) 2>&1 | grep -v -e user -e sys -e '^$'; }
run comp --gen "t=111111111"
run cyc9 --gen "p=1,2,3,4,5,6,7,8,0"
run cyc3 --gen "p=3,4,5,6,7,8,0,1,2"
run swap4 --gen "p=1,0,3,2,5,4,7,6,8"
run t2 --gen "t=110000000"
run swap4t --gen "p=1,0,3,2,5,4,7,6,8;t=000000001"
run cyc9comp --gen "p=1,2,3,4,5,6,7,8,0" --gen "t=111111111"
run cyc3t --gen "p=3,4,5,6,7,8,0,1,2;t=100000000"
run rev --gen "p=8,7,6,5,4,3,2,1,0"
run cyc8 --gen "p=1,2,3,4,5,6,7,0,8"
run cyc8t --gen "p=1,2,3,4,5,6,7,0,8;t=000000001"
run cyc7 --gen "p=1,2,3,4,5,6,0,7,8"
