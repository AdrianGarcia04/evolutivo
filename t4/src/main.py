import sys
import arguments
from Logger import Logger

def main(args):
    print(args.queens, args.maxiter)

main(arguments.defineArgs())
