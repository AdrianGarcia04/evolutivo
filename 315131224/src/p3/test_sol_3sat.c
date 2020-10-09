#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "instance_3sat.h"
#include "sol_3sat.h"
#include "utils.h"
#include <limits.h>

void prettyPrint(char* string) {

}

int main(int argc, char *argv[])
{
  char *file_name = argv[1];
  int pretty = atoi(argv[2]);
  int repetitions = atoi(argv[3]);
  inst_3sat_t *inst =  read_3sat_file(file_name);

  unsigned int seed = (unsigned int) time(NULL);
  srand(seed);

  int satisfied_clauses;
  inst_3sat_sol_t *rand_solution;
  int results [repetitions];
  if (!pretty) {
    printf("Instancia,Variables,Clausulas,Semilla,f(x)\n");

    for (int i = 0; i < repetitions; i++) {
      rand_solution = rand_3sat_sol(inst->num_vars);
      satisfied_clauses = eval_3sat(inst, rand_solution);

      printf("%s,%d,%d,%u,%d\n", file_name, inst->num_vars, inst->num_clauses,
          seed, satisfied_clauses);
      results[i] = satisfied_clauses;

      seed = rand();
      srand(seed);
    }

    int best = 0, worst = INT_MAX, sum = 0;
    for (int i = 0; i < repetitions; i++) {
      best = (results[i] > best) ? results[i] : best;
      worst = (results[i] < worst) ? results[i] : worst;
      sum += results[i];
    }

    int average = sum / repetitions;

    printf("\n\nInstancia,Variables,Clausulas,Mejor valor,Valor promedio,Peor valor,Ejemplo\n");

    char buffer[1024];
    int num_vars = inst->num_vars;
    snprintf(buffer, sizeof(buffer), "[%d, %d, %d, ..., %d, %d, %d]",
      rand_solution->asig[0], rand_solution->asig[1], rand_solution->asig[2],
      rand_solution->asig[num_vars - 3], rand_solution->asig[num_vars - 2], rand_solution->asig[num_vars - 1]);

    printf("%s,%d,%d,%d,%d,%d,%s", file_name, inst->num_vars, inst->num_clauses,
      best, average, worst, buffer);

  }

  if (pretty) {
    rand_solution = rand_3sat_sol(inst->num_vars);
    printf("Generated solution: \n");
    print_3sat_sol(rand_solution);
    satisfied_clauses = eval_3sat(inst, rand_solution);
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
  }

  free_3sat(inst);
  free_3sat_sol(rand_solution);

  return 0;
}
