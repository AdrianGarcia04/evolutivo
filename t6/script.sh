#!/bin/bash
# Rosenbrock
for F in 0.1 0.3 0.5 0.7 0.9
do
  for i in {1..10}
  do
    echo "Repetición: $i - $F"
    make save FUNCT=rosenbrock SCALE=$F
    clear
  done
done

# Rosenbrock
for C in 0.1 0.5 0.9
do
  for i in {1..10}
  do
    echo "Repetición: $i - $F"
    make save FUNCT=rastrigin CROSS=$C
    clear
  done
done

# All, 30 times each
for F in sphere ackley griewank tenth rastrigin rosenbrock
do
  for i in {1..30}
  do
    echo "Repetición: $i - $F"
    make save FUNCT=$F DIM=30
    clear
  done
done
