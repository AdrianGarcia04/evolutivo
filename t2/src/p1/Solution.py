import numpy as np
from BinaryUtils import *
from Functions import *

class Solution:
    def __init__(self, dim, m_bits, funct, as_gray=True):
        self.dim = dim
        self.m_bits = m_bits
        self.funct = funct
        self.bound = ranges[self.funct]
        self.as_gray = as_gray
        if as_gray:
            self.vect = self.rand_gray_vect(dim, m_bits)
        else:
            self.vect = self.rand_bin_vect(dim, m_bits)

    def rand_gray_vect(self, dim, m_bits):
        xx = np.random.uniform(-self.bound, self.bound, self.dim)
        nums = []
        for x in xx:
            nums.append(real_to_gray_interval(x, self.m_bits, -self.bound, self.bound))
        return nums

    def rand_bin_vect(self, dim, m_bits):
        xx = np.random.uniform(-self.bound, self.bound, self.dim)
        nums = []
        for x in xx:
            nums.append(real_to_bin_interval(x, self.m_bits, -self.bound, self.bound))
        return nums

    def explore_neighbourhood(self):
        best_eval = float("inf")
        best_sol = None
        for i, num in enumerate(self.vect):
            vect_copy = self.vect.copy()

            neighbours = generate_neighbourhood(num)
            rand_index = np.random.choice(len(neighbours))

            vect_copy[i] = neighbours[rand_index]
            (fx, _) = self.eval(vect_copy)
            if fx < best_eval:
                best_eval = fx
                best_sol = vect_copy
        return (best_eval, best_sol)

    def set_vect(self, vect):
        self.vect = vect

    def eval(self, vect):
        xx = []
        for coord in vect:
            if self.as_gray:
                xx.append(gray_interval_to_real(coord, self.m_bits, -self.bound, self.bound))
            else:
                xx.append(bin_interval_to_real(coord, self.m_bits, -self.bound, self.bound))
        return eval_funct(xx, self.funct)
