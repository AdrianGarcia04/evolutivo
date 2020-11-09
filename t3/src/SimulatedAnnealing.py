import numpy as np
import copy
import time
from Instance import Instance
from Solution import Solution
from TSPLog import TSPLog

class SimulatedAnnealing:

    def __init__(self, instance, log, inittmp=0, ctype="", cts=None, ntype="", miter=0):
        self.instance = instance
        self.log = log
        self.initial_tmp = inittmp
        self.cooling_type = ctype
        self.constants = cts
        self.neighbourhood_type = ntype
        self.max_iterations = miter

    def gen_random_solution(self):
        # Creating a solution with a random permutation
        return Solution(self.instance, perm_random=True)

    def gen_neighbourhood(self, solution, type):
        if type == 'anychange': return solution.any_change_neighbourhood()
        elif type == 'adjacent': return solution.adjacent_neighbourhood()

    def alpha(self, t_k):
        if self.cooling_type == "linear": return self.initial_tmp - self.constants["eta"] * t_k
        elif self.cooling_type == "log": return self.constants["c"] / (1 + np.log(self.constants["k"]))
        elif self.cooling_type == "slow": return t_k / (1 + self.constants["beta"] * t_k)
        elif self.cooling_type == "geo": return self.constants["alpha"] * t_k

    def search(self):
        t1 = time.time()

        iterations = 0
        # Get a random solution for the instance
        current_solution = self.gen_random_solution()
        current_evaluation = current_solution.get_eval()
        initial_eval = current_evaluation

        # Set the best evaluation to infinite and solution as the actual one
        best_evaluation = float("inf")
        best_solution = current_solution

        tmp = self.initial_tmp
        self.log.set_initial_temp(tmp)

        while iterations < self.max_iterations:
            current_evaluation = current_solution.get_eval()
            # We obtain the current solution neighbourhood
            neighbourhood = self.gen_neighbourhood(current_solution, self.neighbourhood_type)

            # Select one random swap
            random_swap_index = np.random.choice(len(neighbourhood))
            random_swap = neighbourhood[random_swap_index]

            # Create the random neighbour applying the swap
            random_neighbour = copy.deepcopy(current_solution)
            random_neighbour.apply_swap(random_swap)

            # We evaluate the neighbour
            random_neighbour_eval = random_neighbour.get_eval()

            # If we find a better solution, take it
            if random_neighbour_eval < current_evaluation:
                current_solution = random_neighbour
                self.log.add_data("eval-vs-iter", (iterations, random_neighbour_eval))

                # If it is the best so far, save it
                if random_neighbour_eval < best_evaluation:
                    best_evaluation = random_neighbour_eval
                    best_solution = random_neighbour
                    self.log.add_data("best-vs-iter", (iterations, random_neighbour_eval))
            else:
                # Accept solution with this probability
                acceptance_probability = np.exp(-(random_neighbour_eval - current_evaluation) / tmp)
                probability = np.random.uniform()

                # Accepting
                if probability < acceptance_probability:
                    current_solution = random_neighbour
                    self.log.add_data("eval-vs-iter", (iterations, random_neighbour_eval))

            tmp = self.alpha(tmp)
            iterations += 1
            self.constants["k"] = iterations
            self.log.add_data("act-vs-ini", (iterations, initial_eval - random_neighbour_eval))
            self.log.add_data("best-vs-act", (iterations, current_evaluation - best_evaluation))
            print("Percentage {}%".format(iterations * 100 // self.max_iterations), end="\r")

        t2 = time.time()
        self.log.set_final_temp(tmp).set_best_eval(best_evaluation).set_time(t2 - t1)
        self.log.add_data("best-vs-iter", (self.max_iterations, best_evaluation))
        return (best_solution, best_evaluation)
