# -*- coding: utf-8 -*-

import random


def generate_matrix(rows, columns, min_value, max_value):
    matrix = []

    for row in range(rows):
        matrix.append([])

        for _ in range(columns):
            matrix[row].append(random.randint(min_value, max_value))

    return matrix


def input_matrix():
    print('Generating your matrix.')

    rows = int(input('Rows: '))
    columns = int(input('Columns: '))
    min_value = int(input('Min value: '))
    max_value = int(input('Max value: '))

    print('Done.')

    return generate_matrix(rows, columns, min_value, max_value)


def output_matrix(matrix):
    placeholder_length = len(str(max([max(row) for row in matrix]))) + 1

    for row in matrix:
        print(' '.join(map(lambda n: format(n, ' ' + str(placeholder_length)), row)))


def subtract_last_row(matrix):
    last_row = matrix[-1]
    for row_index in range(len(matrix) - 1):
        # last_row length is equal to every matrix's row length
        for column_index in range(len(last_row)):
            matrix[row_index][column_index] -= last_row[column_index]
    return matrix


def main():
    matrix = input_matrix()
    print('The given matrix is:')
    output_matrix(matrix)

    matrix = subtract_last_row(matrix)
    print('The modified matrix is:')
    output_matrix(matrix)


if __name__ == '__main__':
    main()
