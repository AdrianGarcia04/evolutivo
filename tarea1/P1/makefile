DIMENSIONS=[2,5,10]
REP=5
FILE=evaluation_functions.py
CSV_DIR=xls

sphere:
	python3 $(FILE) Sphere $(DIMENSIONS) $(REP) $(CSV_DIR)/Sphere.xls

ackley:
	python3 $(FILE) Ackley $(DIMENSIONS) $(REP) $(CSV_DIR)/Ackley.xls

griewank:
	python3 $(FILE) Griewank $(DIMENSIONS) $(REP) $(CSV_DIR)/Griewank.xls

tenth:
	python3 $(FILE) TenthPower $(DIMENSIONS) $(REP) $(CSV_DIR)/TenthPower.xls

rast:
	python3 $(FILE) Rastrigin $(DIMENSIONS) $(REP) $(CSV_DIR)/Rastrigin.xls

rosen:
	python3 $(FILE) Rosenbrock $(DIMENSIONS) $(REP) $(CSV_DIR)/Rosenbrock.xls

all:
	python3 $(FILE) Sphere $(DIMENSIONS) $(REP) $(CSV_DIR)/Sphere.xls
	python3 $(FILE) Ackley $(DIMENSIONS) $(REP) $(CSV_DIR)/Ackley.xls
	python3 $(FILE) Griewank $(DIMENSIONS) $(REP) $(CSV_DIR)/Griewank.xls
	python3 $(FILE) TenthPower $(DIMENSIONS) $(REP) $(CSV_DIR)/TenthPower.xls
	python3 $(FILE) Rastrigin $(DIMENSIONS) $(REP) $(CSV_DIR)/Rastrigin.xls
	python3 $(FILE) Rosenbrock $(DIMENSIONS) $(REP) $(CSV_DIR)/Rosenbrock.xls
