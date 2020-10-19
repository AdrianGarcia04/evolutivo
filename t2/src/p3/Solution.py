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

        if perm is not None:
            self.perm = np.array(perm)
        elif perm_random:
            self.rand_sol()

        self.distances = instance.distances
        self.evaluation = np.zeros(self.dim, dtype="float64")

        if to_eval:
            self.evaluate()

    def init_rand_sol(instance):
        return Solution(instance, perm_random=True, to_eval=False)

    def rand_sol(self):
        self.perm = np.random.permutation(self.dim)

    def evaluate(self):
        self.eval = 0
        nodes = self.instance.nodes
        for i in range(self.dim - 1):
            self.evaluation[i] = self.distances[self.perm[i]][self.perm[i + 1]]
            self.eval += self.evaluation[i]
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

    def print_genes(self, genes, to_print=True):
        strSol = str(genes[0:5]) + "..." \
        + str(genes[(self.dim - 5):(self.dim)])
        if to_print: print(strSol)
        return strSol

    def any_change_neighbourhood(self):
        combinations = []
        for i in range(self.dim):
            for j in range(i + 1, self.dim):
                combinations.append((i, j))
        return combinations

    def adjacent_neighbourhood(self):
        combinations = []
        for i in range(self.dim - 1):
            combinations.append((i, i + 1))
        combinations.append((0, self.dim - 1))
        return combinations

    def apply_swap(self, coords):
        (x, y) = coords
        self.eval_swap(x, y, apply=True)

    def __str__(self):
        return "Eval: " + str(self.eval) \
        + ", perm: " + self.print_genes(self.perm, to_print=False)

    def __lt__(self, other):
        return self.eval < other.eval
