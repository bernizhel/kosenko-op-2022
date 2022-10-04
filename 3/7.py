# -- coding: utf-8 --
def print_is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print('Да')
        return
    print('Нет')


print_is_leap_year(int(input('Year: ')))
