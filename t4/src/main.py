import sys
import arguments
import time
from Logger import Logger
from Population import Population
from Member import Member

def main(args):
    # Create Log
    log = Logger()
    best_list = [f'iter-best{i}' for i in range(args.best)] + ["best-avg"]
    log.add_dictionaries(best_list + ["iter-avg", "iter-best"])

    popargs = {
        "queens": args.queens,
        "maxiters": args.maxiters,
        "size": 3 * args.queens  if args.size == 0 else args.size,
        "mutation": args.mutation,
        "cross": args.cross,
        "log": log,
    }

    log.set_initial_pob(popargs["size"]).set_cross_prob(args.cross).set_mutation_prob(args.mutation)

    t1 = time.time()
    population = Population(**popargs)
    population.run()
    t2 = time.time()
    log.set_time(t2 - t1)

    # Define graphs data
    aux_labels = ["Segunda", "Tercera", "Cuarta", "Quinta", "Sexta", "Séptima"]
    best_list_labels = ["Mejor solución"] + [f'{aux_labels[j]} mejor solución' for j in range(args.best - 1)]
    f1args = {
        "title": "Comportamiento del algoritmo para N = " + str(args.queens),
        "xlabel": "Número de iteraciones",
        "ylabel": "Función fitness",
        "labels": best_list_labels + ["Promedio"],
        "id": "EvalFunctEvolM"
    }

    f2args = {
        "title": "Promedio para valores fitness",
        "xlabel": "Número de iteraciones",
        "ylabel": "Función fitness",
        "labels": [],
        "id": "AvgEvol"
    }

    f3args = {
        "title": "Comportamiento del algoritmo para N = " + str(args.queens),
        "xlabel": "Número de iteraciones",
        "ylabel": "Función fitness",
        "labels": [],
        "id": "EvalFunctEvol"
    }

    log.gen_graphs(best_list, **f1args) \
    .gen_graphs(["iter-avg"], **f2args) \
    .gen_graphs(["iter-best"], **f3args)

    if args.save: log.save(f'../ejecuciones/n{args.queens}results.txt', args.queens, args.graphs)
    else: log.show()

    if args.latex: population.as_latex()

main(arguments.defineArgs())
