import time
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.ticker as plticker
import numpy as np

class TSPLog:

    def __init__(self):
        self.data = {}
        self.ids = []

    def add_dict(self, name):
        self.data[name] = ([], [])
        return self

    def add_dictionaries(self, names):
        for name in names:
            self.data[name] = ([], [])
        return self

    def add_data(self, name, values):
        (v1, v2) = values
        (l1, l2) = self.data[name]
        l1.append(v1)
        l2.append(v2)
        return self

    def gen_graphs(self, names, title="", xlabel="", ylabel="", id=""):
        plt.figure(len(self.ids))
        plt.title(title, loc='left')
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)

        for name in names:
            (x, y) = self.data[name]
            plt.plot(x, y)
        self.ids.append(id)
        
        return self

    def show(self):
        plt.show()

    def save_graphs(self, path):
        figs = [plt.figure(n) for n in plt.get_fignums()]
        i = 0
        for fig in figs:
            date_time = datetime.now().strftime("%H%M%S")
            name = self.ids[i]
            plt.grid(which='major', color='#CCCCCC', linestyle='--')
            plt.grid(which='minor', color='#CCCCCC', linestyle=':')
            plt.minorticks_on()
            fig.set_size_inches((13, 7), forward=False)
            fig.savefig("{}/{}-{}".format(path, name, date_time))
            i += 1

        # results = open(path + "results.txt", "a")
        # results.write(f'{filename + date_time},{best_eval}')
