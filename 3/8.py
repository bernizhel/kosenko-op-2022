# -*- coding: utf-8 -*-

def print_find_same(a, b, c):
    difference_amount = len({a, b, c})
    if difference_amount == 3:
        print(0)
    elif difference_amount == 2:
        print(2)
    else:
        print(3)


print_find_same(int(input('a: ')), int(input('b: ')), int(input('c: ')))
