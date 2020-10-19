# -------------------- Global -------------------- #
DATA_DIR=data
SRC_DIR=src
RES_DIR=ejecuciones

# -------------------- P4 defs -------------------- #
P4_DIR=p4
MAX_ITER=100
TEMPERATURE=1000
N_TYPE=adjacent

# -------------------- P4 -------------------- #
solvepbl:
	python3 $(SRC_DIR)/$(P4_DIR)/main.py $(DATA_DIR)/pbl395.tsp $(MAX_ITER) $(TEMPERATURE) 0 $(N_TYPE)

savepbl:
	python3 $(SRC_DIR)/$(P4_DIR)/main.py $(DATA_DIR)/pbl395.tsp $(MAX_ITER) $(TEMPERATURE) 1 $(N_TYPE) $(RES_DIR)/TSP.xls

solvexqf:
	python3 $(SRC_DIR)/$(P4_DIR)/main.py $(DATA_DIR)/xqf131.tsp $(MAX_ITER) $(TEMPERATURE) 0 $(N_TYPE)

savexqf:
	python3 $(SRC_DIR)/$(P4_DIR)/main.py $(DATA_DIR)/xqf131.tsp $(MAX_ITER) $(TEMPERATURE) 1 $(N_TYPE) $(RES_DIR)/TSP.xls

solvexqg:
	python3 $(SRC_DIR)/$(P4_DIR)/main.py $(DATA_DIR)/xqg237.tsp $(MAX_ITER) $(TEMPERATURE) 0 $(N_TYPE)

savexqg:
	python3 $(SRC_DIR)/$(P4_DIR)/main.py $(DATA_DIR)/xqg237.tsp $(MAX_ITER) $(TEMPERATURE) 1 $(N_TYPE) $(RES_DIR)/TSP.xls

solveTSP: solvepbl solvexqf solvexqg

saveTSP: savepbl savexqf savexqg
