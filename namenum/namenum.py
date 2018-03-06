#!usr/bin/env python
# -*- coding: utf-8 -*-

"""
ID: xiaofen6
LANG: PYTHON2
PROG: namenum
"""

"""
把所给的name转换成数字，然后做比较。
"""
arr = [2,2,2,
        3,3,3,
        4,4,4,
        5,5,5,
        6,6,6,
        7,0,7,7,
        8,8,8,
        9,9,9,0]

_NAME_LIST = []
with open("dict.txt", "r") as f:
    for line in f:
        _NAME_LIST.append(line.strip())

def list_to_num(lst):
    num = 0
    for l in lst:
        num = num*10 + (arr[ord(l)-65])
    return num

num_list = map(list_to_num, _NAME_LIST)

NUMBER = 0
with open("namenum.in", "r") as fin:
    NUMBER = int(fin.readline().strip())

names = []
for i in range(len(num_list)):
    if num_list[i] == NUMBER:
        names.append(_NAME_LIST[i])

with open("namenum.out", "w") as fout:
    if names:
        for name in names:
            fout.write(name + "\n")
    else:
        fout.write("NONE\n")
