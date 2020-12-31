import numpy as np

def create_board(n):
    return np.zeros((n, n), dtype=int)

def fill_board(board, gen):
    for (i, pos) in enumerate(gen):
        board[pos][i] = 1
    return board

class Member:

    def __init__(self, queens, gen=None):
        self.size = queens
        if gen is not None:
            self.gen = gen
        else:
            self.gen = np.random.randint(queens, size=queens)
        self.fitness = self.get_fitness()

    def update_fitness(self):
        self.fitness = self.get_fitness()

    def get_fitness(self):
        hits = 0
        board = fill_board(create_board(self.size), self.gen)
        col = 0
        for queen in self.gen:
            try:
                for i in range(col - 1, -1, -1):
                    if board[queen][i] == 1:
                        hits += 1
            except IndexError:
                pass
            for i, j in zip(range(queen - 1, -1, -1), range(col - 1, -1, -1)):
                if board[i][j] == 1:
                    hits += 1
            for i, j in zip(range(queen + 1, self.size, 1), range(col - 1, -1, -1)):
                if board[i][j] == 1:
                    hits += 1
            col += 1
        return hits

    def __str__(self):
        return f'Gen: {self.gen}, Fitness: {self.fitness}'
