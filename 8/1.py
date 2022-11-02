# -*- coding: utf-8 -*-

from functools import lru_cache


@lru_cache(None)
def dividers_sum(n):
    total_sum = 0
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            total_sum += i
    return total_sum


@lru_cache(None)
def friendly_numbers(n):
    friendly_pairs = []
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            if dividers_sum(i) == j and i == dividers_sum(j):
                friendly_pairs.append((i, j))
    return friendly_pairs


for pair in friendly_numbers(int(input('N: '))):
    print(f'{pair[0]} {pair[1]}')
