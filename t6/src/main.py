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

main(arguments.defineArgs())
