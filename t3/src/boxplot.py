import numpy as np
import sys
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
        best_by_tmp = data_extract.segment("best", "init_temp")

        keys = list(best_by_tmp.keys())
        keys.sort()

        values = []
        for k in keys:
            values.append(best_by_tmp[k])

        plt.figure(dir)
        plt.boxplot(values)

        poss = []
        for p in range(len(keys)):
            poss.append(p + 1)

        plt.xticks(ticks=poss, labels=keys)
        plt.xlabel("Temperaturas")
        plt.ylabel("Función de evaluación (distancia total)")
        plt.title(f'Boxplot de la instancia {dir}', loc='left')

        plt.savefig(f'../ejecuciones/{dir}/boxplot')
