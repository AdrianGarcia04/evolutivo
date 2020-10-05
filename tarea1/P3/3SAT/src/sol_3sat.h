#ifndef SOL_3SAT_H
#define SOL_3SAT_H

#include "instance_3sat.h"

#define TRUE 1
#define FALSE 0

/*
*  3SAT Instance Solution Struct
*/
typedef struct {
  int num_vars;
  int *asig;
} inst_3sat_sol_t;

/*
*  Function that, given the number of variables, returns a struct
*    solution for the 3SAT problem.
*  Input:
*    int num_vars > 0
*  Output:
*    inst_3sat_sol_t* struct
*  Requests memory allocation.
*/
inst_3sat_sol_t * create_3sat_sol(int num_vars);

/*
*  Function that, given a 3SAT instance struct solution, releases it's requested
*    memory.
*  Input:
*    inst_3sat_sol_t struct
*  Output:
*    void
*  Releases memory allocation.
*/
void free_3sat_sol(inst_3sat_sol_t *);

/*
*  Function that, given a 3SAT instance struct solution, prints it in terminal.
*  Input:
*    inst_3sat_t struct
*  Output:
*    void
*/
void print_3sat_sol(inst_3sat_sol_t *);

/*
*  Function that, given the number of variables, returns a random struct
*    solution for the 3SAT problem.
*  Input:
*    int num_vars > 0
*  Output:
*    inst_3sat_sol_t* struct
*  Requests memory allocation.
*/
inst_3sat_sol_t * rand_3sat_sol(int num_vars);

int eval_literal(int value, int is_neg);
int eval_3sat(inst_3sat_t *inst, inst_3sat_sol_t *sol);

#endif
