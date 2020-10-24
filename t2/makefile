# -------------------- Global -------------------- #
DATA_DIR=data
SRC_DIR=src
RES_DIR=ejecuciones

# -------------------- P1 defs -------------------- #
M_BITS=30
DIM=10
P1_DIR=p1
CODIFICATION=Gray
# CODIFICATION=Bin

# -------------------- P2 defs -------------------- #
P2_DIR=p2
MAX_ITER=500
TEMPERATURE=10000
N_TYPE=adjacent

# -------------------- P1 -------------------- #
solveSph:
	python3 $(SRC_DIR)/$(P1_DIR)/main.py Sphere $(DIM) $(M_BITS) $(CODIFICATION) 0

saveSph:
	python3 $(SRC_DIR)/$(P1_DIR)/main.py Sphere $(DIM) $(M_BITS) $(CODIFICATION) 1 $(RES_DIR)/Functions.xls

solveAck:
	python3 $(SRC_DIR)/$(P1_DIR)/main.py Ackley $(DIM) $(M_BITS) $(CODIFICATION) 0

saveAck:
	python3 $(SRC_DIR)/$(P1_DIR)/main.py Ackley $(DIM) $(M_BITS) $(CODIFICATION) 1 $(RES_DIR)/Functions.xls

solveGrie:
	python3 $(SRC_DIR)/$(P1_DIR)/main.py Griewank $(DIM) $(M_BITS) $(CODIFICATION) 0

saveGrie:
	python3 $(SRC_DIR)/$(P1_DIR)/main.py Griewank $(DIM) $(M_BITS) $(CODIFICATION) 1 $(RES_DIR)/Functions.xls

solveTenth:
	python3 $(SRC_DIR)/$(P1_DIR)/main.py TenthPower $(DIM) $(M_BITS) $(CODIFICATION) 0

saveTenth:
	python3 $(SRC_DIR)/$(P1_DIR)/main.py TenthPower $(DIM) $(M_BITS) $(CODIFICATION) 1 $(RES_DIR)/Functions.xls

solveRast:
	python3 $(SRC_DIR)/$(P1_DIR)/main.py Rastrigin $(DIM) $(M_BITS) $(CODIFICATION) 0

saveRast:
	python3 $(SRC_DIR)/$(P1_DIR)/main.py Rastrigin $(DIM) $(M_BITS) $(CODIFICATION) 1 $(RES_DIR)/Functions.xls

solveRosen:
	python3 $(SRC_DIR)/$(P1_DIR)/main.py Rosenbrock $(DIM) $(M_BITS) $(CODIFICATION) 0

saveRosen:
	python3 $(SRC_DIR)/$(P1_DIR)/main.py Rosenbrock $(DIM) $(M_BITS) $(CODIFICATION) 1 $(RES_DIR)/Functions.xls

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
