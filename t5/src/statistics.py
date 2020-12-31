import numpy as np
import sys
import math
import arguments
import matplotlib.pyplot as plt
from DataExtract import DataExtract

if __name__ == '__main__':
    fields = {
        "queens": "int",
        "pop_init": "int",
        "pop_fini": "int",
        "prob_cross": "float",
        "prob_mut": "float",
        "best_fit": "int",
        "ex_time": "float",
        "iters": "int",
    }

    files = [f'n{n}results.txt' for n in range(8, 21)]
    data_extract = DataExtract(fields)

    for file in files:
        data_extract.read(f'../ejecuciones/{file}')
        iterations = data_extract.get_field("iters")
        execution_times = data_extract.get_field("ex_time")
        best_fits = data_extract.get_field("best_fit")

        experiments = len(iterations)
        solved = best_fits.count(0)
        print(file)
        print("Promedio de iteraciones: ", np.average(iterations))
        print("Tiempo de ejecución promedio: ", np.average(execution_times), "s")
        print(f'Porcentaje de éxito: {solved}/{experiments} = {solved * 100 / experiments}')
