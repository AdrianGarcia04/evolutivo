#!/bin/bash
for FUNCT in sphere cosin a b c
do
  for i in {1..20}
  do
    for LR in 0.5 0.7
    do
      for OMEGA in 0.5 0.7
      do
        echo "Repetición: $i - $FUNCT"
        make data FUNCT=$FUNCT LR=$LR OMEGA=$OMEGA
        clear
      done
    done
  done
done
