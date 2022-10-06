# -*- coding: utf-8 -*-

def find_min_divider(n):
    for i in range(2, n // 2 + 2):
        if n % i == 0:
            return i
    return n


print(find_min_divider(int(input('N: '))))
