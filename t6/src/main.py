import arguments
import numpy as np
from Instance import Instance

def main(args):
    kwargs = {
        "funct": args.function,
        "maxiters": args.maxiters,
        "size": args.size,
        "cross": args.cross,
        "scale": args.scale,
        "dim": args.dim,
    }
    instance = Instance(**kwargs)

    for i in range(instance.maxiters):
        v_i = instance.generate_test_vect(i)

main(arguments.defineArgs())
