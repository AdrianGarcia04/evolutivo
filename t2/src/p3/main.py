import numpy as np
import sys
import copy
from Instance import Instance
from Solution import Solution

def gen_random_solution(instance):
    # Creating a solution with a random permutation
    return Solution(instance, perm_random=True)

def gen_neighbourhood(solution, type=1):
    if type == 1: return solution.any_change_neighbourhood()
    elif type == 2: return solution.adjacent_neighbourhood()

def stochastic_search(instance, neighbourhood_type=2):
    # Set iterations
    iterations = 0
    # Get a random solution for the instance and its evaluation
    current_solution = gen_random_solution(instance)
    current_evaluation = current_solution.get_eval()

    # Set the best evaluation to infinite and solution as the actual one
    best_evaluation = float("inf")
    best_solution = current_solution

    while iterations < max_iterations:
        # We obtain the current solution neighbourhood
        neighbourhood = gen_neighbourhood(current_solution, type=neighbourhood_type)

        random_swap_index = np.random.choice(len(neighbourhood))
        random_swap = neighbourhood[random_swap_index]

        random_neighbour = copy.deepcopy(current_solution)
        random_neighbour.apply_swap(random_swap)

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
            acceptance_probability = np.exp(-(random_neighbour_eval - current_evaluation) / temperature)
            probability = np.random.uniform() * 100

            if probability < acceptance_probability:
                current_solution = random_neighbour

        iterations += 1

    return (best_solution, best_evaluation)

if __name__ == '__main__':
    file = sys.argv[1]
    max_iterations = int(sys.argv[2])
    temperature = int(sys.argv[3])
    neighbourhood_type = sys.argv[4]
    if neighbourhood_type == "anychange": neighbourhood_type = 1
    elif neighbourhood_type == "adjacent": neighbourhood_type = 2

    # Reading file
    instance = Instance.read_file(file)

    # Start Stochastic Search
    (best_solution, best_evaluation) = stochastic_search(instance, neighbourhood_type)

    print(best_solution)
