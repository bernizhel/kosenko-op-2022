# -*- coding: utf-8 -*-

import math

x = float(input('x: '))
y = float(input('y: '))
z = float(input('z: '))
s = (2 ** (y ** x)) + (3 ** x) ** y - (
        (y * (math.atan(z) - 1 / 3)) / (abs(x) + (1 / (y ** 2 + 1))))
print('{:.5f}'.format(s))
