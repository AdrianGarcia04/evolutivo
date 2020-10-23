import sys
from BinaryUtils import *
from Solution import Solution

if __name__ == '__main__':
    funct = sys.argv[1]
    dim = int(sys.argv[2])
    m_bits = int(sys.argv[3])

    sol = Solution(dim, m_bits, funct)
    (best_eval, _) = sol.eval(sol.vect)
    has_improvement = True
    i = 0
    while has_improvement:
        i += 1
        has_improvement = False
        (found_eval, found_sol) = sol.explore_neighbourhood()
        print("Iter {} Eval {}".format(i, found_eval))
        if found_eval < best_eval:
            best_eval = found_eval
            sol.set_vect(found_sol)
            has_improvement = True
