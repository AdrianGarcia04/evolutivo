import numpy as np
import sys
import math
import arguments
import matplotlib.pyplot as plt
from DataExtract import DataExtract

def field(data, field):
    res = []
    for lst in data:
        res.append(lst[field])
    return res

if __name__ == '__main__':
    fields = {
        "func_name": "str",
        "dim": "int",
        "cross": "float",
        "scale": "float",
        "population": "int",
        "evals": "int",
        "ex_time": "float",
        "best_found": "float",
    }

    data_extract = DataExtract(fields)
    data_extract.read(sys.argv[1])

    rosenbrock = data_extract.where("func_name", "rosenbrock")
    # Rosenbrock - F = 0.1
    rosenbrock_01 = data_extract.where("scale", 0.1, rosenbrock)
    print(f'Factor de escala: {0.1}\n Mejor: {min(field(rosenbrock_01, 7))}\n Promedio: {np.average(field(rosenbrock_01, 7))}\n Peor: {max(field(rosenbrock_01, 7))}\n Desv: {np.std(field(rosenbrock_01, 7))}')
    print("--------------------------------------")

    # Rosenbrock - F = 0.3
    rosenbrock_03 = data_extract.where("scale", 0.3, rosenbrock)
    print(f'Factor de escala: {0.3}\n Mejor: {min(field(rosenbrock_03, 7))}\n Promedio: {np.average(field(rosenbrock_03, 7))}\n Peor: {max(field(rosenbrock_03, 7))}\n Desv: {np.std(field(rosenbrock_03, 7))}')
    print("--------------------------------------")

    # Rosenbrock - F = 0.5
    rosenbrock_05 = data_extract.where("scale", 0.5, rosenbrock)
    print(f'Factor de escala: {0.5}\n Mejor: {min(field(rosenbrock_05, 7))}\n Promedio: {np.average(field(rosenbrock_05, 7))}\n Peor: {max(field(rosenbrock_05, 7))}\n Desv: {np.std(field(rosenbrock_05, 7))}')
    print("--------------------------------------")

    # Rosenbrock - F = 0.7
    rosenbrock_07 = data_extract.where("scale", 0.7, rosenbrock)
    print(f'Factor de escala: {0.7}\n Mejor: {min(field(rosenbrock_07, 7))}\n Promedio: {np.average(field(rosenbrock_07, 7))}\n Peor: {max(field(rosenbrock_07, 7))}\n Desv: {np.std(field(rosenbrock_07, 7))}')
    print("--------------------------------------")

    # Rosenbrock - F = 0.9
    rosenbrock_09 = data_extract.where("scale", 0.9, rosenbrock)
    print(f'Factor de escala: {0.9}\n Mejor: {min(field(rosenbrock_09, 7))}\n Promedio: {np.average(field(rosenbrock_09, 7))}\n Peor: {max(field(rosenbrock_09, 7))}\n Desv: {np.std(field(rosenbrock_09, 7))}')
    print("--------------------------------------")


    rastrigin = data_extract.where("func_name", "rastrigin")
    # Rastrigin - CR = 0.1
    rastrigin_01 = data_extract.where("cross", 0.1, rastrigin)
    print(f'Proba de cruza: {0.1}\n Mejor: {min(field(rastrigin_01, 7))}\n Promedio: {np.average(field(rastrigin_01, 7))}\n Peor: {max(field(rastrigin_01, 7))}\n Desv: {np.std(field(rastrigin_01, 7))}')
    print("--------------------------------------")

    # Rastrigin - CR = 0.5
    rastrigin_05 = data_extract.where("cross", 0.5, rastrigin)
    print(f'Proba de cruza: {0.3}\n Mejor: {min(field(rastrigin_05, 7))}\n Promedio: {np.average(field(rastrigin_05, 7))}\n Peor: {max(field(rastrigin_05, 7))}\n Desv: {np.std(field(rastrigin_05, 7))}')
    print("--------------------------------------")

    # Rastrigin - CR = 0.9
    rastrigin_09 = data_extract.where("cross", 0.9, rastrigin)
    print(f'Proba de cruza: {0.9}\n Mejor: {min(field(rastrigin_09, 7))}\n Promedio: {np.average(field(rastrigin_09, 7))}\n Peor: {max(field(rastrigin_09, 7))}\n Desv: {np.std(field(rastrigin_09, 7))}')
    print("--------------------------------------")


    # sphere - dim = 30
    sphere_30 = data_extract.where("dim", 30, data_extract.where("func_name", "sphere"))
    print(f'Funcion: sphere\n Mejor: {min(field(sphere_30, 7))}\n Promedio: {np.average(field(sphere_30, 7))}\n Peor: {max(field(sphere_30, 7))}\n Desv: {np.std(field(sphere_30, 7))}\n Tiempo: {np.average(field(sphere_30, 6))}')
    print("--------------------------------------")

    # ackley - dim = 30
    ackley_30 = data_extract.where("dim", 30, data_extract.where("func_name", "ackley"))
    print(f'Funcion: ackley\n Mejor: {min(field(ackley_30, 7))}\n Promedio: {np.average(field(ackley_30, 7))}\n Peor: {max(field(ackley_30, 7))}\n Desv: {np.std(field(ackley_30, 7))}\n Tiempo: {np.average(field(ackley_30, 6))}')
    print("--------------------------------------")

    # griewank - dim = 30
    griewank_30 = data_extract.where("dim", 30, data_extract.where("func_name", "griewank"))
    print(f'Funcion: griewank\n Mejor: {min(field(griewank_30, 7))}\n Promedio: {np.average(field(griewank_30, 7))}\n Peor: {max(field(griewank_30, 7))}\n Desv: {np.std(field(griewank_30, 7))}\n Tiempo: {np.average(field(griewank_30, 6))}')
    print("--------------------------------------")

    # tenth - dim = 30
    tenth_30 = data_extract.where("dim", 30, data_extract.where("func_name", "tenth"))
    print(f'Funcion: tenth\n Mejor: {min(field(tenth_30, 7))}\n Promedio: {np.average(field(tenth_30, 7))}\n Peor: {max(field(tenth_30, 7))}\n Desv: {np.std(field(tenth_30, 7))}\n Tiempo: {np.average(field(tenth_30, 6))}')
    print("--------------------------------------")

    # rastrigin - dim = 30
    rastrigin_30 = data_extract.where("dim", 30, data_extract.where("func_name", "rastrigin"))
    print(f'Funcion: rastrigin\n Mejor: {min(field(rastrigin_30, 7))}\n Promedio: {np.average(field(rastrigin_30, 7))}\n Peor: {max(field(rastrigin_30, 7))}\n Desv: {np.std(field(rastrigin_30, 7))}\n Tiempo: {np.average(field(rastrigin_30, 6))}')
    print("--------------------------------------")

    # rosenbrock - dim = 30
    rosenbrock_30 = data_extract.where("dim", 30, data_extract.where("func_name", "rosenbrock"))
    print(f'Funcion: rosenbrock\n Mejor: {min(field(rosenbrock_30, 7))}\n Promedio: {np.average(field(rosenbrock_30, 7))}\n Peor: {max(field(rosenbrock_30, 7))}\n Desv: {np.std(field(rosenbrock_30, 7))}\n Tiempo: {np.average(field(rosenbrock_30, 6))}')
    print("--------------------------------------")
