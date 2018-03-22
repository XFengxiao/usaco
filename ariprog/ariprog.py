#!usr/bin/env python
# -*- coding: utf-8 -*-

"""
ID: xiaofen6
LANG: PYTHON2
PROG: ariprog
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

def get_S(M):
    S = set()
    for i in range(M+1):
        for j in range(M+1):
            S.add(i*i + j*j)
    return S

def get_sequences(N, S):
    sequences = []
    m = max(S)
    for b in range(1, (m/2)+1):
        for a in S[:-3]:
            count = 0
            for n in range(N):
                if (a+n*b) in S:
                    count += 1
            if count == N:
                sequences.append([a,b])
    return sequences

if __name__ == "__main__":
    with open("ariprog.in", "r") as fin:
        N = fin.readline().strip()
        N = int(N)
        M = fin.readline().strip()
        M = int(M)

    S = get_S(M)
    S = list(S)
    sequences = get_sequences(N, S)

    #with open("ariprog.out", "w") as fout:
    #    if not sequences:
    #        fout.write("NONE" + "\n")
    #    else:
    #        for i, j in sequences:
    #            fout.write(str(i) + ' ' + str(j) + '\n')

