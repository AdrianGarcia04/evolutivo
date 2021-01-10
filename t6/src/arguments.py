import argparse

def defineArgs():
    parser = argparse.ArgumentParser(description='Knapsack problem')

    parser.add_argument('-f', '--function', help='function to use', type=str,
        default='sphere', choices=['sphere', 'ackley', 'griewank', 'rastrigin', 'rosenbrock'])

    parser.add_argument('-m', '--maxiters', help='number of max iterations',
        type=int, default=10000)

    parser.add_argument('-s', '--size', help='population size',
        type=int, default=100)

    parser.add_argument('-cr', '--cross', help='cross probability',
        type=float, default=0.9)

    parser.add_argument('-sc', '--scale', help='cross probability',
        type=float, default=0.7)

    parser.add_argument('-d', '--dim', help='dimension',
        type=int, default=10)

    return parser.parse_args()
