import argparse

def defineArgs():
    parser = argparse.ArgumentParser(description='Simulated Annealing')

    parser.add_argument('-m', '--maxiter', help='number of max iterations',
        type=int, default=1000)

    parser.add_argument('-q', '--queens', help='number of queens', type=int,
        default=8)

    return parser.parse_args()
