import sys
import numpy as np
from functions import *

class Instance:

    def __init__(self, funct="", maxiters=0, size=0, cross=0.0, scale=0.0, dim=0):
        self.functName = funct
        self.maxiters = maxiters * dim
        self.size = size
        self.cross = cross
        self.scale = scale
        self.dim = dim
        self.ranges = ranges[funct]
        self.funct = functs[funct]
        self.population = np.random.uniform(low=-self.ranges, high=self.ranges, size=(size, dim))

    def generate_test_vect(self, i):
        rands = np.random.randint(0, self.size, size=3)
        while len(set(list(rands) + [i])) != 4:
            rands = np.random.randint(0, self.size, size=3)

        (r_1, r_2, r_3) = (rands[0], rands[1], rands[2])
        (x_1, x_2, x_3) = (self.population[r_1], self.population[r_2], self.population[r_3])

        diff = self.scale * (x_2 - x_3)
        return x_1 + diff
