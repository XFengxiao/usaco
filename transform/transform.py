#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
ID: xiaofen6
LANG: PYTHON2
PROG: transform
"""

def rotation_90(matrix):
    return map(list, zip(*matrix[::-1]))

def rotation_180(matrix):
    return rotation_90(rotation_90(matrix))

def rotation_270(matrix):
    return map(list, zip(*matrix))[::-1]

def reflection(matrix):
    return (rotation_180(matrix))[::-1]
    #for i in range(len(matrix)):
    #    matrix[i] = matrix[i][::-1]
    #return matrix

def combination(matrix):
    matrix1 = rotation_90(reflection(matrix))
    matrix2 = rotation_180(reflection(matrix))
    matrix3 = rotation_270(reflection(matrix))
    return matrix1, matrix2, matrix3

def get_num(before_matrix, after_matrix):
    if after_matrix == rotation_90(before_matrix):
        return 1
    elif after_matrix == rotation_180(before_matrix):
        return 2
    elif after_matrix == rotation_270(before_matrix):
        return 3
    elif after_matrix == reflection(before_matrix):
        return 4
    elif (after_matrix in combination(before_matrix)):
        return 5
    elif after_matrix == before_matrix:
        return 6
    else:
        return 7

data = []
with open("transform.in", "r") as fin:
    for line in fin:
        data.append(line.strip())

N = int(data[0])
before_matrix = []
after_matrix = []

for i in range(1, N+1):
    before_matrix.append(list(data[i]))

for i in range(N+1, len(data)):
    after_matrix.append(list(data[i]))

num = get_num(before_matrix, after_matrix)

with open("transform.out", "w") as fout:
    fout.write(str(num) + "\n")
