# -*- coding: utf-8 -*-

def fibonacci_sum_from(n, k):
    total = 0
    prev_num = 0
    next_num = 1
    for i in range(1, k + n + 1):
        if i >= k:
            total += prev_num
        prev_num, next_num = next_num, prev_num + next_num
    return total


print(fibonacci_sum_from(int(input('n: ')), int(input('k: '))))
