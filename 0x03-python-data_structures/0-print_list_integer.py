#!/usr/bin/python3
def print_list_integer(my_list=[]):
    new_matrix = []
    for col in my_list:
        result = list(map(lambda x: x**2, col))
        new_matrix.append(result)
    return new_matrix
