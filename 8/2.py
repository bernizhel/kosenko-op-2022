# -*- coding: utf-8 -*-

def median_to_side(side_index, sides):
    return (((sides[side_index - 2] ** 2 + sides[side_index - 1] ** 2) / 2) - (
            (sides[side_index] ** 2) / 4)) ** 0.5


def find_medians(sides):
    medians = []
    for i in range(3):
        medians.append(median_to_side(i, sides))
    return medians


def find_medians_of_medians(a, b, c):
    return find_medians(find_medians([a, b, c]))


for median in find_medians_of_medians(int(input('A: ')), int(input('B: ')),
                                      int(input('C: '))):
    print(f'{median:.2f}')
