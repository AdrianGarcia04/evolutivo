import numpy as np
import sys
import ast
import time

def sphere(xx):
    sum = 0;

    for x in xx:
        sum = sum + x**2

    return sum

def ackley(xx):
    n = len(xx)
    s1 = 0
    s2 = 0

    for x in xx:
        s1 = s1 + x**2
        s2 = s2 + np.cos(2 * np.pi * x)

    f = 20 + np.e - 20 * np.exp(- 0.2 * s1 / n) - np.exp(s2 / n)
    return f

def griewank(xx):
    s1 = 0
    p1 = 1
    i = 1
    for x in xx:
        s1 = s1 + x**2 / 4000
        p1 = p1 * np.cos(x / np.sqrt(i))
        i = i + 1

    f = 1 + s1 - p1
    return f

def tenth_power_function(xx):
    sum = 0;

    for x in xx:
        sum = sum + x**10

    return sum

def rastrigin(xx):
    s1 = 0;

    for x in xx:
        s1 = s1 + (x**2 - 10 * np.cos(2 * np.pi * x))

    f = 10 * len(xx) + s1
    return f

def rosenbrock(xx):
    sum = 0;

    for i in range(0, len(xx) - 1):
        sum = sum + (100 * (xx[i + 1] - xx[i]**2)**2 + (1 - xx[i])**2)

    return sum

def test(funct, xx):

    t1 = time.time()

    if funct == 'Sphere':
        fx = sphere(xx)
    elif funct == 'Ackley':
        fx = ackley(xx)
    elif funct == 'Griewank':
        fx = griewank(xx)
    elif funct == 'TenthPower':
        fx = tenth_power_function(xx)
    elif funct == 'Rastrigin':
        fx = rastrigin(xx)
    elif funct == 'Rosenbrock':
        fx = rosenbrock(xx)

    t2 = time.time()

    ex_time = (t2 - t1) * 1000.0

    return (fx, ex_time)

if __name__ == '__main__':

    funct = sys.argv[1]

    dim_str = sys.argv[2].strip('[]').split(',')
    dimensions = list(map(lambda x: int(x), dim_str))

    repetitions = int(sys.argv[3])

    ranges = {
        "Sphere": 5.12,
        "Ackley": 30,
        "Griewank": 600,
        "TenthPower": 5.12,
        "Rastrigin": 5.12,
        "Rosenbrock": 2.048
    }

    table = open(sys.argv[4], "w")

    r2instance = []
    results = []

    table.write("Función,Dimensión,Semilla,f(x),Tiempo\n")
    for dim in dimensions:
        for i in range(0, repetitions):
            np.random.seed(np.random.get_state()[1][np.random.randint(low=len(np.random.get_state()[1]))])
            seed = np.random.get_state()[1][0]

            xx = np.random.uniform(-ranges[funct], ranges[funct], dim)
            if dim == 2:
                r2instance = xx

            (fx, ex_time) = test(funct, xx)

            results.append(fx)

            table.write("{},{},{},{},{}\n".format(funct, dim, seed, fx, ex_time))

    table.write("\n\nFunción,Número de repeticiones,Dimensión,Mejor valor,Valor promedio,Peor valor,Ejemplo en R2\n")
    i = 0
    for dim in dimensions:
        l = i * repetitions
        h = (i + 1) * repetitions
        i = i + 1

        rowresults = results[l:h]
        lowest = min(rowresults)
        average = np.average(rowresults)
        highest = max(rowresults)

        if dim != 2:
            r2instance = ""

        table.write("{},{},{},{},{},{},{}\n".format(funct, repetitions, dim,
            lowest, average, highest, r2instance))

    table.close()
