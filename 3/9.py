# -*- coding: utf-8 -*-

def print_is_chocolate_breakable(n, m, k):
    if k % n == 0 or k % m == 0:
        print('Да')
        return
    print('Нет')


print_is_chocolate_breakable(int(input('n: ')), int(input('m: ')),
                             int(input('k: ')))
