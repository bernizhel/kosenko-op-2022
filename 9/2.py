# -*- coding: utf-8 -*-

import random


def subtract_last_row(matrix):
    last_row = matrix[-1]
    for row_index in range(len(matrix) - 1):
        # last_row length is equal to every matrix's row length
        for column_index in range(len(last_row)):
            matrix[row_index][column_index] -= last_row[column_index]
    return matrix


def create_matrix():
    matrix = []
    n = random.randint(2, 5)
    m = random.randint(2, 5)
    for row in range(n):
        matrix.append([])
        for column in range(m):
            matrix[row].append(random.randint(1, 9))
    return matrix


random_matrix = create_matrix()
print('The given matrix is:')
for random_row in random_matrix:
    print(' '.join(map(str, random_row)))
print('The modified matrix is:')
for random_row in subtract_last_row(random_matrix):
    print(' '.join(map(lambda n: f'{n:2d}', random_row)))
