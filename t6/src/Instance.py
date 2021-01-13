import sys
import numpy as np
from functions import *

class Instance:

    def __init__(self, funct="", maxevals=0, size=0, cross=0.0, scale=0.0, dim=0):
        self.functName = funct
        self.maxevals = maxevals * dim
        self.num_evals = 0
        self.size = size
        self.cross = cross
        self.scale = scale
        self.dim = dim
        self.ranges = ranges[funct]
        self.eval = functs[funct]
        self.population = np.random.uniform(low=-self.ranges, high=self.ranges, size=(size, dim))

    def not_term(self):
        return (self.num_evals < self.maxevals)

    def eval_ind(self, ind):
        self.num_evals += 1
        return self.eval(ind)

    def gen_mut_vect(self, i):

        rands = np.random.randint(0, self.size, size=3)
        while len(set(list(rands) + [i])) != 4:
            rands = np.random.randint(0, self.size, size=3)

        (r_1, r_2, r_3) = (rands[0], rands[1], rands[2])
        (x_1, x_2, x_3) = (self.population[r_1], self.population[r_2], self.population[r_3])

        diff = self.scale * (x_2 - x_3)
        return self.repair(x_1 + diff, x_1)

    def repair(self, child, base):
        for j in range(self.dim):
            if child[j] < -self.ranges:
                child[j] = base[j] + np.random.rand() * (-self.ranges - base[j])
            if child[j] > self.ranges:
                child[j] = base[j] + np.random.rand() * (self.ranges - base[j])
        return child

    def gen_test_vec(self, v_i, x_i):

        j_r = np.random.randint(0, self.dim)
        u_i = np.zeros(self.dim)

        for j in range(self.dim):
            r_cj = np.random.rand()
            if (r_cj < self.cross) or (j == j_r):
                u_i[j] = v_i[j]
            else:
                u_i[j] = x_i[j]

        return u_i
