#include <stdio.h>
#include <stdlib.h>
#include "instance_3sat.h"

inst_3sat_t * create_3sat(int num_vars, int num_clauses) {
  inst_3sat_t *inst = NULL;

  inst = malloc(sizeof(inst_3sat_t));

  inst->num_vars = num_vars;
  inst->num_clauses = num_clauses;
  inst->clauses = malloc(sizeof(int *) * num_clauses);

  for(int i = 0; i < inst->num_clauses; i++)
    inst->clauses[i] = malloc(sizeof(int) * 3);

  return inst;
}

void free_3sat(inst_3sat_t *inst) {
  for(int i = 0; i < inst->num_clauses; i++)
    free(inst->clauses[i]);

  free(inst->clauses);
  free(inst);
}

inst_3sat_t * read_3sat_file(char *nombreArchivo) {
  inst_3sat_t *inst = NULL;

  FILE *in = fopen(nombreArchivo, "r");

  int tmpScanf = 0;
  int num_vars = 0;
  int num_clauses = 0;

  tmpScanf = fscanf(in, "%d", &num_vars);
  tmpScanf = fscanf(in, "%d", &num_clauses);

  inst = create_3sat(num_vars, num_clauses);

  for(int i = 0; i < num_clauses; i++)
    tmpScanf = fscanf(in, "%d %d %d",
      &inst->clauses[i][0],
      &inst->clauses[i][1],
      &inst->clauses[i][2]);

  fclose(in);
  return inst;
}

void print_3sat(inst_3sat_t *inst) {
  printf("Variables: %d\nClauses: %d\n", inst->num_vars, inst->num_clauses);

  for(int i=0; i < inst->num_clauses; i++) {
    printf("%cx%d ∨ ",
      inst->clauses[i][0] > 0 ? ' ' : '-',
      inst->clauses[i][0] > 0 ? inst->clauses[i][0] : -inst->clauses[i][0] );

    printf("%cx%d ∨ ",
      inst->clauses[i][1] > 0 ? ' ' : '-',
      inst->clauses[i][1] > 0 ? inst->clauses[i][1] : -inst->clauses[i][1] );

    printf("%cx%d \n",
      inst->clauses[i][2] > 0 ? ' ' : '-',
      inst->clauses[i][2] > 0 ? inst->clauses[i][2] : -inst->clauses[i][2] );
  }
}

void print_format_3sat(inst_3sat_t *inst) {
  printf("%d\n%d\n", inst->num_vars, inst->num_clauses);

  for(int i=0; i < inst->num_clauses; i++)
    printf("%d %d %d\n",
      inst->clauses[i][0],
      inst->clauses[i][1],
      inst->clauses[i][2]);
}

inst_3sat_t * rand_3sat(int num_vars, int num_clauses) {

  inst_3sat_t * inst = create_3sat(num_vars, num_clauses);
  int v1, v2, v3;
  int num_asign = 0;

  for(int i = 0; i < num_clauses; i++) {

    if (num_asign < num_vars) {
      v1 = 1 + (num_asign++ % num_vars);
      v2 = 1 + (num_asign++ % num_vars);
      v3 = 1 + (num_asign++ % num_vars);
    }
    else {
      v1 = 1 + (i % num_vars);
      v2 = 1 + (rand() % (num_vars));
      v3 = 1 + (rand() % (num_vars));

      while (v1 == v2) v2 = 1 + (rand() % (num_vars));
      while (v2 == v3) v3 = 1 + (rand() % (num_vars));
      while (v1 == v3) v3 = 1 + (rand() % (num_vars));
    }

    inst->clauses[i][0] = (rand() % 2 == 0 ? v1 : -v1);
    inst->clauses[i][1] = (rand() % 2 == 0 ? v2 : -v2);
    inst->clauses[i][2] = (rand() % 2 == 0 ? v3 : -v3);
  }

  return inst;
}
