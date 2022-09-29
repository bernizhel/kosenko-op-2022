# -*- coding: utf-8 -*-

from functools import reduce


def sum_of_factorials(n):
    total = 0
    for i in range(1, n + 1):
        total += reduce((lambda x, y: x * y), range(1, i + 1))
    return total


print(sum_of_factorials(int(input('n: '))))
