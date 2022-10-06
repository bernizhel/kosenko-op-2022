# -*- coding: utf-8 -*-

def fibonacci_sum(n):
    total = 0
    prev_num = next_num = 1
    for i in range(1, n + 1):
        total += prev_num
        prev_num, next_num = next_num, prev_num + next_num
    return total


print(fibonacci_sum(int(input('n: '))))
