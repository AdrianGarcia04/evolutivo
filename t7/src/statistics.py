import numpy as np
import sys
import math
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
        "blo": "float",
        "bup": "float",
        "evals": "int",
        "size": "int",
        "dim": "int",
        "omega": "float",
        "phip": "float",
        "phig": "float",
        "lr": "float",
        "ex_time": "float",
        "best_found": "float",
    }

    data_extract = DataExtract(fields)
    data_extract.read(sys.argv[1])

    sphere = data_extract.where("func_name", "sphere")
    sphere = data_extract.where("lr", 0.5, sphere)
    sphere_05_05 = data_extract.where("omega", 0.5, sphere)
    print("Sphere")
    print(f'Lr: {0.5}\n Omega: {0.5}\n Mejor: {min(field(sphere_05_05, 11))}\n Promedio: {np.average(field(sphere_05_05, 11))}\n Peor: {max(field(sphere_05_05, 11))}\n Desv: {np.std(field(sphere_05_05, 11))}')
    print("--------------------------------------")

    sphere = data_extract.where("func_name", "sphere")
    sphere = data_extract.where("lr", 0.5, sphere)
    sphere_05_07 = data_extract.where("omega", 0.7, sphere)
    print("Sphere")
    print(f'Lr: {0.5}\n Omega: {0.7}\n Mejor: {min(field(sphere_05_07, 11))}\n Promedio: {np.average(field(sphere_05_07, 11))}\n Peor: {max(field(sphere_05_07, 11))}\n Desv: {np.std(field(sphere_05_07, 11))}')
    print("--------------------------------------")

    sphere = data_extract.where("func_name", "sphere")
    sphere = data_extract.where("lr", 0.7, sphere)
    sphere_07_05 = data_extract.where("omega", 0.5, sphere)
    print("Sphere")
    print(f'Lr: {0.7}\n Omega: {0.5}\n Mejor: {min(field(sphere_07_05, 11))}\n Promedio: {np.average(field(sphere_07_05, 11))}\n Peor: {max(field(sphere_07_05, 11))}\n Desv: {np.std(field(sphere_07_05, 11))}')
    print("--------------------------------------")

    sphere = data_extract.where("func_name", "sphere")
    sphere = data_extract.where("lr", 0.7, sphere)
    sphere_07_07 = data_extract.where("omega", 0.7, sphere)
    print("Sphere")
    print(f'Lr: {0.7}\n Omega: {0.7}\n Mejor: {min(field(sphere_07_07, 11))}\n Promedio: {np.average(field(sphere_07_07, 11))}\n Peor: {max(field(sphere_07_07, 11))}\n Desv: {np.std(field(sphere_07_07, 11))}')
    print("--------------------------------------")

    cosin = data_extract.where("func_name", "cosin")
    cosin = data_extract.where("lr", 0.5, cosin)
    cosin_05_05 = data_extract.where("omega", 0.5, cosin)
    print("cosin")
    print(f'Lr: {0.5}\n Omega: {0.5}\n Mejor: {min(field(cosin_05_05, 11))}\n Promedio: {np.average(field(cosin_05_05, 11))}\n Peor: {max(field(cosin_05_05, 11))}\n Desv: {np.std(field(cosin_05_05, 11))}')
    print("--------------------------------------")

    cosin = data_extract.where("func_name", "cosin")
    cosin = data_extract.where("lr", 0.5, cosin)
    cosin_05_07 = data_extract.where("omega", 0.7, cosin)
    print("cosin")
    print(f'Lr: {0.5}\n Omega: {0.7}\n Mejor: {min(field(cosin_05_07, 11))}\n Promedio: {np.average(field(cosin_05_07, 11))}\n Peor: {max(field(cosin_05_07, 11))}\n Desv: {np.std(field(cosin_05_07, 11))}')
    print("--------------------------------------")

    cosin = data_extract.where("func_name", "cosin")
    cosin = data_extract.where("lr", 0.7, cosin)
    cosin_07_05 = data_extract.where("omega", 0.5, cosin)
    print("cosin")
    print(f'Lr: {0.7}\n Omega: {0.5}\n Mejor: {min(field(cosin_07_05, 11))}\n Promedio: {np.average(field(cosin_07_05, 11))}\n Peor: {max(field(cosin_07_05, 11))}\n Desv: {np.std(field(cosin_07_05, 11))}')
    print("--------------------------------------")

    cosin = data_extract.where("func_name", "cosin")
    cosin = data_extract.where("lr", 0.7, cosin)
    cosin_07_07 = data_extract.where("omega", 0.7, cosin)
    print("cosin")
    print(f'Lr: {0.7}\n Omega: {0.7}\n Mejor: {min(field(cosin_07_07, 11))}\n Promedio: {np.average(field(cosin_07_07, 11))}\n Peor: {max(field(cosin_07_07, 11))}\n Desv: {np.std(field(cosin_07_07, 11))}')
    print("--------------------------------------")

    af = data_extract.where("func_name", "af")
    af = data_extract.where("lr", 0.5, af)
    af_05_05 = data_extract.where("omega", 0.5, af)
    print("A function")
    print(f'Lr: {0.5}\n Omega: {0.5}\n Mejor: {min(field(af_05_05, 11))}\n Promedio: {np.average(field(af_05_05, 11))}\n Peor: {max(field(af_05_05, 11))}\n Desv: {np.std(field(af_05_05, 11))}')
    print("--------------------------------------")

    af = data_extract.where("func_name", "af")
    af = data_extract.where("lr", 0.5, af)
    af_05_07 = data_extract.where("omega", 0.7, af)
    print("A function")
    print(f'Lr: {0.5}\n Omega: {0.7}\n Mejor: {min(field(af_05_07, 11))}\n Promedio: {np.average(field(af_05_07, 11))}\n Peor: {max(field(af_05_07, 11))}\n Desv: {np.std(field(af_05_07, 11))}')
    print("--------------------------------------")

    af = data_extract.where("func_name", "af")
    af = data_extract.where("lr", 0.7, af)
    af_07_05 = data_extract.where("omega", 0.5, af)
    print("A function")
    print(f'Lr: {0.7}\n Omega: {0.5}\n Mejor: {min(field(af_07_05, 11))}\n Promedio: {np.average(field(af_07_05, 11))}\n Peor: {max(field(af_07_05, 11))}\n Desv: {np.std(field(af_07_05, 11))}')
    print("--------------------------------------")

    af = data_extract.where("func_name", "af")
    af = data_extract.where("lr", 0.7, af)
    af_07_07 = data_extract.where("omega", 0.7, af)
    print("A function")
    print(f'Lr: {0.7}\n Omega: {0.7}\n Mejor: {min(field(af_07_07, 11))}\n Promedio: {np.average(field(af_07_07, 11))}\n Peor: {max(field(af_07_07, 11))}\n Desv: {np.std(field(af_07_07, 11))}')
    print("--------------------------------------")

    bf = data_extract.where("func_name", "bf")
    bf = data_extract.where("lr", 0.5, bf)
    bf_05_05 = data_extract.where("omega", 0.5, bf)
    print("B function")
    print(f'Lr: {0.5}\n Omega: {0.5}\n Mejor: {min(field(bf_05_05, 11))}\n Promedio: {np.average(field(bf_05_05, 11))}\n Peor: {max(field(bf_05_05, 11))}\n Desv: {np.std(field(bf_05_05, 11))}')
    print("--------------------------------------")

    bf = data_extract.where("func_name", "bf")
    bf = data_extract.where("lr", 0.5, bf)
    bf_05_07 = data_extract.where("omega", 0.7, bf)
    print("B function")
    print(f'Lr: {0.5}\n Omega: {0.7}\n Mejor: {min(field(bf_05_07, 11))}\n Promedio: {np.average(field(bf_05_07, 11))}\n Peor: {max(field(bf_05_07, 11))}\n Desv: {np.std(field(bf_05_07, 11))}')
    print("--------------------------------------")

    bf = data_extract.where("func_name", "bf")
    bf = data_extract.where("lr", 0.7, bf)
    bf_07_05 = data_extract.where("omega", 0.5, bf)
    print("B function")
    print(f'Lr: {0.7}\n Omega: {0.5}\n Mejor: {min(field(bf_07_05, 11))}\n Promedio: {np.average(field(bf_07_05, 11))}\n Peor: {max(field(bf_07_05, 11))}\n Desv: {np.std(field(bf_07_05, 11))}')
    print("--------------------------------------")

    bf = data_extract.where("func_name", "bf")
    bf = data_extract.where("lr", 0.7, bf)
    bf_07_07 = data_extract.where("omega", 0.7, bf)
    print("B function")
    print(f'Lr: {0.7}\n Omega: {0.7}\n Mejor: {min(field(bf_07_07, 11))}\n Promedio: {np.average(field(bf_07_07, 11))}\n Peor: {max(field(bf_07_07, 11))}\n Desv: {np.std(field(bf_07_07, 11))}')
    print("--------------------------------------")

    cf = data_extract.where("func_name", "cf")
    cf = data_extract.where("lr", 0.5, cf)
    cf_05_05 = data_extract.where("omega", 0.5, cf)
    print("C function")
    print(f'Lr: {0.5}\n Omega: {0.5}\n Mejor: {min(field(cf_05_05, 11))}\n Promedio: {np.average(field(cf_05_05, 11))}\n Peor: {max(field(cf_05_05, 11))}\n Desv: {np.std(field(cf_05_05, 11))}')
    print("--------------------------------------")

    cf = data_extract.where("func_name", "cf")
    cf = data_extract.where("lr", 0.5, cf)
    cf_05_07 = data_extract.where("omega", 0.7, cf)
    print("C function")
    print(f'Lr: {0.5}\n Omega: {0.7}\n Mejor: {min(field(cf_05_07, 11))}\n Promedio: {np.average(field(cf_05_07, 11))}\n Peor: {max(field(cf_05_07, 11))}\n Desv: {np.std(field(cf_05_07, 11))}')
    print("--------------------------------------")

    cf = data_extract.where("func_name", "cf")
    cf = data_extract.where("lr", 0.7, cf)
    cf_07_05 = data_extract.where("omega", 0.5, cf)
    print("C function")
    print(f'Lr: {0.7}\n Omega: {0.5}\n Mejor: {min(field(cf_07_05, 11))}\n Promedio: {np.average(field(cf_07_05, 11))}\n Peor: {max(field(cf_07_05, 11))}\n Desv: {np.std(field(cf_07_05, 11))}')
    print("--------------------------------------")

    cf = data_extract.where("func_name", "cf")
    cf = data_extract.where("lr", 0.7, cf)
    cf_07_07 = data_extract.where("omega", 0.7, cf)
    print("C function")
    print(f'Lr: {0.7}\n Omega: {0.7}\n Mejor: {min(field(cf_07_07, 11))}\n Promedio: {np.average(field(cf_07_07, 11))}\n Peor: {max(field(cf_07_07, 11))}\n Desv: {np.std(field(cf_07_07, 11))}')
    print("--------------------------------------")
