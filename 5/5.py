# -*- coding: utf-8 -*-

def length_of_sequence():
    length = 0
    n = int(input('N1: '))
    while n != 0:
        length += 1
        n = int(input(f'N{length + 1}: '))
    return length


print(length_of_sequence())
