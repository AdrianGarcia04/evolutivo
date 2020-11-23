#!/bin/bash
for queens in {8..12}
do
  for i in {1..20}
  do
    echo "Repetición: $i. Reinas: $queens"
    python3 main.py -q $queens -s; sleep 1; clear
  done
done
