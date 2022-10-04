# -*- coding: utf-8 -*-

def print_sum_of_n(N):
    total = 0
    for i in range(N):
        total += int(input(str(i + 1) + ' number: '))
    print(total)


print_sum_of_n(int(input('N: ')))
