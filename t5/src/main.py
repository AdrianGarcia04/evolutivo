import sys
import arguments
import numpy as np
import time
from Instance import Instance

def main(args):
    # Reading file and creating instance problem
    kwargs = {"maxiters": args.maxiters, "pop_size": args.size}
    file = "./data/" + args.file
    instance = Instance.from_file(file, **kwargs)

    t1 = time.time()

    # Initial population
    instance.init()

    # Repeat
    for _ in range(args.maxiters):

        # Calculate frequencies
        instance.calc_frequencies()

        # Calculate joint frecuencies
        instance.calc_joint_frequencies()

        # Calculate mutual information
        instance.mutual_info()

        # Create chain model
        instance.calc_chain_model()

        # Sampling
        instance.sampling()

    t2 = time.time()

    ex_time = (t2 - t1) * 1000.0

    print(instance.best, instance.fitness(instance.best), f'{ex_time}s')

main(arguments.defineArgs())
