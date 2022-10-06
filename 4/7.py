# -*- coding: utf-8 -*-

def sum_of_factorials(n):
    total = 1
    next_factor = 1
    for i in range(2, n + 1):
        next_factor *= i
        total += next_factor
    return total


print(sum_of_factorials(int(input('n: '))))
