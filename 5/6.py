# -*- coding: utf-8 -*-

def average_of_sequence():
    sequence = []
    n = int(input())
    while n != 0:
        sequence.append(n)
        n = int(input())
    return sum(sequence) / len(sequence)


print(average_of_sequence())
