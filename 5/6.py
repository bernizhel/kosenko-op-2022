# -*- coding: utf-8 -*-

def average_of_sequence():
    sequence = []
    n = int(input('N1: '))
    while n != 0:
        sequence.append(n)
        n = int(input(f'N{len(sequence) + 1}: '))
    return sum(sequence) / len(sequence)


print(average_of_sequence())
