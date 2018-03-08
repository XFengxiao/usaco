#!usr/bin/env python
# -*- coding: utf-8 -*-

"""
ID: xiaofen6 
LANG: PYTHON2
PROG: palsquare
"""

def trans(num, base):
    mapping = ['0', '1', '2', '3', '4',
            '5', '6', '7', '8', '9',
            'A', 'B', 'C', 'D', 'E',
            'F', 'G', 'H', 'I', 'J']
    n = ''
    temp = num
    while temp > 0:
        n = mapping[temp%base] + n
        temp = temp / base
    return n

def is_palsquare(s):
    # s = '12321'
    if s == s[::-1]:
        return True
    return False

with open("palsquare.in", "r") as fin:
    NUM = int(fin.readline().strip())

with open("palsquare.out", "w") as fout:
    for i in range(1, 301):
        foo = trans(i*i, NUM)
        foo_1 = trans(i, NUM)
        if is_palsquare(foo):
            fout.write(foo_1 + " " + foo + "\n")
