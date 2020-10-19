from Instance import Instance
import sys
import os
import numpy as np
import time
from itertools import tee

def pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

def test(cities, tspInstance):

    t1 = time.time()

    sum = 0
    for a, b in pairwise(cities):
        sum = sum + tspInstance.getDistance(a, b)

    t2 = time.time()

    ex_time = (t2 - t1) * 1000.0

    return (sum, ex_time)

def getExampleString(results, num_nodes):
    slice1 = example[0:3]
    slice2 = example[(num_nodes-2):]

    string = "["
    for city in slice1:
        string = string + "{}-".format(city)

    for city in slice2:
        string = string + "{}-".format(city)

    return string[:-1] + "]"

if __name__ == '__main__':

    tspInstance = Instance.readFile(sys.argv[1])

    instance = sys.argv[1].replace("data/", "")
    repetitions = int(sys.argv[2])
    num_nodes = len(tspInstance.nodes)

    results = []

    table = open(sys.argv[3], "w")

    table.write("Instancia,Dimensión,Semilla,f(x),Tiempo\n")
    for i in range(0, 5):

        np.random.seed(np.random.get_state()[1][np.random.randint(low=len(np.random.get_state()[1]))])
        seed = np.random.get_state()[1][0]

        cities = list(np.random.choice(num_nodes, size=num_nodes, replace=False))
        cities.append(cities[0])

        (fx, ex_time) = test(cities, tspInstance)

        results.append(fx)
        example = cities

        table.write("{},{},{},{},{}\n".format(instance, num_nodes, seed, fx, ex_time))


    table.write("\n\nInstancia,Número de repeticiones,Dimensión,Mejor valor,Valor promedio,Peor valor,Ejemplo en R2\n")
    lowest = min(results)
    average = np.average(results)
    highest = max(results)

    exampleString = str(getExampleString(results, num_nodes))
    table.write("{},{},{},{},{},{},{}\n".format(instance, repetitions, num_nodes,
        lowest, average, highest, exampleString))

    table.close()
