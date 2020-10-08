DATA_DIR=data
SRC_DIR=src

P1_DIR=p1
P1_FILE=main.py
DIMENSIONS=[2,5,10]
REP=5
CSV_DIR=ejecuciones

P2_DIR=p2
P2_FILE=main.py

CC=gcc
CFLAGS=-O2

P3_DIR=p3
P3_FILE=instance1.txt
NUM_VARS=10
NUM_CLAUSES=5

# -------------------- P1 -------------------- #

sphere:
	python3 $(SRC_DIR)/$(P1_DIR)/$(P1_FILE) Sphere $(DIMENSIONS) $(REP) $(CSV_DIR)/Sphere.xls

ackley:
	python3 $(SRC_DIR)/$(P1_DIR)/$(P1_FILE) Ackley $(DIMENSIONS) $(REP) $(CSV_DIR)/Ackley.xls

griewank:
	python3 $(SRC_DIR)/$(P1_DIR)/$(P1_FILE) Griewank $(DIMENSIONS) $(REP) $(CSV_DIR)/Griewank.xls

tenth:
	python3 $(SRC_DIR)/$(P1_DIR)/$(P1_FILE) TenthPower $(DIMENSIONS) $(REP) $(CSV_DIR)/TenthPower.xls

rast:
	python3 $(SRC_DIR)/$(P1_DIR)/$(P1_FILE) Rastrigin $(DIMENSIONS) $(REP) $(CSV_DIR)/Rastrigin.xls

rosen:
	python3 $(SRC_DIR)/$(P1_DIR)/$(P1_FILE) Rosenbrock $(DIMENSIONS) $(REP) $(CSV_DIR)/Rosenbrock.xls

p1all: sphere ackley griewank tenth rast rosen

# -------------------- P2 -------------------- #

solvepbl:
	python3 $(SRC_DIR)/$(P2_DIR)/$(P2_FILE) $(DATA_DIR)/pbl395.tsp

solvexqf:
	python3 $(SRC_DIR)/$(P2_DIR)/$(P2_FILE) $(DATA_DIR)/xqf131.tsp

solvexqg:
	python3 $(SRC_DIR)/$(P2_DIR)/$(P2_FILE) $(DATA_DIR)/xqg237.tsp

# -------------------- P3 -------------------- #

genInstance:
	$(CC) $(CFLAGS) -o generate_3sat src/instance_3sat.c src/generate_3sat.c
	./generate_3sat $(NUM_VARS) $(NUM_CLAUSES) > $(DATA_DIR)/$(FILE)

genSol:
	$(CC) $(CFLAGS) -o generate_3sat_sol src/instance_3sat.c src/utils.c src/sol_3sat.c src/test_sol_3sat.c
	./generate_3sat_sol $(DATA_DIR)/$(FILE)
