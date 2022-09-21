# -*- coding: utf-8 -*-

def print_time_from_minutes(n):
    n = n % (60 * 24)
    hours = str(int(n / 60)).zfill(2)
    print(f'{hours}:{str(n % 60).zfill(2)}')


print_time_from_minutes(int(input('Minutes: ')))
