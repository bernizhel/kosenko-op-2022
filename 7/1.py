# -*- coding: utf-8 -*-

def find_min_odd(seq):
    return min(list(filter(lambda x: x % 2, seq)))


print(find_min_odd(
    map(int, input('Print numbers separated by spaces: ').split(' '))))
