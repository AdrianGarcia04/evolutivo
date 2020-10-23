# -------------------- Global -------------------- #
DATA_DIR=data
SRC_DIR=src
RES_DIR=ejecuciones

# -------------------- P1 defs -------------------- #
M_BITS=20
DIM=10
P1_DIR=p2

# -------------------- P2 defs -------------------- #
P2_DIR=p4
MAX_ITER=100
TEMPERATURE=1000
N_TYPE=adjacent

# -------------------- P1 -------------------- #
solveSph:
	python3 $(SRC_DIR)/$(P1_DIR)/main.py Sphere $(DIM) $(M_BITS)

solveAck:
	python3 $(SRC_DIR)/$(P1_DIR)/main.py Ackley $(DIM) $(M_BITS)

solveGrie:
	python3 $(SRC_DIR)/$(P1_DIR)/main.py Griewank $(DIM) $(M_BITS)

solveTenth:
	python3 $(SRC_DIR)/$(P1_DIR)/main.py TenthPower $(DIM) $(M_BITS)

solveRast:
	python3 $(SRC_DIR)/$(P1_DIR)/main.py Rastrigin $(DIM) $(M_BITS)

solveRosen:
	python3 $(SRC_DIR)/$(P1_DIR)/main.py Rosenbrock $(DIM) $(M_BITS)

# -------------------- P2 -------------------- #
solvepbl:
	python3 $(SRC_DIR)/$(P2_DIR)/main.py $(DATA_DIR)/pbl395.tsp $(MAX_ITER) $(TEMPERATURE) 0 $(N_TYPE)

savepbl:
	python3 $(SRC_DIR)/$(P2_DIR)/main.py $(DATA_DIR)/pbl395.tsp $(MAX_ITER) $(TEMPERATURE) 1 $(N_TYPE) $(RES_DIR)/TSP.xls

solvexqf:
	python3 $(SRC_DIR)/$(P2_DIR)/main.py $(DATA_DIR)/xqf131.tsp $(MAX_ITER) $(TEMPERATURE) 0 $(N_TYPE)

savexqf:
	python3 $(SRC_DIR)/$(P2_DIR)/main.py $(DATA_DIR)/xqf131.tsp $(MAX_ITER) $(TEMPERATURE) 1 $(N_TYPE) $(RES_DIR)/TSP.xls

solvexqg:
	python3 $(SRC_DIR)/$(P2_DIR)/main.py $(DATA_DIR)/xqg237.tsp $(MAX_ITER) $(TEMPERATURE) 0 $(N_TYPE)

savexqg:
	python3 $(SRC_DIR)/$(P2_DIR)/main.py $(DATA_DIR)/xqg237.tsp $(MAX_ITER) $(TEMPERATURE) 1 $(N_TYPE) $(RES_DIR)/TSP.xls

solveTSP: solvepbl solvexqf solvexqg

saveTSP: savepbl savexqf savexqg
