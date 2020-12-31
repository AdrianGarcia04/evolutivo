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

    def from_file(file, maxiters=0, pop_size=0):
        file = open(file, "r")
        (num_items, wmax) = file.readline().strip().split(' ')

        items = []
        for line in file:
            items.append(line.strip().split(' '))

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

    def frequencies(self):
        self.frequencies = []
        for i in range(self.num_items):
            count = 0
            for ind in self.population:
                count += 1 if ind[i] else 0
            self.frequencies.append(count / self.pop_size)

    def joint_frequencies(self):
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

                    l1 = false_false / (i_false * j_false)
                    l2 = false_true / (i_false * j_true)
                    l3 = true_false / (i_true * j_false)
                    l4 = true_true / (i_true * j_true)

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
