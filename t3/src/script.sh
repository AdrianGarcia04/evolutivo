#!/bin/bash
for tmp in 20 150 250 1000 2000
do
  for i in {1..10}
  do
    echo "Repetición: $i. Temperatura: $tmp"
    python3 main.py -m 5000 -f xqg237 -t $tmp -s; sleep 2; clear
  done
done
