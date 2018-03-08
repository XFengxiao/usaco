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

print trans(5, 4)

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
    for i in range(s+1, 10001):
        if len(pal) == n:
            return pal
        else:
            if is_dualpal(i):
                pal.append(i)

with open("dualpal.in", "r") as fin:
    N, S = fin.readline().strip().split()
    N = int(N)
    S = int(S)

print N
print S
pali = get_dualpal(N, S)
print pali

#with open("dualpal.out", "w") as fout:
#    if pal:
#        for i in pal:
#            fout.write(str(i) + "\n")
