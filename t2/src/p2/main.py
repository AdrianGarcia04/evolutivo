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
            acceptance_probability = np.exp(-(random_neighbour_eval - current_evaluation) / temperature)
            probability = np.random.uniform() * 100

            # Accepting
            if probability < acceptance_probability:
                current_solution = random_neighbour

        iterations += 1

    return (best_solution, best_evaluation)

if __name__ == '__main__':
    file = sys.argv[1]
    max_iterations = int(sys.argv[2])
    temperature = int(sys.argv[3])
    to_table = int(sys.argv[4])
    neighbourhood_type = sys.argv[5]
    if neighbourhood_type == "anychange": neighbourhood_type = 1
    elif neighbourhood_type == "adjacent": neighbourhood_type = 2

    # Reading file
    instance = Instance.read_file(file)

    # Start Stochastic Search
    (best_solution, best_evaluation) = stochastic_search(instance, neighbourhood_type)

    # If the user specifies to write the info to the table
    if to_table:
        to_table_file = sys.argv[6]
        table_file = open(to_table_file, "a")

        table_file.write("{},{},{},{},{}\n".format(file, max_iterations, temperature, \
            best_evaluation, best_solution.pretty_perm()))

        table_file.close()
    # Just print the solution
    else:
        print(best_solution)
