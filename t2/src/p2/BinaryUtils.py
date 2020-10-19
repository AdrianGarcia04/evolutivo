import numpy as np

def natural_to_bin(n):
    remstack = []
    while n > 0:
        rem = n % 2
        remstack.insert(0, rem)
        n = n // 2
    return remstack

def bin_to_gray(bin_array):
    result = [bin_array[0]]
    for i in range(1, len(bin_array)):
        result.append(bin_array[i-1] ^ bin_array[i])
    return result

def bin_to_natural(bin_array):
    result = 0
    for i in range(len(bin_array)):
        result += ((2**(len(bin_array) - i - 1) ) * bin_array[i])
    return result

def gray_to_bin(gray_array):
    bin_array = [None] * len(gray_array)
    bin_array[0] = gray_array[0]
    for i in range(1, len(gray_array)):
        bin_array[i] = gray_array[i] ^ bin_array[i-1]
    return bin_array

def rand_solution(num_bits):
    solution = [None] * num_bits
    for i in range(num_bits):
        solution[i] = np.random.randint(2)
    return solution

def generate_neighbourhood(solution):
    neighbours = [[]] * len(solution)
    for i in range(len(solution)):
        neighbours[i] = [1 - bit if pos == i else bit for (pos, bit) in enumerate(solution)]
    return neighbours

def real_to_bin_interval(real, m, cot_inf, cot_sup):
    return None
