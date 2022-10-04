# -*- coding: utf-8 -*-

def factorial(n):
    total = 1
    for i in range(1, n + 1):
        total *= i
    return total


print(factorial(int(input('n: '))))
