# -*- coding: utf-8 -*-

def stairs(n):
    total_string = ''
    for i in range(1, n + 1):
        total_string += ''.join(map(str, range(1, i + 1))) + '\n'
    return total_string


print(stairs(int(input('n: '))))
