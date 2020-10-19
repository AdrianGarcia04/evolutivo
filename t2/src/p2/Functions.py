import numpy as np

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
