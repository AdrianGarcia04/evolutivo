# -------------------- Global -------------------- #
DATA_DIR=data
SRC_DIR=src
CC=gcc
CFLAGS=-O2
# -------------------- P1 defs -------------------- #
P1_DIR=p1
P1_FILE=main.py
DIMENSIONS=[2,5,10]
REP_P1=5
XLS_DIR=ejecuciones
# -------------------- P2 defs -------------------- #
P2_DIR=p2
P2_FILE=main.py
REP_P2=5
# -------------------- P3 I1 defs -------------------- #
P3_DIR=p3
I1_FILE=instance1
I1_NUM_VARS=10
I1_NUM_CLAUSES=5
# -------------------- P3 I2 defs -------------------- #
I2_FILE=instance2
I2_NUM_VARS=10
I2_NUM_CLAUSES=5
# -------------------- P3 I3 defs -------------------- #
I3_FILE=instance3
I3_NUM_VARS=25
I3_NUM_CLAUSES=30
# -------------------- P3 I4 defs -------------------- #
I4_FILE=instance4
I4_NUM_VARS=25
I4_NUM_CLAUSES=30
# -------------------- P3 I5 defs -------------------- #
I5_FILE=instance5
I5_NUM_VARS=50
I5_NUM_CLAUSES=60
# -------------------- P3 I6 defs -------------------- #
I6_FILE=instance6
I6_NUM_VARS=100
I6_NUM_CLAUSES=200

# -------------------- P1 -------------------- #
sphere:
	python3 $(SRC_DIR)/$(P1_DIR)/$(P1_FILE) Sphere $(DIMENSIONS) $(REP_P1) $(XLS_DIR)/Sphere.xls

ackley:
	python3 $(SRC_DIR)/$(P1_DIR)/$(P1_FILE) Ackley $(DIMENSIONS) $(REP_P1) $(XLS_DIR)/Ackley.xls

griewank:
	python3 $(SRC_DIR)/$(P1_DIR)/$(P1_FILE) Griewank $(DIMENSIONS) $(REP_P1) $(XLS_DIR)/Griewank.xls

tenth:
	python3 $(SRC_DIR)/$(P1_DIR)/$(P1_FILE) TenthPower $(DIMENSIONS) $(REP_P1) $(XLS_DIR)/TenthPower.xls

rast:
	python3 $(SRC_DIR)/$(P1_DIR)/$(P1_FILE) Rastrigin $(DIMENSIONS) $(REP_P1) $(XLS_DIR)/Rastrigin.xls

rosen:
	python3 $(SRC_DIR)/$(P1_DIR)/$(P1_FILE) Rosenbrock $(DIMENSIONS) $(REP_P1) $(XLS_DIR)/Rosenbrock.xls

p1all: sphere ackley griewank tenth rast rosen

# -------------------- P2 -------------------- #

solvepbl:
	python3 $(SRC_DIR)/$(P2_DIR)/$(P2_FILE) $(DATA_DIR)/pbl395.tsp $(REP_P2) $(XLS_DIR)/pbl395.xls

solvexqf:
	python3 $(SRC_DIR)/$(P2_DIR)/$(P2_FILE) $(DATA_DIR)/xqf131.tsp $(REP_P2) $(XLS_DIR)/xqf131.xls

solvexqg:
	python3 $(SRC_DIR)/$(P2_DIR)/$(P2_FILE) $(DATA_DIR)/xqg237.tsp $(REP_P2) $(XLS_DIR)/xqg237.xls

# -------------------- P3 -------------------- #

genI1:
	$(CC) $(CFLAGS) -o generate_3sat $(SRC_DIR)/$(P3_DIR)/instance_3sat.c $(SRC_DIR)/$(P3_DIR)/generate_3sat.c
	./generate_3sat $(I1_NUM_VARS) $(I1_NUM_CLAUSES) > $(DATA_DIR)/$(I1_FILE).txt

genI2:
	$(CC) $(CFLAGS) -o generate_3sat $(SRC_DIR)/$(P3_DIR)/instance_3sat.c $(SRC_DIR)/$(P3_DIR)/generate_3sat.c
	./generate_3sat $(I2_NUM_VARS) $(I2_NUM_CLAUSES) > $(DATA_DIR)/$(I2_FILE).txt

