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

    rows_and_columns = int(input('Rows and columns: '))
    min_value = int(input('Min value: '))
    max_value = int(input('Max value: '))

    print('Done generating the matrix.')

    return generate_matrix(rows_and_columns, rows_and_columns, min_value, max_value)


def output_matrix(matrix):
    placeholder_length = len(str(max([max(row) for row in matrix]))) + 1

    for row in matrix:
        print(' '.join(map(lambda n: format(n, ' ' + str(placeholder_length)), row)))


def get_matrix(filename='input_1.json'):
    print('Getting the matrix.')

    if input('Generate new matrix? (print y): ').lower().find('y') != -1:
        new_matrix = input_matrix()
        
        send_data(new_matrix, filename=filename)
    
    if not os.path.exists(get_path(filename)):
        print('The given file does not exist.')
        exit(1)
    
    with open(get_path(filename), 'r') as input_file:
        loaded_matrix = json.load(input_file)
    
    print('Done getting the matrix.')

    return loaded_matrix


def send_data(data, filename='output_1.json'):
    with open(get_path(filename), 'w') as output_file:
        json.dump(data, output_file, separators=(',', ':'))


def get_path(filename):
    return os.path.realpath(os.path.join(__file__, '..', filename))


def output_answer(answer):
    print(' '.join(map(str, answer['answer'])) if answer['answer'] != None else answer['answer'])


def find_same_rows_and_columns(matrix):
    right_k = {'answer': []}

    for k in range(len(matrix)):
        if matrix[k] == [row[k] for row in matrix]:
            right_k['answer'].append(k)

    if right_k['answer'] == []:
        right_k['answer'] = None

    return right_k


def main():
    matrix = get_matrix()
    print('The given matrix is:')
    output_matrix(matrix)

    right_rows_and_columns = find_same_rows_and_columns(matrix)
    print('The right K numbers are: ')
    output_answer(right_rows_and_columns)
    send_data(right_rows_and_columns)


if __name__ == '__main__':
    main()
