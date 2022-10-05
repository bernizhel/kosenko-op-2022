# -*- coding: utf-8 -*-

import math


def find_max_power(n):
    return math.floor(math.log2(n))


print(find_max_power(int(input('N: '))))
