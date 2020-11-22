import numpy as np

def create_board(n):
    return np.zeros((n, n), dtype=int)

def fill_board(board, gen):
    for (i, pos) in enumerate(gen):
        board[pos][i] = 1
    return board

class Member:

    def __init__(self, queens):
        self.size = queens
        self.gen = np.random.randint(queens, size=queens)

    def fitness(self):
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

class Population:

    def __init__(self, queens=8, maxiters=100, size=10):
        self.queens = queens
        self.max_iters = maxiters
        self.size = size
        self.population = [Member(queens) for _ in range(size)]
