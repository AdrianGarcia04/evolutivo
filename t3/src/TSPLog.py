import time
import matplotlib.pyplot as plt
import matplotlib.ticker as plticker
import numpy as np

class TSPLog:

    def __init__(self, arg):
        self.iterations = 0
        self.current_solution = None
        self.current_eval = float("inf")
        self.best_solution = None
        self.best_eval = float("inf")
        self.plt1_data_x = []
        self.plt1_data_y = []
        self.plt2_data_x = []
        self.plt2_data_y = []
        self.title = ""
        self.started_at = time.time()

    def new_current(self, new_solution, new_eval):
        self.current_solution = new_solution
        self.current_eval = new_eval

    def new_best(self, new_solution, new_eval):
        self.best_solution = new_solution
        self.best_eval = new_eval

    def tick(self):
        self.iterations += 1
        self.plt1_data_x.append(self.iterations)
        self.plt1_data_y.append(self.current_eval)
        self.plt2_data_x.append(self.iterations)
        self.plt2_data_y.append(self.best_eval)

    def set_title(self, title):
        self.title = title

    def plot(self):
        fig,ax=plt.subplots()

        (x_min, x_max) = self.x_interval
        (y_min, y_max) = self.y_interval
        x_major_ticks = np.arange(x_min, x_max, (x_max - x_min) * 0.05)
        x_minor_ticks = np.arange(y_min, y_max, (y_max - y_min) * 0.1)

        y_major_ticks = np.arange(x_min, x_max, (x_max - x_min) * 0.5)
        y_minor_ticks = np.arange(y_min, y_max, (y_max - y_min) * 0.25)

        ax.set_xticks(x_major_ticks)
        ax.set_xticks(x_minor_ticks, minor=True)
        # ax.set_yticks(y_major_ticks)
        # ax.set_yticks(y_minor_ticks, minor=True)

        plt.grid(which='major', color='#CCCCCC', linestyle='--')
        plt.grid(which='minor', color='#CCCCCC', linestyle=':')
        plt.minorticks_on()
        mng = plt.get_current_fig_manager()
        mng.full_screen_toggle()
        plt.plot(self.plt1_data_x, self.plt1_data_y)
        plt.plot(self.plt2_data_x, self.plt2_data_y)
        plt.title(self.title, loc='left')
        plt.xlabel("Número de iteraciones")
        plt.ylabel("Función de evaluación")
        plt.show()

    def set_intervals(self, x, y):
        self.x_interval = x
        self.y_interval = y

    def stop(self):
        stopped_at = time.time()
        execution_time = (self.started_at - stopped_at) * 1000
