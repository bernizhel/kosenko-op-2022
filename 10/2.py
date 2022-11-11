# -*- coding: utf-8 -*-

import random


def subtract_last_row(matrix):
    last_row = matrix[-1]
    for row_index in range(len(matrix) - 1):
        # last_row length is equal to every matrix's row length
        for column_index in range(len(last_row)):
            matrix[row_index][column_index] -= last_row[column_index]
    return matrix


def get_matrix():
    return_matrix = []
    with open('Kosenko_Danil_Aleksandrovich_U-222_vvod.txt') as input_file:
        for line in input_file.readlines():
            return_matrix.append(list(map(int, line.split(' '))))
    return return_matrix


def send_output(matrix):
    with open('Kosenko_Danil_Aleksandrovich_U-222_vivod.txt', 'w') as output_file:
        output_file.writelines([' '.join(map(str, row)) + '\n' for row in matrix])


matrix = get_matrix()
send_output(subtract_last_row(matrix))
