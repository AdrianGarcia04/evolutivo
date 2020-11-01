import time
import matplotlib.pyplot as plt

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

    def plot(self):
        plt.tight_layout()
        mng = plt.get_current_fig_manager()
        mng.full_screen_toggle()
        plt.plot(self.plt1_data_x, self.plt1_data_y)
        plt.plot(self.plt2_data_x, self.plt2_data_y)
        plt.show()

    def stop(self):
        stopped_at = time.time()
        execution_time = (self.started_at - stopped_at) * 1000
