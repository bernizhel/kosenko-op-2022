# -*- coding: utf-8 -*-

from functools import lru_cache


@lru_cache(None)
def fibonacci(n):
    if n == 0:
        return 0
    if n < 3:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_sum(n):
    total = 0
    for i in range(1, n + 1):
        total += fibonacci(i)
    return total


print(fibonacci_sum(int(input('n: '))))
