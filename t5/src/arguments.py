import argparse

def defineArgs():
    parser = argparse.ArgumentParser(description='Knapsack problem')

    parser.add_argument('-f', '--file', help='input file',
        type=str, default='low/4_11')

    parser.add_argument('-m', '--maxiters', help='number of max iterations',
        type=int, default=1000)

    parser.add_argument('-s', '--size', help='population size', type=int,
        default=10)

    return parser.parse_args()
