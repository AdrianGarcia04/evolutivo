#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "instance_3sat.h"

int main(int argc, char *argv[]) {
  
  int num_vars = atoi(argv[1]);
  int num_clauses = atoi(argv[2]);

  unsigned int seed = (unsigned int) time(NULL);
  srand(seed);

  inst_3sat_t *inst = rand_3sat(num_vars, num_clauses);

  print_format_3sat(inst);
  free_3sat(inst);
  return 0;
}
