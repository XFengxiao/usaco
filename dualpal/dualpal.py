#!usr/bin/env python
# -*- coding: utf-8 -*-

"""
ID: xiaofen6
LANG: PYTHON2
PROG: dualpal
"""

def trans(num, base):
    mapping = "0123456789"
    st = ""
    temp = num
    while temp > 0:
        st = mapping[temp%base] + st
        temp = temp / base
    return st

def is_pal(string):
    if string == string[::-1]:
        return True
    return False

def is_dualpal(num):
    count = 0
    for i in range(2, 11):
        if is_pal(trans(num, i)):
            count += 1
    if count >= 2:
        return True
    return False

def get_dualpal(n, s):
    pal = []
    p = s
    while True:
        p += 1
        if len(pal) == n:
            return pal
        else:
            if is_dualpal(p):
                pal.append(p)

with open("dualpal.in", "r") as fin:
    N, S = fin.readline().strip().split()
    N = int(N)
    S = int(S)

pal = get_dualpal(N, S)

with open("dualpal.out", "w") as fout:
    for i in pal:
        fout.write(str(i) + "\n")
