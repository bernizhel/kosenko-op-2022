# -*- coding: utf-8 -*-

def get_color_number(column, row):
    if column % 2 and row % 2:
        return 1
    elif not (column % 2) and not (row % 2):
        return 1
    return 0


def print_is_color_same(first_col, first_row, second_col, second_row):
    if (get_color_number(first_col, first_row) == get_color_number(second_col,
                                                                   second_row)):
        print('Да')
        return
    print('Нет')


print_is_color_same(int(input('First cell column: ')),
                    int(input('First cell row: ')),
                    int(input('Second cell column: ')),
                    int(input('Second cell row: ')))
