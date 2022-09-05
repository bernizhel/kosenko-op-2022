# -*- coding: utf-8 -*-
from math import floor


seconds = int(input('Seconds: '))
d = floor(seconds / 3600 / 24)
seconds -= d * 3600 * 24
h = floor(seconds / 3600)
seconds -= h * 3600
m = floor(seconds / 60)
seconds -= m * 60
print(f'{d}:{str(h).zfill(2)}:{str(m).zfill(2)}:{str(seconds).zfill(2)}')
