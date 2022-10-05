# -*- coding: utf-8 -*-

def greater_pairs_in_sequence():
    total = 0
    pair = [int(input())]
    if pair[0] != 0:
        pair.append(int(input()))
    while 0 not in pair:
        if pair[0] < pair[1]:
            total += 1
        pair[0], pair[1] = pair[1], int(input())
    return total


print(greater_pairs_in_sequence())