genI3:
	$(CC) $(CFLAGS) -o generate_3sat $(SRC_DIR)/$(P3_DIR)/instance_3sat.c $(SRC_DIR)/$(P3_DIR)/generate_3sat.c
	./generate_3sat $(I3_NUM_VARS) $(I3_NUM_CLAUSES) > $(DATA_DIR)/$(I3_FILE).txt

genI4:
	$(CC) $(CFLAGS) -o generate_3sat $(SRC_DIR)/$(P3_DIR)/instance_3sat.c $(SRC_DIR)/$(P3_DIR)/generate_3sat.c
	./generate_3sat $(I4_NUM_VARS) $(I4_NUM_CLAUSES) > $(DATA_DIR)/$(I4_FILE).txt

genI5:
	$(CC) $(CFLAGS) -o generate_3sat $(SRC_DIR)/$(P3_DIR)/instance_3sat.c $(SRC_DIR)/$(P3_DIR)/generate_3sat.c
	./generate_3sat $(I5_NUM_VARS) $(I5_NUM_CLAUSES) > $(DATA_DIR)/$(I5_FILE).txt

genI6:
	$(CC) $(CFLAGS) -o generate_3sat $(SRC_DIR)/$(P3_DIR)/instance_3sat.c $(SRC_DIR)/$(P3_DIR)/generate_3sat.c
	./generate_3sat $(I6_NUM_VARS) $(I6_NUM_CLAUSES) > $(DATA_DIR)/$(I6_FILE).txt

genSol1:
	$(CC) $(CFLAGS) -o generate_3sat_sol $(SRC_DIR)/$(P3_DIR)/instance_3sat.c $(SRC_DIR)/$(P3_DIR)/utils.c $(SRC_DIR)/$(P3_DIR)/sol_3sat.c $(SRC_DIR)/$(P3_DIR)/test_sol_3sat.c
	./generate_3sat_sol $(DATA_DIR)/$(I1_FILE).txt 0 5 > $(XLS_DIR)/$(I1_FILE).xls

genSol2:
	$(CC) $(CFLAGS) -o generate_3sat_sol $(SRC_DIR)/$(P3_DIR)/instance_3sat.c $(SRC_DIR)/$(P3_DIR)/utils.c $(SRC_DIR)/$(P3_DIR)/sol_3sat.c $(SRC_DIR)/$(P3_DIR)/test_sol_3sat.c
	./generate_3sat_sol $(DATA_DIR)/$(I2_FILE).txt 0 5 > $(XLS_DIR)/$(I2_FILE).xls

genSol3:
	$(CC) $(CFLAGS) -o generate_3sat_sol $(SRC_DIR)/$(P3_DIR)/instance_3sat.c $(SRC_DIR)/$(P3_DIR)/utils.c $(SRC_DIR)/$(P3_DIR)/sol_3sat.c $(SRC_DIR)/$(P3_DIR)/test_sol_3sat.c
	./generate_3sat_sol $(DATA_DIR)/$(I3_FILE).txt 0 5 > $(XLS_DIR)/$(I3_FILE).xls

genSol4:
	$(CC) $(CFLAGS) -o generate_3sat_sol $(SRC_DIR)/$(P3_DIR)/instance_3sat.c $(SRC_DIR)/$(P3_DIR)/utils.c $(SRC_DIR)/$(P3_DIR)/sol_3sat.c $(SRC_DIR)/$(P3_DIR)/test_sol_3sat.c
	./generate_3sat_sol $(DATA_DIR)/$(I4_FILE).txt 0 5 > $(XLS_DIR)/$(I4_FILE).xls

genSol5:
	$(CC) $(CFLAGS) -o generate_3sat_sol $(SRC_DIR)/$(P3_DIR)/instance_3sat.c $(SRC_DIR)/$(P3_DIR)/utils.c $(SRC_DIR)/$(P3_DIR)/sol_3sat.c $(SRC_DIR)/$(P3_DIR)/test_sol_3sat.c
	./generate_3sat_sol $(DATA_DIR)/$(I5_FILE).txt 0 5 > $(XLS_DIR)/$(I5_FILE).xls

genSol6:
	$(CC) $(CFLAGS) -o generate_3sat_sol $(SRC_DIR)/$(P3_DIR)/instance_3sat.c $(SRC_DIR)/$(P3_DIR)/utils.c $(SRC_DIR)/$(P3_DIR)/sol_3sat.c $(SRC_DIR)/$(P3_DIR)/test_sol_3sat.c
	./generate_3sat_sol $(DATA_DIR)/$(I6_FILE).txt 0 5 > $(XLS_DIR)/$(I6_FILE).xls
