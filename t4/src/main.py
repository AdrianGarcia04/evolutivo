import sys
import arguments
from Logger import Logger
from Genetics import Population

def main(args):
    popargs = {
        "queens": args.queens,
        "maxiters": args.maxiters,
        "size": args.size,
    }
    population = Population(**popargs)

    population.run()

main(arguments.defineArgs())
