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

    for curr_i in range(instance.maxiters):
        print(curr_i, end='\r')
        test_vectors = []
        for (i, x_i) in enumerate(instance.population):
            v_i = instance.gen_mut_vect(i)

            u_i = instance.gen_test_vec(v_i, x_i)
            test_vectors.append(u_i)
            if instance.eval(u_i) < instance.eval(x_i):
                instance.population[i] = u_i

    for ind in instance.population:
        print(instance.eval(ind))



main(arguments.defineArgs())
