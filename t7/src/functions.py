import numpy as np

def sphere(x, y):
    return np.sum(x**2 + y**2)

def cosin(x, y):
    return np.cos(x) * np.sin(y)

def a(x, y):
    return np.sin(x) ** 10 + np.cos(10 + y * x) * np.cos(x)

def b(x, y):
    return np.cos(x / 2) + np.sin(y / 4)

def c(x, y):
    return np.cos(np.sqrt(x ** 3)) + np.sin(np.sqrt(y ** 3))

fncts = {
    "sphere": sphere,
    "cosin": cosin,
    "a": a,
    "b": b,
    "c": c,
}
