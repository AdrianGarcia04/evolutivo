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

def real_to_bin_interval(real, n_bits, cot_inf, cot_sup):
    if real < cot_inf: return fill_zeros(n_bits, [0])
    if real > cot_sup: return natural_to_bin(2 ** n_bits - 1)
    delta = (cot_sup - cot_inf) / (2 ** n_bits - 1)
    tmp = cot_inf - real
    tmp = tmp / delta
    tmp = abs(int(tmp))
    return fill_zeros(n_bits, natural_to_bin(tmp))

def real_to_gray_interval(real, n_bits, cot_inf, cot_sup):
    return bin_to_gray(real_to_bin_interval(real, n_bits, cot_inf, cot_sup))

def bin_interval_to_real(data_bin, n_bits, cot_inf, cot_sup):
    delta = (cot_sup - cot_inf) / (2 ** n_bits - 1)
    natural = bin_to_natural(data_bin)
    tmp = delta * natural
    tmp = cot_inf + tmp
    return tmp

def gray_interval_to_real(data_gray, n_bits, cot_inf, cot_sup):
    return bin_interval_to_real(gray_to_bin(data_gray), n_bits, cot_inf, cot_sup)

def fill_zeros(n_bits, data):
    while len(data) < n_bits:
        data.insert(0, 0)
    return data
