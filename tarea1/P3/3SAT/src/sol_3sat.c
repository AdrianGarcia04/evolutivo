#include <stdio.h>
#include <stdlib.h>
#include "sol_3sat.h"
#include "utils.h"

inst_3sat_sol_t * create_3sat_sol(int num_vars) {
  inst_3sat_sol_t *solution = NULL;

  solution = malloc(sizeof(inst_3sat_sol_t));
  solution->num_vars = num_vars;
  solution->asig = malloc(sizeof(int) * num_vars);

  return solution;
}

void free_3sat_sol(inst_3sat_sol_t *solution) {
  free(solution->asig);
  free(solution);
}

void print_3sat_sol(inst_3sat_sol_t *solution) {

  printf("[");
  for(int i = 0; i < solution->num_vars; i++) {
    (solution->asig[i]) ? green() : red();
    printf("%d", solution->asig[i]);
    reset();
    if (i + 1 < solution->num_vars)
      printf(",");
  }
  printf("]\n");
}

inst_3sat_sol_t * rand_3sat_sol(int num_vars) {
  inst_3sat_sol_t *solution = create_3sat_sol(num_vars);

  for(int i=0; i < num_vars; i++)
    solution->asig[i] = rand() % 2 == 0 ? TRUE : FALSE;

  return solution;
}

int eval_literal(int value, int is_neg) {
  return (is_neg && value == FALSE) || (!is_neg && value == TRUE);
}

int eval_3sat(inst_3sat_t *inst, inst_3sat_sol_t *solution) {

  int satisfied_clauses = 0;
  int var1, var2, var3;
  for(int i=0; i < inst->num_clauses; i++) {
    var1 = inst->clauses[i][0] > 0 ? inst->clauses[i][0] : -inst->clauses[i][0];
    var2 = inst->clauses[i][1] > 0 ? inst->clauses[i][1] : -inst->clauses[i][1];
    var3 = inst->clauses[i][2] > 0 ? inst->clauses[i][2] : -inst->clauses[i][2];

    satisfied_clauses += (
      eval_literal(solution->asig[var1], inst->clauses[i][0] < 0) ||
      eval_literal(solution->asig[var2], inst->clauses[i][1] < 0) ||
      eval_literal(solution->asig[var3], inst->clauses[i][2] < 0)
      ) ? 1 : 0;
  }

  return satisfied_clauses;
}
