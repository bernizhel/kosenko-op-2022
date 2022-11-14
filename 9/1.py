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


def find_same_rows_and_columns(matrix):
    right_k = []

    for k in range(len(matrix)):
        if matrix[k] == [row[k] for row in matrix]:
            right_k.append(k)

    return right_k


def main():
    matrix = input_matrix()
    print('The given matrix is:')
    output_matrix(matrix)

    right_rows_and_columns = find_same_rows_and_columns(matrix)
    print('The right K numbers are:')
    print(' '.join(map(str, right_rows_and_columns)) or None)


if __name__ == '__main__':
    main()
