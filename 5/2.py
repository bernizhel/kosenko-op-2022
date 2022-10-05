# -*- coding: utf-8 -*-

def find_max_divider(n):
    for i in range(n // 2 + 1, 1, -1):
        if n % i == 0:
            return i


print(find_max_divider(int(input('N: '))))
