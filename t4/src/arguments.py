import argparse

def defineArgs():
    parser = argparse.ArgumentParser(description='8-Queens Problem')

    parser.add_argument('-m', '--maxiters', help='number of max iterations',
        type=int, default=1000)

    parser.add_argument('-q', '--queens', help='number of queens', type=int,
        default=8)

    parser.add_argument('-p', '--size', help='population size', type=int,
        default=0)

    parser.add_argument('-x', '--mutation', help='mutation probability', type=float,
        default=0.5)

    parser.add_argument('-c', '--cross', help='crossing probability', type=float,
        default=0.9)

    parser.add_argument('-s', '--save', help='whether or not save the results',
        action='store_true')

    parser.add_argument('-g', '--graphs', help='whether or not save the graphs',
        action='store_true')

    parser.add_argument('-l', '--latex', help='print latex codification',
        action='store_true')

    parser.add_argument('-b', '--best', help='graph b bests', type=int,
        default=3)

    return parser.parse_args()
