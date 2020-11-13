import numpy as np
import sys
import arguments
import glob
import matplotlib.pyplot as plt
from DataExtract import DataExtract

if __name__ == '__main__':
    fields = {
        "iter": "int",
        "funct": "float",
    }

    instances = ["a280", "ch130", "pbl395", "xqf131", "xqg237"]
    tmps_lists = {
        "a280": [20, 150, 200, 1000, 2000],
        "ch130": [20, 150, 200, 1000, 2000],
        "pbl395": [10, 150, 250, 1000, 2000],
        "xqf131": [20, 150, 200, 1000, 2000],
        "xqg237": [10, 150, 250, 1000, 2000],
    }
    executions = len(instances) * len(tmps_lists)
    data_extract = DataExtract(fields)

    current_execution = 1
    for instance in instances:
        tmps = tmps_lists[instance]
        base_path = "../ejecuciones/" + instance + "/withtemps/"
        plt.figure(instance)

        for tmp in tmps:
            ref_path = base_path + f'evalwithtemp{tmp}'
            files = glob.glob(ref_path + ".txt")
            files = files + glob.glob(ref_path + "-[0-9]*.txt")

            values = []
            for file in files:
                data_extract.read(file)
                values.append(data_extract.get_field("funct"))

            values = np.array(values)
            rows, cols = values.shape
            averages = []
            for i in range(cols):
                averages.append(np.sum(values[:,i]) / rows)

            lab = f'T = {tmp}'
            plt.plot(averages, label=lab)
            plt.grid(which='major', color='#CCCCCC', linestyle='--')
            plt.grid(which='minor', color='#CCCCCC', linestyle=':')
            plt.minorticks_on()

            plt.legend(loc='upper right')

            plt.xlabel("Iteraciones")
            plt.ylabel("Función de evaluación (distancia total)")
            print("Percentage {}%".format(current_execution * 100 // executions), end="\r")
            current_execution += 1

        plt.savefig(f'../ejecuciones/{instance}/tmpsaverage')
