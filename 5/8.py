# -*- coding: utf-8 -*-

def greater_pairs_in_sequence():
    max_length = length = 0
    pair = [int(input())]
    if pair[0] != 0:
        pair.append(int(input()))
        length += 1
    while 0 not in pair:
        if pair[0] == pair[1]:
            length += 1
        else:
            max_length = max(length, max_length)
            length = 0
        pair[0], pair[1] = pair[1], int(input())
    max_length = max(length, max_length)
    return max_length


print(greater_pairs_in_sequence())
