import numpy as np

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

fncts = {
    "sphere": sphere,
    "ackley": ackley,
    "griewank": griewank,
    "tenth": tenth_power_function,
    "rastrigin": rastrigin,
    "rosenbrock": rosenbrock
}
