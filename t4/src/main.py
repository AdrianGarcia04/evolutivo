import sys
import arguments
from Logger import Logger
from Genetics import Population

def main(args):
    population = Population(args.queens, args.maxiter)


main(arguments.defineArgs())
