# -*- coding: utf-8 -*-

def length_of_sequence():
    length = 0
    n = int(input())
    while n != 0:
        length += 1
        n = int(input())
    return length


print(length_of_sequence())
