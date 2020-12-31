import argparse

def defineArgs():
    parser = argparse.ArgumentParser(description='Knapsack problem')

    parser.add_argument('-f', '--file', help='input file', type=str,
        default='4_11', choices=['4_11', '4_20', '5_80', '7_50', '10_60', \
                            '10_269', '15_375', '20_878', '20_879', '23_10000'])

    parser.add_argument('-m', '--maxiters', help='number of max iterations',
        type=int, default=1000)

    parser.add_argument('-p', '--size', help='population size', type=int,
        default=100)

    return parser.parse_args()
