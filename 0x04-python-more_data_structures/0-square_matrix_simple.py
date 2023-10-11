#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    mat = []
    for row in matrix:
        sq = list(map(lambda x: x**2, row))
        mat.append(sq)
    return mat
