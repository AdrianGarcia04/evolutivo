import sys
import numpy as np

class Instance:

    def __init__(self, name="", num_items=0, wmax=0, items=[], maxiters=0, pop_size=0):

        self.name = ""
        self.num_items = int(num_items)
        self.wmax = int(wmax)
        self.items = items
        self.maxiters = maxiters
        self.pop_size = pop_size
        self.population = []
        self.best = None

    def from_file(file, maxiters=0, pop_size=0):
        remove_last = True if "large" in file else False

        file = open(file, "r")
        (num_items, wmax) = file.readline().strip().split(' ')

        items = []

        for line in file:
            items.append(line.strip().split(' '))

        if remove_last:
            items = items[:-1]

        kwargs = {
            "name" : file,
            "num_items": num_items,
            "wmax": wmax,
            "items": items,
            "maxiters": maxiters,
            "pop_size": pop_size
        }

        return Instance(**kwargs)

    def init(self):

        for _ in range(self.pop_size):
            self.population.append(list(np.random.randint(2, size=self.num_items)))

    def calc_frequencies(self):

        self.frequencies = []
        self.pop_size = len(self.population)

        for i in range(self.num_items):

            count = 0

            for ind in self.population:
                count += 1 if ind[i] else 0

            self.frequencies.append(count / self.pop_size)

    def calc_joint_frequencies(self):

        (rows, cols) = (self.num_items, self.num_items)
        joint_freq_true_true = np.zeros((rows, cols))
        joint_freq_false_false = np.zeros((rows, cols))

        joint_freq_true_false = np.zeros((rows, cols))
        joint_freq_false_true = np.zeros((rows, cols))
        
        for i in range(cols):
            for j in range(rows):

                if i == j:

                    joint_freq_true_true[i][j] = self.frequencies[i]
                    joint_freq_false_false[i][j] = 1 - self.frequencies[i]

                    joint_freq_true_false[i][j] = 0
                    joint_freq_false_true[i][j] = 0

                else:

                    joint_freq_true_true[i][j] = self.count((i, 1), (j, 1))
                    joint_freq_false_false[i][j] = self.count((i, 0), (j, 0))

                    joint_freq_true_false[i][j] = self.count((i, 1), (j, 0))
                    joint_freq_false_true[i][j] = self.count((i, 0), (j, 1))

        self.joint_freq_true_true = joint_freq_true_true
        self.joint_freq_false_false = joint_freq_false_false

        self.joint_freq_true_false = joint_freq_true_false
        self.joint_freq_false_true = joint_freq_false_true

    def count(self, i_val, j_val):

        (i, bool_i) = i_val
        (j, bool_j) = j_val
        count = 0

        for ind in self.population:
            if ind[i] == bool_i and ind[j] == bool_j:
                count += 1

        return count / self.pop_size

    def mutual_info(self):

        mutual_table = np.zeros((self.num_items, self.num_items))

        for i in range(self.num_items):
            for j in range(self.num_items):

                if i == j:
                    mutual_table[i][j] = 0

                else:

                    true_true = self.joint_freq_true_true[i][j]
                    false_false = self.joint_freq_false_false[i][j]

                    true_false = self.joint_freq_true_false[i][j]
                    false_true = self.joint_freq_false_true[i][j]

                    i_true = self.frequencies[i]
                    i_false = 1 - self.frequencies[i]

                    j_true = self.frequencies[j]
                    j_false = 1 - self.frequencies[j]

                    if (i_false * j_false) == 0:
                        l1 = 0
                    else: 
                        l1 = false_false / (i_false * j_false)

                    if (i_false * j_true) == 0:
                        l2 = 0
                    else: 
                        l2 = false_true / (i_false * j_true)

                    if (i_true * j_false) == 0:
                        l3 = 0
                    else: 
                        l3 = true_false / (i_true * j_false)

                    if (i_true * j_true) == 0:
                        l4 = 0
                    else: 
                        l4 = true_true / (i_true * j_true)

                    #########################

                    if l1 == 0:
                        p1 = 0
                    else: 
                        p1 = false_false * np.log10(l1)

                    if l2 == 0:
                        p2 = 0
                    else: 
                        p2 = false_true * np.log10(l2)

                    if l3 == 0:
                        p3 = 0
                    else: 
                        p3 = true_false * np.log10(l3)

                    if l4 == 0:
                        p4 = 0
                    else: 
                        p4 = true_true * np.log10(l4)

                    mutual_table[i][j] = p1 + p2 + p3 + p4
                    mutual_table[j][i] = p1 + p2 + p3 + p4

        self.mutual_table = mutual_table

    def calc_chain_model(self):

        rng_items = range(self.num_items)

        (max_i, max_j, max_mutual) = self.get_max_mutual(rng_items, rng_items)
        chain_model = [max_i, max_j]
        chain_model = list(set(chain_model))


        while len(chain_model) != self.num_items:

            fst = chain_model[0]
            lst = chain_model[-1]
            mejor_izq_i = mejor_der_i = -1
            mejor_izq_v = mejor_der_v = -1
            diff = self.list_diff(chain_model, list(rng_items))

            for xi in diff:

                if self.mutual_table[xi][fst] > mejor_izq_v:
                    mejor_izq_i = xi
                    mejor_izq_v = self.mutual_table[xi][fst]

                if self.mutual_table[lst][xi] > mejor_der_v:
                    mejor_der_i = xi
                    mejor_der_v = self.mutual_table[lst][xi]


            if max(mejor_izq_v, mejor_der_v) == mejor_izq_v:
                chain_model.insert(0, mejor_izq_i)
            else:
                chain_model.append(mejor_der_i)


        self.chain_model = chain_model

    def list_diff(self, l1, l2):
        return (list(list(set(l1)-set(l2)) + list(set(l2)-set(l1))))

    def get_max_mutual(self, i_range, j_range):

        max_mutual = max_i = max_j = 0

        for i in i_range:
            for j in j_range:

                if self.mutual_table[i][j] > max_mutual:
                    max_mutual = self.mutual_table[i][j]
                    max_i = i
                    max_j = j

        return (max_i, max_j, max_mutual)

    def sampling(self):

        probabilities = []
        prev_var = None

        for var in self.chain_model:

            if prev_var == None:

                true_true = self.joint_freq_true_true[var][var]
                probabilities.append([1 - true_true, true_true])

            else:

                var_marg_false = self.joint_freq_false_false[prev_var][prev_var]
                var_marg_true = self.joint_freq_true_true[prev_var][prev_var]
                
                true_false = self.joint_freq_true_false[var][prev_var]
                true_true = self.joint_freq_true_true[var][prev_var]

                pfalse = 0
                if var_marg_false != 0:
                    pfalse = true_false / var_marg_false

                ptrue = 0
                if var_marg_true != 0:
                    ptrue = true_true / var_marg_true
                
                var_probs = [pfalse, ptrue]
                probabilities.append(var_probs)

            prev_var = var

        new_population = []

        for _ in range(self.pop_size):

            ind = [0] * self.num_items
            prev_res = None

            for i, var in enumerate(self.chain_model):

                if prev_res == None:

                    r = np.random.rand()
                    p = probabilities[i][1]
                    ind[var] = 1 if r < p else 0

                else:

                    r = np.random.rand()
                    p = probabilities[i][prev_res]
                    ind[var] = 1 if r < p else 0

                prev_res = ind[var]

            new_population.append(ind)

        pop_fitness = []
        best = None
        best_fitness = 0

        for ind in new_population:
            fitness = self.fitness(ind)
            pop_fitness.append(fitness)
            if fitness >= best_fitness:
                best = ind

        avg = np.average(pop_fitness)

        self.population = [best]
        if self.best == None or self.fitness(self.best) < self.fitness(best):
            self.best = best

        new_population.remove(best)

        for i, ind in enumerate(new_population):

            if pop_fitness[i] >= avg:
                self.population.append(ind)

    def fitness(self, ind):

        total_value = total_weight = 0

        for i, item in enumerate(self.items):

            if ind[i]:
                total_value += int(item[0])
                total_weight += int(item[1])

        if total_weight > self.wmax:
            return 0
        else:
            return total_value






