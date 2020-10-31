import sys
import copy
import numpy as np
import arguments
from Instance import Instance
from Solution import Solution
from SimulatedAnnealing import SimulatedAnnealing

def main(args):
    constants = {
        "alpha": args.alpha,
        "beta": args.beta,
        "eta": args.eta,
        "c": args.cvalue,
        "k": args.kvalue
    }

    # Reading file
    instance = Instance.read_file(args.file)

    tup = (args.temp, args.cooling, constants, args.neightype, args.maxiter)

    # Start Stochastic Search
    sim_annealing = SimulatedAnnealing(instance, tup)
    (best_solution, best_evaluation) = sim_annealing.search()

    # If the user specifies to write the info to the table
    if args.save:
        table_file = open(args.output, "a")

        table_file.write("{},{},{},{},{}\n".format(args.file, args.maxiter, args.temp, \
            best_evaluation, best_solution.pretty_perm()))

        table_file.close()
    # Just print the solution
    else:
        print(best_solution)

main(arguments.defineArgs())
