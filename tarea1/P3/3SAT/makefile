CC=gcc
CFLAGS=-O2

DATA_DIR=data

FILE=instance1.txt
NUM_VARS=10
NUM_CLAUSES=5

genInstance:
	$(CC) $(CFLAGS) -o generate_3sat src/instance_3sat.c src/generate_3sat.c
	./generate_3sat $(NUM_VARS) $(NUM_CLAUSES) > $(DATA_DIR)/$(FILE)

genSol:
	$(CC) $(CFLAGS) -o generate_3sat_sol src/instance_3sat.c src/utils.c src/sol_3sat.c src/test_sol_3sat.c
	./generate_3sat_sol $(DATA_DIR)/$(FILE)
