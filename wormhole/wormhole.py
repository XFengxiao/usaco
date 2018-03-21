#!usr/bin/env python
# -*- coding: utf-8 -*-

"""
ID: xiaofen6 
LANG: PYTHON2
PROG: wormhole
"""


def my_sort(coordinates):
    # coordinates = [(2,3), (2,4), (5,8)]
    count = len(coordinates)
    for i in range(0, count-1):
        for j in range(0, count-1-i):
            if coordinates[j][1] > coordinates[j+1][1]:
                coordinates[j], coordinates[j+1] = coordinates[j+1], coordinates[j]
    return coordinates

def cycle_exists():
    for start in range(N):
        pos = start
        for count in range(N):
            pos = next_on_right[partner[pos]]
        if pos != 0:
            return True

def solve():
    total = 0
    for i in range(N):
        if partner[i] == 0:
            break

    if i == N-1:
        if cycle_exists():
            return 1
        return 0

    for j in range(i+1, N):
        if partner[j] == 0:
            partner[i] = j
            partner[j] = i
            print "begin solve()"
            total += solve()
            print "end solve()"
            partner[i] = partner[j] = 0
    return total


if __name__ == "__main__":
    data = []
    partner = [0] * 12
    next_on_right = [0] * 12

    with open("wormhole.in", "r") as fin:
        for line in fin:
            data.append(line.strip())

    X = []
    Y = []

    N = int(data[0])

    for i in range(1, len(data)):
        a, b = map(int, data[i].split())
        X.append(a)
        Y.append(b)

    print "X = ", X
    print "Y =", Y

    for i in range(N):
        for j in range(N):
            if X[j] > X[i] and Y[i] == Y[j]:
                if next_on_right[i] == 0 or (X[j]-X[i] < X[next_on_right[i]]-X[i]):
                    next_on_right[i] = j

    print next_on_right

    print solve()

