# -*- coding: utf-8 -*-

def sum_of_cubes(n):
    return sum(map(lambda x: x ** 3, range(1, n + 1)))


print(sum_of_cubes(int(input('n: '))))
