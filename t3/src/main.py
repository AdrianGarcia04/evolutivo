import sys
import copy
import numpy as np
import arguments
from TSPLog import TSPLog
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
    file = "../data/" + args.file + ".tsp"
    instance = Instance.read_file(file)

    # Create Log
    log = TSPLog()
    log.add_dictionaries(["eval-vs-iter", "best-vs-iter", "act-vs-ini", "best-vs-act"])

    # Start Stochastic Search
    simargs = {
        "inittmp": args.temp,
        "ctype": args.cooling,
        "cts": constants,
        "ntype": args.neightype,
        "miter": args.maxiter
    }
    SimulatedAnnealing(instance, log, **simargs).search()

    # Define graphs data
    f1args = {
        "title": "Función de evaluación " + args.file,
        "xlabel": "Número de iteraciones",
        "ylabel": "Función de evaluación",
        "labels": ["Solución actual", "Mejor solución encontrada"],
        "id": "EvalFunctEvol"
    }

    f2args = {
        "title": "Solución inicial vs solución actual " + args.file,
        "xlabel": "Número de iteraciones",
        "ylabel": "Diferencia",
        "labels": [],
        "id": "SolInivsActSol"
    }

    f3args = {
        "title": "Mejor solución vs solución actual " + args.file,
        "xlabel": "Número de iteraciones",
        "ylabel": "Diferencia",
        "labels": [],
        "id": "BestSolvsActSol"
    }

    log.gen_graphs(["eval-vs-iter", "best-vs-iter"], **f1args) \
    .gen_graphs(["act-vs-ini"], **f2args) \
    .gen_graphs(["best-vs-act"], **f3args)

    if args.save: log.save("../ejecuciones/" + args.file, args.file, args.graphs)
    else: log.show()

    if args.save:
        filename = "../ejecuciones/" + args.file + "/withtemps/evalwithtemp" + str(args.temp)
        ext = ".txt"
        fstline = "Iteración,Función de evaluación\n"
        log.save_in("eval-vs-iter", filename, ext, fstline)

main(arguments.defineArgs())
