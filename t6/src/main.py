import arguments
import numpy as np
import timeit
from Instance import Instance

def execute(instance):
    while instance.not_term():
        test_vectors = []
        for (i, x_i) in enumerate(instance.population):
            v_i = instance.gen_mut_vect(i)

            u_i = instance.gen_test_vec(v_i, x_i)
            test_vectors.append(u_i)
            if instance.eval_ind(u_i) < instance.eval_ind(x_i):
                instance.population[i] = u_i

def main(args):
    kwargs = {
        "funct": args.function,
        "maxevals": args.maxevals,
        "size": args.size,
        "cross": args.cross,
        "scale": args.scale,
        "dim": args.dim,
    }
    global instance

    instance = Instance(**kwargs)
    execution_time = timeit.timeit("execute(instance)", globals=globals())
    evals = instance.num_evals

    best = None
    best_eval = 10000
    for ind in instance.population:
        ev = instance.eval_ind(ind)
        if ev < best_eval:
            best = ind

    print(f'{args.function},{args.dim},{args.cross},{args.scale},{args.size},{evals},{execution_time},{instance.eval_ind(ind)}')

main(arguments.defineArgs())
