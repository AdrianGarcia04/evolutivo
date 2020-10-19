import numpy as np
import sys
import copy
from Instance import Instance
from Solution import Solution

def gen_random_solution(instance):
    return Solution(instance, perm_random=True)

def eval_solution(solution):
    return solution.get_eval()

def gen_neighbourhood(solution, type=1):
    if type == 1:
        return solution.any_change_neighbourhood()
    elif type == 2:
        return solution.adjacent_neighbourhood()

def stochastic_search(instance):
    iterations = 0
    current_solution = gen_random_solution(instance)
    current_evaluation = eval_solution(current_solution)

    best_evaluation = float("inf")

    while iterations < max_iterations:
        neighbourhood = gen_neighbourhood(current_solution, type=1)

        random_swap_index = np.random.choice(len(neighbourhood))
        random_swap = neighbourhood[random_swap_index]

        random_neighbour = copy.deepcopy(current_solution)
        random_neighbour.apply_swap(random_swap)

        random_neighbour_eval = eval_solution(random_neighbour)

        if random_neighbour_eval < current_evaluation:
            current_solution = random_neighbour

            if random_neighbour_eval < best_evaluation:
                best_evaluation = random_neighbour_eval
        else:
            acceptance_probability = np.exp(-(random_neighbour_eval - current_evaluation) / temperature)
            probability = np.random.uniform() * 100

            if probability < acceptance_probability:
                current_solution = random_neighbour

        iterations += 1

    print(best_evaluation)


if __name__ == '__main__':
    file = sys.argv[1]
    max_iterations = int(sys.argv[2])
    temperature = int(sys.argv[3])

    tspInstance = Instance.read_file(file)

    stochastic_search(tspInstance)
