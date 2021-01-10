import sys
import numpy as np

class Instance:

    def __init__(self, funct="", maxiters=0, size=0, cross=0.0, scale=0.0, dim=0):
        self.funct = funct
        self.maxiters = maxiters * dim
        self.size = size
        self.cross = cross
        self.scale = scale
        self.dim = dim
        ranges = {
            "sphere": 5.12,
            "ackley": 30,
            "griewank": 600,
            "tenthPower": 5.12,
            "rastrigin": 5.12,
            "rosenbrock": 2.048
        }
        self.ranges = ranges[funct]
        self.population = np.random.uniform(low=-self.ranges, high=self.ranges, size=(size, dim))
