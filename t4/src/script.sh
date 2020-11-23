#!/bin/bash
for queens in {8..20}
do
  for i in {1..5}
  do
    echo "Repetición: $i. Reinas: $queens"
    python3 main.py -q $queens -s; sleep 1; clear
  done
done
