# -*- coding: utf-8 -*-

def print_from_to_down(a, b):
    if a < b:
        for i in range(a, b + 1):
            print(i)
    else:
        for i in range(a, b - 1, -1):
            print(i)


print_from_to_down(int(input('A: ')), int(input('B: ')))
