from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.ticker as plticker
import numpy as np
import os
import re

class Logger:

    def __init__(self):
        self.data = {}
        self.simple_data = {}
        self.ids = []
        self.initial_tmp = 0
        self.final_tmp = 0
        self.best_eval = 0
        self.time = 0
        self.max_iters = 0

    def set_initial_temp(self, tmp):
        self.initial_tmp = tmp
        return self

    def set_final_temp(self, tmp):
        self.final_tmp = tmp
        return self

    def set_best_eval(self, best):
        self.best_eval = best
        return self

    def set_time(self, time):
        self.time = time
        return self

    def set_max_iters(self, max_iters):
        self.max_iters = max_iters
        return self

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

    def gen_graphs(self, names, title="", xlabel="", ylabel="", labels=[], id=""):
        plt.figure(len(self.ids))
        plt.title(title, loc='left')
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)

        for name in names:
            (x, y) = self.data[name]
            plt.plot(x, y)
        if labels:
            plt.legend(labels, loc='upper right')
        self.ids.append(id)

        return self

    def show(self):
        plt.show()

    def save(self, path, instance, save_graphs):
        figs = [plt.figure(n) for n in plt.get_fignums()]
        i = 0
        for fig in figs:
            date_time = datetime.now().strftime("%H%M%S")
            name = self.ids[i]
            plt.grid(which='major', color='#CCCCCC', linestyle='--')
            plt.grid(which='minor', color='#CCCCCC', linestyle=':')
            plt.minorticks_on()
            fig.set_size_inches((13, 7), forward=False)
            if save_graphs:
                fig.savefig("{}/{}-{}".format(path, name, date_time))
            i += 1

        results = open(path + "/results.txt", "a")
        results.write(f'{instance},{self.best_eval},{self.initial_tmp},{self.final_tmp},{self.time},{self.max_iters}\n')
        results.close()

    def save_in(self, data_name, filename, ext, fstline):
        filename_cp = filename
        if os.path.exists(filename + ext):
            cnt = 1
            filename_cp = filename + f'-{cnt}'
            while os.path.exists(filename_cp + ext):
                m = re.search(filename, filename_cp)
                filename_cp = m.group()
                cnt += 1
                filename_cp += f'-{cnt}'
        results = open(filename_cp + ext, "w")
        results.write(fstline)
        for (v1, v2) in zip(self.data[data_name][0], self.data[data_name][1]):
            results.write(f'{v1},{v2}\n')
        results.close()
