# -*- coding: utf-8 -*-

import random
import json
import os


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

    print('Done generating the matrix.')

    return generate_matrix(rows, columns, min_value, max_value)


def output_matrix(matrix):
    placeholder_length = len(str(max([max(row) for row in matrix]))) + 1

    for row in matrix:
        print(' '.join(map(lambda n: format(n, ' ' + str(placeholder_length)), row)))


def get_matrix(filename='input_2.json'):
    print('Getting the matrix.')

    if input('Generate new matrix? (print y): ').lower().find('y') != -1:
        new_matrix = input_matrix()
        
        send_matrix(new_matrix, filename=filename)
    
    if not os.path.exists(get_path(filename)):
        print('The given file does not exist.')
        exit(1)
    
    with open(get_path(filename), 'r') as input_file:
        loaded_matrix = json.load(input_file)
    
    print('Done getting the matrix.')

    return loaded_matrix


def send_matrix(matrix, filename='output_2.json'):
    with open(get_path(filename), 'w') as output_file:
        json.dump(matrix, output_file, separators=(',', ':'))


def get_path(filename):
    return os.path.realpath(os.path.join(__file__, '..', filename))


def subtract_last_row(matrix):
    last_row = matrix[-1]

    for row_index in range(len(matrix) - 1):
        # last_row length is equal to every matrix's row length
        for column_index in range(len(last_row)):
            matrix[row_index][column_index] -= last_row[column_index]

    return matrix


def main():
    matrix = get_matrix()
    print('The given matrix is:')
    output_matrix(matrix)

    matrix = subtract_last_row(matrix)
    print('The modified matrix is:')
    output_matrix(matrix)
    send_matrix(matrix)


if __name__ == '__main__':
    main()
