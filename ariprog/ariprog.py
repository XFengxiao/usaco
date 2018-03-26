#!usr/bin/env python
# -*- coding: utf-8 -*-

"""
ID: xiaofen6
LANG: PYTHON2
PROG: ariprog
"""

"""
原来判断一个元素在不在列表里面这么耗时的。
"""

#>>>L = [('b',6),('a',1),('c',3),('d',4)]
#>>>L.sort(key=lambda x:x[1])
#>>>L
#>>>[('a', 1), ('c', 3), ('d', 4), ('b', 6)]
#
#>>>L = [('b',2),('a',1),('c',3),('d',4)]

def my_sort(lis):
    # lis = [[2,5], [5,2], [3,9], [8,7]]
    num = len(lis)
    # 根据第二个元素冒泡排序
    for i in range(num - 1):
        for j in range(num - i -1):
            if lis[j][1] > lis[j+1][1]:
                lis[j], lis[j+1] = lis[j+1], lis[j]
    return lis

with open("ariprog.in", "r") as fin:
    N = fin.readline().strip()
    N = int(N)
    M = fin.readline().strip()
    M = int(M)

def get_exist(M):
    #S = set()
    S = [0] * (2*M*M+1)
    exist = [0] * (2*M*M+1)
    for i in range(M+1):
        for j in range(M+1):
            #S.add(i*i + j*j)
            S[i*i+j*j] = i*i + j*j
            exist[i*i+j*j] = 1
    return S, exist

_S, _exist = get_exist(M)

def check(a, b):
    temp = a
    for i in range(N):
        if not _exist[temp]:
            return False
        temp += b
    return True

def get_sequences(N, S, exist):
    sequences = []
    for b in range(1, (S[-1]/(N-1))+1):
        for a in range(len(exist)):
            if exist[a]:
                if S[a] + (N-1) * b > S[-1]:
                    break
                if check(a, b):
                    sequences.append([S[a], b])
    return sequences

sequences = get_sequences(N, _S, _exist)
print sequences
#with open("ariprog.out", "w") as fout:
#    if not sequences:
#        fout.write("NONE" + "\n")
#    else:
#        for i, j in sequences:
#            fout.write(str(i) + ' ' + str(j) + '\n')

