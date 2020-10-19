import numpy as np

class LocalSearch:
    def __init__(self, solution):
        self.solution = solution

    def any_change_neighbourhood(self, solution):
        combinations = []
        for i in range(solution.dim):
            for j in range(i + 1, solution.dim):
                combinations.append((i, j))
        return combinations
