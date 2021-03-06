from Instance import Instance
import numpy as np
import math
import time

class Solution:
    def __init__(self, instance, perm=None, perm_random=False, to_eval=True):
        self.instance = instance
        self.dim = instance.dim
        self.perm = np.array(range(self.dim))
        self.eval = float("inf")

        # If the perm exists, take it
        if perm is not None:
            self.perm = np.array(perm)
        # Else, if specified, create random solution
        elif perm_random:
            self.rand_sol()

        self.distances = instance.distances
        self.evaluation = np.zeros(self.dim, dtype="float64")

        # If specified, evaluate solution
        if to_eval:
            self.evaluate()

    def init_rand_sol(instance):
        return Solution(instance, perm_random=True, to_eval=False)

    def rand_sol(self):
        self.perm = np.random.permutation(self.dim)

    def evaluate(self):
        self.eval = 0
        nodes = self.instance.nodes
        # Calc distance between nodes
        for i in range(self.dim - 1):
            self.evaluation[i] = self.distances[self.perm[i]][self.perm[i + 1]]
            self.eval += self.evaluation[i]
        # Calc distance between first and last node
        self.evaluation[self.dim - 1] = self.distances[self.perm[0]][self.perm[self.dim - 1]]
        self.eval += self.evaluation[self.dim - 1]
        return self.eval

    def eval_swap(self, x, y, apply=False):
        (x, y) = (min(x, y), max(x, y))

        diff_eval = 0
        eval_suc_x = 0
        eval_pred_y = 0
        if (y != x + 1):
          eval_suc_x = self.distances[self.perm[y]][self.perm[x+1]]
          eval_pred_y = self.distances[self.perm[y-1]][self.perm[x]]
        else:
          eval_suc_x = self.evaluation[x]
          eval_pred_y = self.evaluation[y-1]

        diff_eval += eval_suc_x-self.evaluation[x]
        diff_eval += eval_pred_y-self.evaluation[y-1]

        eval_pred_x = 0
        eval_suc_y = 0

        if x > 0:
          eval_pred_x = self.distances[self.perm[x-1]][self.perm[y]]
          diff_eval += eval_pred_x-self.evaluation[x-1]

        if y < (self.dim -1):
          eval_suc_y = self.distances[self.perm[x]][self.perm[y+1]]
          diff_eval += eval_suc_y-self.evaluation[y]

        eval_fin = 0
        if x == 0:
          if y != self.dim-1:
            eval_fin = self.distances[self.perm[self.dim-1]][self.perm[y]]
          else:
            eval_fin = self.evaluation[self.dim - 1]

          diff_eval += eval_fin - self.evaluation[self.dim-1]

        if y == (self.dim-1):
          if x != 0:
            eval_fin = self.distances[self.perm[x]][self.perm[0]]
          else:
            eval_fin = self.evaluation[self.dim - 1]

          diff_eval += eval_fin - self.evaluation[self.dim-1]

        new_eval = self.eval + diff_eval

        if apply:
          self.evaluation[x] = eval_suc_x
          self.evaluation[y-1] =  eval_pred_y
          if x > 0:
            self.evaluation[x-1] = eval_pred_x
          if y < (self.dim - 1):
            self.evaluation[y] = eval_suc_y

          if x== 0 or y == (self.dim - 1):
            self.evaluation[self.dim-1] = eval_fin

          self.eval = new_eval

          tmp = self.perm[x]
          self.perm[x] = self.perm[y]
          self.perm[y] = tmp

        return new_eval

    def get_eval(self):
        self.evaluate()
        return np.sum(self.evaluation)

    def any_change_neighbourhood(self):
        combinations = []
        # Add all posible swaps 2 by 2
        for i in range(self.dim):
            for j in range(i + 1, self.dim):
                combinations.append((i, j))
        return combinations

    def adjacent_neighbourhood(self):
        combinations = []
        # Add swaps between neighbours
        for i in range(self.dim - 1):
            combinations.append((i, i + 1))
        combinations.append((0, self.dim - 1))
        return combinations

    def apply_swap(self, coords):
        (x, y) = coords
        self.eval_swap(x, y, apply=True)

    def pretty_perm(self):
        str_sol = "["

        for i in range(5):
            str_sol += "{}, ".format(self.perm[i])
        str_sol += "..., "

        for i in range(5):
            str_sol += "{}, ".format(self.perm[i - 5])
        str_sol = str_sol[:-2] + "]"
        return str_sol

    def __str__(self):
        return "Evaluation: " + str(self.eval) \
        + "\nPermutation: " + self.pretty_perm()

    def __lt__(self, other):
        return self.eval < other.eval
