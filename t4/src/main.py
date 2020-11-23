import sys
import arguments
from Logger import Logger
from Population import Population
from Member import Member

def main(args):
    popargs = {
        "queens": args.queens,
        "maxiters": args.maxiters,
        "size": 3 * args.queens  if args.size == 0 else args.size,
    }
    population = Population(**popargs)
    population.run()
    population.as_latex()

main(arguments.defineArgs())
