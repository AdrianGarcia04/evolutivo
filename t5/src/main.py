import sys
import arguments
import numpy as np
from Instance import Instance

def main(args):
    # Reading file and creating instance problem
    kwargs = {"maxiters": args.maxiters, "pop_size": args.size}
    file = "./data/" + args.file
    instance = Instance.from_file(file, **kwargs)

    # Initial population
    instance.init()

    # Repeat
    # for _ in range(args.maxiters):

    # Calculate frequencies
    instance.frequencies()

    # Calculate joint frecuencies
    instance.joint_frequencies()

    # Calculate mutual information

    # Create chain model

    # Sampling

main(arguments.defineArgs())
