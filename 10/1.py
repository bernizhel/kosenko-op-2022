# -*- coding: utf-8 -*-

def find_same_rows_and_columns(matrix):
    right_k = []
    for k in range(len(matrix)):
        if matrix[k] == [row[k] for row in matrix]:
            right_k.append(k)
    return right_k


def get_matrix():
    return_matrix = []
    with open('Kosenko_Danil_Aleksandrovich_U-222_vvod.txt') as input_file:
        return_matrix.append(input_file.readline().split(' '))
    return return_matrix


def send_output(data):
    with open('Kosenko_Danil_Aleksandrovich_U-222_vivod.txt', 'w') as output_file:
        output_file.write(data)


matrix = get_matrix()
output_k = ' '.join(map(str, find_same_rows_and_columns(matrix))) or '0'
send_output(output_k)
