SRC_DIR = src
DATA_DIR = data
RES_DIR = ejecuciones
RES_FILE = results.txt
FUNCT = sphere
# sphere / ackley / griewank / tenth / rastrigin / rosenbrock
MAX_EVALS = 10000
SIZE = 100
CROSS = 0.9
SCALE = 0.7
DIM = 10

run:
	@python3 ./$(SRC_DIR)/main.py -f $(FUNCT) -m $(MAX_EVALS) -s $(SIZE) -cr $(CROSS) -sc $(SCALE) -d $(DIM)

sphere:
	@python3 ./$(SRC_DIR)/main.py -f sphere -m $(MAX_EVALS) -s $(SIZE) -cr $(CROSS) -sc $(SCALE) -d $(DIM)

ackley:
	@python3 ./$(SRC_DIR)/main.py -f ackley -m $(MAX_EVALS) -s $(SIZE) -cr $(CROSS) -sc $(SCALE) -d $(DIM)

griewank:
	@python3 ./$(SRC_DIR)/main.py -f griewank -m $(MAX_EVALS) -s $(SIZE) -cr $(CROSS) -sc $(SCALE) -d $(DIM)

tenth:
	@python3 ./$(SRC_DIR)/main.py -f tenth -m $(MAX_EVALS) -s $(SIZE) -cr $(CROSS) -sc $(SCALE) -d $(DIM)

rastrigin:
	@python3 ./$(SRC_DIR)/main.py -f rastrigin -m $(MAX_EVALS) -s $(SIZE) -cr $(CROSS) -sc $(SCALE) -d $(DIM)

rosenbrock:
	@python3 ./$(SRC_DIR)/main.py -f rosenbrock -m $(MAX_EVALS) -s $(SIZE) -cr $(CROSS) -sc $(SCALE) -d $(DIM)

save:
	@python3 ./$(SRC_DIR)/main.py -f $(FUNCT) -m $(MAX_EVALS) -s $(SIZE) -cr $(CROSS) -sc $(SCALE) -d $(DIM) >> $(RES_DIR)/$(RES_FILE)

stats:
	@python3 ./$(SRC_DIR)/statistics.py ./$(RES_DIR)/results.txt
