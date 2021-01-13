import arguments
import numpy as np
from Instance import Instance

def main(args):
    kwargs = {
        "funct": args.function,
        "maxevals": args.maxevals,
        "size": args.size,
        "cross": args.cross,
        "scale": args.scale,
        "dim": args.dim,
    }
    instance = Instance(**kwargs)

    curr_i = 0
    while instance.not_term():
        print(curr_i, instance.num_evals, end='\r')
        test_vectors = []
        for (i, x_i) in enumerate(instance.population):
            v_i = instance.gen_mut_vect(i)

            u_i = instance.gen_test_vec(v_i, x_i)
            test_vectors.append(u_i)
            if instance.eval_ind(u_i) < instance.eval_ind(x_i):
                instance.population[i] = u_i
        curr_i += 1

    best = None
    best_eval = 10000
    for ind in instance.population:
        ev = instance.eval_ind(ind)
        if ev < best_eval:
            best = ind
    print(best, instance.eval_ind(ind), int(instance.eval_ind(ind)))

main(arguments.defineArgs())
