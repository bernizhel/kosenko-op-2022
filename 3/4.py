# -*- coding: utf-8 -*-

def print_lacing_length(a, b, l, N):
    print(2 * (N - 1) * (a + b) + a + l * 2)


print_lacing_length(int(input('a: ')), int(input('b: ')), int(input('l: ')),
                    int(input('N: ')))
