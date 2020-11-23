import numpy as np
from itertools import tee
from Member import Member

def pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

def cross(f1, f2):
    cut_point = np.random.randint(f1.size)
    queens = f1.size

    gen1 = list(f1.gen[:cut_point]) + list(f2.gen[cut_point:])
    gen2 = list(f2.gen[:cut_point]) + list(f1.gen[cut_point:])
    return (Member(queens, gen=gen1), Member(queens, gen=gen2))

class Population:

    def __init__(self, queens=8, maxiters=100, size=10, mutation=0.3, cross=0.9, log=None):
        self.queens = queens
        self.max_iters = maxiters
        self.size = size
        self.population = [Member(queens) for _ in range(size)]
        self.mutation_prob = mutation
        self.cross_prob = cross
        self.log = log

    def sort_population(self):
        self.population = sorted(self.population, key=lambda x: x.fitness)

    def eval(self):
        for member in self.population:
            member.update_fitness()

    def run(self):
        i = 0
        while i < self.max_iters:
            fathers = self.select_fathers()
            new_members = self.gen_new_members(fathers)
            self.mutate(new_members)
            self.replace(new_members)
            self.eval()
            self.sort_population()
            i += 1

            best_fit = self.population[0].fitness
            self.log.add_data("iter-best", (i, best_fit))

            fitness_avg = np.average([m.fitness for m in self.population])
            self.log.add_data("iter-avg", (i, fitness_avg))

            if best_fit == 0:
                break

            print(f'Percentage {i * 100 // self.max_iters}%', end="\r")

        final_pob_len = len(self.population)
        best_fit = self.population[0].fitness

        self.log.set_final_pob(final_pob_len).set_best_fit(best_fit).set_max_iters(i)
        print(self.population[0])

    def select_fathers(self):
        return self.tournament(len(self.population) // 2)

    def gen_new_members(self, fathers):
        new_members = []
        for f1, f2 in pairwise(fathers):
            if np.random.uniform() <= self.cross_prob:
                m1, m2 = cross(f1, f2)
            else:
                m1, m2 = f1, f2
            new_members.append(m1)
            new_members.append(m2)
        m1, m2 = cross(fathers[-1], fathers[0])
        new_members.append(m1)
        new_members.append(m2)
        return new_members

    def mutate(self, new_members):
        for member in new_members:
            if np.random.uniform() <= self.mutation_prob:
                rand_index = np.random.randint(member.size)
                member.gen[rand_index] = np.random.randint(member.size)

    def replace(self, new_members):
        self.sort_population()
        new_pop = [self.population[0]]
        new_pop += new_members
        self.population = new_pop

    def tournament(self, select, num_contestants=2):
        fathers = []
        for _ in range(select):
            contestants = np.random.choice(self.population, size=num_contestants)
            contestants = sorted(contestants, key=lambda x: x.fitness)
            fathers.append(contestants[0])
        return fathers

    def as_latex(self):
        self.sort_population()
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
        'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        q = self.queens
        fen_pos = ""

        for (i, pos) in enumerate(self.population[0].gen):
            fen_pos += f'Q{letters[i]}{q - pos},'
        fen_pos = fen_pos[:-1]
        maxfield = f'{letters[q - 1]}{q}'
        print(f'\\storechessboardstyle{{{q}x{q}}}{{maxfield={maxfield}}}')
        print(f'\\chessboard[style={q}x{q},setwhite={{{fen_pos}}},showmover=false]')
