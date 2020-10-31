import numpy as np
import copy
from Instance import Instance
from Solution import Solution

class SimulatedAnnealing:

    def __init__(self, instance, args):
        (initial_tmp, cooling_type, constants, neighbourhood_type, max_iter) = args
        self.instance = instance
        self.initial_tmp = initial_tmp
        self.cooling_type = cooling_type
        self.constants = constants
        self.neighbourhood_type = neighbourhood_type
        self.max_iterations = max_iter

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
        # Set iterations
        iterations = 0
        # Get a random solution for the instance and its evaluation
        current_solution = self.gen_random_solution()
        current_evaluation = current_solution.get_eval()

        # Set the best evaluation to infinite and solution as the actual one
        best_evaluation = float("inf")
        best_solution = current_solution

        tmp = self.initial_tmp

        while iterations < self.max_iterations:
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

                # If it is the best so far, save it
                if random_neighbour_eval < best_evaluation:
                    best_evaluation = random_neighbour_eval
                    best_solution = random_neighbour
            else:
                # Accept solution with this probability
                acceptance_probability = np.exp(-(random_neighbour_eval - current_evaluation) / tmp)
                probability = np.random.uniform() * 100

                # Accepting
                if probability < acceptance_probability:
                    current_solution = random_neighbour

            tmp = self.alpha(tmp)
            iterations += 1
            self.constants["k"] = iterations

        return (best_solution, best_evaluation)
