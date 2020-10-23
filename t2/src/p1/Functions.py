import numpy as np
import time

def sphere(xx):
    # x in [-5.12, 5.12]
    sum = 0;
    for x in xx:
        sum = sum + x**2
    return sum

def ackley(xx):
    # x in [-30, 30]
    n = len(xx)
    s1 = 0
    s2 = 0
    for x in xx:
        s1 = s1 + x**2
        s2 = s2 + np.cos(2 * np.pi * x)
    f = 20 + np.e - 20 * np.exp(- 0.2 * s1 / n) - np.exp(s2 / n)
    return f

def griewank(xx):
    # x in [-600, 600]
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
    # x in [-5.12, 5.12]
    sum = 0;
    for x in xx:
        sum = sum + x**10
    return sum

def rastrigin(xx):
    # x in [-5.12, 5.12]
    s1 = 0;
    for x in xx:
        s1 = s1 + (x**2 - 10 * np.cos(2 * np.pi * x))
    f = 10 * len(xx) + s1
    return f

def rosenbrock(xx):
    # x in [-2.048, 2.048]
    sum = 0;
    for i in range(0, len(xx) - 1):
        sum = sum + (100 * (xx[i + 1] - xx[i]**2)**2 + (1 - xx[i])**2)
    return sum

ranges = {
    "Sphere": 5.12,
    "Ackley": 30,
    "Griewank": 600,
    "TenthPower": 5.12,
    "Rastrigin": 5.12,
    "Rosenbrock": 2.048
}

def eval_funct(xx, funct, time=False):
    if time:
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

    ex_time = None
    if time:
        t2 = time.time()
        ex_time = (t2 - t1) * 1000.0

    return (fx, ex_time)
