import sys
import arguments
import time
from Logger import Logger
from Population import Population
from Member import Member

def main(args):
    # Create Log
    log = Logger()
    log.add_dictionaries(["iter-best", "iter-avg"])

    popargs = {
        "queens": args.queens,
        "maxiters": args.maxiters,
        "size": 3 * args.queens  if args.size == 0 else args.size,
        "mutation": args.mutation,
        "cross": args.cross,
        "log": log,
    }

    log.set_initial_pob(popargs["size"]).set_mutation_prob(args.mutation)

    t1 = time.time()
    population = Population(**popargs)
    population.run()
    t2 = time.time()
    log.set_time(t2 - t1)

    # Define graphs data
    f1args = {
        "title": "Comportamiento del algoritmo para N = " + str(args.queens),
        "xlabel": "Número de iteraciones",
        "ylabel": "Función fitness",
        "labels": [],
        "id": "EvalFunctEvol"
    }

    f2args = {
        "title": "Promedio para valores fitness",
        "xlabel": "Número de iteraciones",
        "ylabel": "Función fitness",
        "labels": [],
        "id": "AvgEvol"
    }

    log.gen_graphs(["iter-best"], **f1args).gen_graphs(["iter-avg"], **f2args)

    if args.save: log.save(f'../ejecuciones/n{args.queens}results.txt', args.queens, args.graphs)
    else: log.show()

    if args.latex: population.as_latex()

main(arguments.defineArgs())
