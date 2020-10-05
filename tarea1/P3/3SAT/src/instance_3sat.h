#ifndef INSTANCE_3SAT_H
#define INSTANCE_3SAT_H

/*
*  3SAT Instance Struct
*/
typedef struct {
  int num_vars;
  int num_clauses;
  int **clauses;
} inst_3sat_t;

/*
*  Function that, given the number of variables and clauses, returns
*    a 3SAT instance struct.
*  Input:
*    int num_vars > 0
*    int num_clauses > 0
*  Output:
*    inst_3sat_t* struct
*  Requests memory allocation.
*/
inst_3sat_t * create_3sat(int num_vars, int num_clauses);

/*
*  Function that, given a 3SAT instance struct, releases it's requested memory.
*  Input:
*    inst_3sat_t struct
*  Output:
*    void
*  Releases memory allocation.
*/
void free_3sat(inst_3sat_t *);

/*
*  Function that, given a file name, creates a 3SAT instance struct.
*  Input:
*    char* file_name
*  Output:
*    inst_3sat_t* struct
*  Requests memory allocation.
*/
inst_3sat_t * read_3sat_file(char *file_name);

/*
*  Function that, given a 3SAT instance struct, prints it in terminal.
*  Input:
*    inst_3sat_t struct
*  Output:
*    void
*/
void print_3sat(inst_3sat_t *);

/*
*  Function that, given a 3SAT instance struct, prints it in terminal.
*  Input:
*    inst_3sat_t struct
*  Output:
*    void
*/
void print_format_3sat(inst_3sat_t *);

/*
*  Function that, given the number of variables and clauses, creates
*    a random 3SAT instance struct.
*  Input:
*    int num_vars > 0
*    int num_clauses > 0
*  Output:
*    inst_3sat_t* struct
*/
inst_3sat_t * rand_3sat(int num_vars, int num_clauses);

#endif
