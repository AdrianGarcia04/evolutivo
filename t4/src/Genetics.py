import numpy as np
from itertools import tee

def pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

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

def cross(f1, f2):
    cut_point = np.random.randint(f1.size)
    queens = f1.size

    gen1 = list(f1.gen[0:cut_point]) + list(f2.gen[cut_point:])
    gen2 = list(f2.gen[0:cut_point]) + list(f1.gen[cut_point:])
    return (Member(queens, gen=gen1), Member(queens, gen=gen2))

class Population:

    def __init__(self, queens=8, maxiters=100, size=10):
        self.queens = queens
        self.max_iters = maxiters
        self.size = size
        self.population = [Member(queens) for _ in range(size)]

    def run(self):
        i = 0
        while i < self.max_iters:
            fathers = self.select_fathers()
            new_members = self.gen_new_members(fathers)
            self.mutate(new_members)
            self.replace(new_members)
            i += 1
            print("Percentage {}%".format(i * 100 // self.max_iters), end="\r")
        self.population = sorted(self.population, key=lambda x: x.fitness)
        print(self.population[0])

    def select_fathers(self):
        return self.tournament(len(self.population) // 2)

    def gen_new_members(self, fathers):
        new_members = []
        for f1, f2 in pairwise(fathers):
            m1, m2 = cross(f1, f2)
            new_members.append(m1)
            new_members.append(m2)
        m1, m2 = cross(fathers[-1], fathers[0])
        new_members.append(m1)
        new_members.append(m2)
        return new_members

    def mutate(self, new_members):
        for member in new_members:
            if np.random.uniform() <= 0.3:
                rand_index = np.random.randint(member.size)
                member.gen[rand_index] = np.random.randint(member.size)

    def replace(self, new_members):
        self.population = sorted(self.population, key=lambda x: x.fitness)
        new_pop = [self.population[0]]
        new_pop += new_members

    def tournament(self, select, num_contestants=2):
        fathers = []
        for _ in range(select):
            contestants = np.random.choice(self.population, size=num_contestants)
            contestants = sorted(contestants, key=lambda x: x.fitness)
            fathers.append(contestants[0])
        return fathers
