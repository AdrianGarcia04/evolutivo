import argparse

def defineArgs():
    parser = argparse.ArgumentParser(description='Simulated Annealing')

    parser.add_argument('-f', '--file', help='input file', type=str,
        default='pbl395', choices=['a280', 'ch130', 'pbl395', 'xqf131', 'xqg237'])

    parser.add_argument('-m', '--maxiter', help='number of max iterations',
        type=int, default=1000)

    parser.add_argument('-t', '--temp', help='initial temperature', type=int,
        default=10000)

    parser.add_argument('-s', '--save', help='whether or not save the results',
        action='store_true')

    parser.add_argument('-o', '--output', help='output file', type=str,
        default='results.txt')

    parser.add_argument('-n', '--neightype',
        help='specifies which neighbourhood generation method to use',
        type=str, default='adjacent', choices=['adjacent', 'anychange'])

    parser.add_argument('-c', '--cooling', help='specifies which cooling method to use',
        type=str, default='slow')

    parser.add_argument('-a', '--alpha', help='specifies alpha value',
        type=float, default=0.9)

    parser.add_argument('-b', '--beta', help='specifies beta value',
        type=float, default=0.0001)

    parser.add_argument('-e', '--eta', help='specifies eta value',
        type=float, default=0.8)

    parser.add_argument('-cv', '--cvalue', help='specifies c value',
        type=float, default=1.0)

    parser.add_argument('-k', '--kvalue', help='specifies k value',
        type=float, default=1.0)

    return parser.parse_args()
