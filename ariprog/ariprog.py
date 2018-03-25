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

def get_S(M):
    S = set()
    exist = [0] * (2*M*M+1)
    for i in range(M+1):
        for j in range(M+1):
            S.add(i*i + j*j)
            exist[i*i+j*j] = 1
    return S, exist

def get_sequences(N, S, exist):
    sequences = []
    m = max(S)
    for b in range(1, (m/(N-1))+1):
        for a in S[:-N+1]:
            count = 0
            if a + (N-1) * b > m:
                break
            sequences.append([a,b])
            #for n in range(N):
            #    count += 1
            #    #if exist[a+n*b]:
            #    #    count += 1
            #    #else:
            #    #    break
            #if count == N:
            #    sequences.append([a,b])
    return sequences

if __name__ == "__main__":
    import time
    with open("ariprog.in", "r") as fin:
        N = fin.readline().strip()
        N = int(N)
        M = fin.readline().strip()
        M = int(M)

    S, exist = get_S(M)
    S = list(S)
    S.sort()
    print "b len ", (max(S)/(N-1))+1
    print "S len ", len(S)
    print "max S ", max(S)
    #begin = time.time()
    #sequences = get_sequences(N, S, exist)
    ##print sequences
    #end = time.time()
    #print (end-begin)
    

    #sequences = get_sequences(N, S, exist)
    #with open("ariprog.out", "w") as fout:
    #    if not sequences:
    #        fout.write("NONE" + "\n")
    #    else:
    #        for i, j in sequences:
    #            fout.write(str(i) + ' ' + str(j) + '\n')

