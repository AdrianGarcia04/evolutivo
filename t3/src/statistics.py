import numpy as np
import sys
import math
import arguments
import matplotlib.pyplot as plt
from DataExtract import DataExtract

if __name__ == '__main__':
    fields = {
        "instance": "str",
        "best": "float",
        "init_temp": "float",
        "final_temp": "float",
        "ex_time": "float",
        "iters": "int",
    }

    dirs = ["a280", "ch130", "pbl395", "xqf131", "xqg237"]
    data_extract = DataExtract(fields)

    for dir in dirs:
        data_extract.read("../ejecuciones/" + dir + "/results.txt")
        best_evaluations = data_extract.get_field("best")
        execution_times = data_extract.get_field("ex_time")
        iterations = data_extract.get_field("iters")

        print(dir)
        print("Mínimo (mejor): ", min(best_evaluations))
        print("Máximo (peor): ", max(best_evaluations))
        print("Media (promedio): ", np.average(best_evaluations))
        print("Mediana: ", np.median(best_evaluations))
        print("Desviación estandar: ", np.std(best_evaluations))
        print("Promedio de iteraciones: ", np.average(iterations))
        print("Tiempo de ejecución promedio: ", np.average(execution_times), "s")
