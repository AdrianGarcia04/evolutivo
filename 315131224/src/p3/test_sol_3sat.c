#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "instance_3sat.h"
#include "sol_3sat.h"
#include "utils.h"

int main(int argc, char *argv[])
{
  char *file_name = argv[1];
  inst_3sat_t *inst =  read_3sat_file(file_name);

  unsigned int seed = (unsigned int) time(NULL);
  // unsigned int seed = 1601670311;
  // unsigned int seed = 1928309128;
  srand(seed);

  inst_3sat_sol_t *rand_solution = rand_3sat_sol(inst->num_vars);

  printf("Generated solution: \n");
  print_3sat_sol(rand_solution);

  int satisfied_clauses = eval_3sat(inst, rand_solution);
  printf("Satisfied clauses: %d of %d. ",
    satisfied_clauses, inst->num_clauses);

  if (satisfied_clauses == inst->num_clauses) {
    green();
    printf("PASS\n");
  }
  else {
    red();
    printf("FAILED\n");
  }
  reset();

  free_3sat(inst);
  free_3sat_sol(rand_solution);

  return 0;
}
