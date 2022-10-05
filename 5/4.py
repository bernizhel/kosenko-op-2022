# -*- coding: utf-8 -*-

def get_day(x, y):
    days = 0
    while x < y:
        x *= 1.1
        days += 1
    return days


print(get_day(float(input('x: ')), float(input('y: '))))
