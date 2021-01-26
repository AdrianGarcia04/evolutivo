import numpy as np

def cosin(x, y):
    return np.cos(x) * np.sin(y)

def a(x, y):
    return np.sin(x) ** 10 + np.cos(10 + y * x) * np.cos(x)

def b(x, y):
    return np.cos(x / 2) + np.sin(y / 4)

def c(x, y):
    return np.cos(np.sqrt(x ** 3)) + np.sin(np.sqrt(y ** 3))

fncts = {
    "cosin": cosin,
    "a": a,
    "b": b,
    "c": c,
}
