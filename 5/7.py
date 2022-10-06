# -*- coding: utf-8 -*-

def greater_pairs_in_sequence():
    total = 0
    pair = [int(input('N1: '))]
    if pair[0] != 0:
        pair.append(int(input('N2: ')))
    length = 2
    while 0 not in pair:
        if pair[0] < pair[1]:
            total += 1
        length += 1
        pair[0], pair[1] = pair[1], int(input(f'N{length}: '))
    return total


print(greater_pairs_in_sequence())
