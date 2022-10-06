# -*- coding: utf-8 -*-

def max_length_in_sequence():
    max_length = length = 0
    pair = [int(input('N1: '))]
    if pair[0] != 0:
        pair.append(int(input('N2: ')))
        length += 1
    sequence_length = 2
    while 0 not in pair:
        if pair[0] == pair[1]:
            length += 1
        else:
            max_length = max(length, max_length)
            length = 1
        sequence_length += 1
        pair[0], pair[1] = pair[1], int(input(f'N{sequence_length}: '))
    return max(length, max_length)


print(max_length_in_sequence())
