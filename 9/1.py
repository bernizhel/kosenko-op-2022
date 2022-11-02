# -*- coding: utf-8 -*-

import random


def find_same_rows_and_columns(matrix):
    right_k = []
    for k in range(len(matrix)):
        if matrix[k] == [row[k] for row in matrix]:
            right_k.append(k)
    return right_k


def create_matrix(k):
    matrix = []
    for row in range(k):
        matrix.append([])
        for column in range(k):
            matrix[row].append(random.randint(1, 2))
    return matrix


random_matrix = create_matrix(int(input('K: ')))
print('The given matrix is:')
for random_row in random_matrix:
    print(' '.join(map(str, random_row)))
print('The right K numbers are:')
output_k = ' '.join(map(str, find_same_rows_and_columns(random_matrix)))
print(output_k if output_k else None)
