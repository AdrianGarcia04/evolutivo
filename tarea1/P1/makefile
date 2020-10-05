DIMENSIONS=[2,5,10]
REP=5
FILE=evaluation_functions.py
CSV_DIR=csv

sphere:
	python3 $(FILE) Sphere $(DIMENSIONS) $(REP) > $(CSV_DIR)/Sphere.csv

ackley:
	python3 $(FILE) Ackley $(DIMENSIONS) $(REP) > $(CSV_DIR)/Ackley.csv

griewank:
	python3 $(FILE) Griewank $(DIMENSIONS) $(REP) > $(CSV_DIR)/Griewank.csv

tenth:
	python3 $(FILE) TenthPower $(DIMENSIONS) $(REP) > $(CSV_DIR)/TenthPower.csv

rast:
	python3 $(FILE) Rastrigin $(DIMENSIONS) $(REP) > $(CSV_DIR)/Rastrigin.csv

rosen:
	python3 $(FILE) Rosenbrock $(DIMENSIONS) $(REP) > $(CSV_DIR)/Rosenbrock.csv
