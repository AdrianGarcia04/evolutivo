import sys
from BinaryUtils import *
from Solution import Solution

if __name__ == '__main__':
    funct = sys.argv[1]
    dim = int(sys.argv[2])
    m_bits = int(sys.argv[3])
    codification = sys.argv[4]
    to_table = int(sys.argv[5])

    as_gray = True if codification == "Gray" else False

    # Create random solution of given dimension, given number of bits under the
    # specified funct
    sol = Solution(dim, m_bits, funct, as_gray=as_gray)
    # Consider it the best evaluation so far
    (best_eval, _) = sol.eval(sol.vect)
    has_improvement = True
    i = 0
    while has_improvement:
        i += 1
        has_improvement = False
        # Find the neighbour with best evaluation, if exists
        (found_eval, found_sol) = sol.explore_neighbourhood()
        # If the evaluation is better, take it and restart
        # If not, finish
        if found_eval < best_eval:
            best_eval = found_eval
            sol.set_vect(found_sol)
            has_improvement = True

    # If the user specifies to write the info to the table
    if to_table:
        to_table_file = sys.argv[6]
        table_file = open(to_table_file, "a")

        table_file.write("{},{},{},{},{},{},{}\n".format(funct, dim, i, \
            codification, m_bits, best_eval, sol.get_values()))

        table_file.close()
    # Just print the best solution
    else:
        print(sol)
