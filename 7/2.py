# -*- coding: utf-8 -*-

def switch_places(a, b):
    a, b = b, a
    print('a: ' + ' '.join(map(str, a)))
    print('b: ' + ' '.join(map(str, b)))


a_input = (
    map(int, input('Print 10 numbers separated by spaces for a: ').split(' ')))
b_input = (
    map(int, input('Print 10 numbers separated by spaces for b: ').split(' ')))
switch_places(a_input, b_input)
