# -*- coding: utf-8 -*-

def print_odd_from_to_down(a, b):
    for i in range(a, b - 1, -1):
        if i % 2 == 1:
            print(i)


print_odd_from_to_down(int(input('A: ')), int(input('B: ')))
