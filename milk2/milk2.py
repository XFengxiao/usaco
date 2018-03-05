#!/usr/bin/env python 
# -*- coding: utf-8 -*-

"""
ID: xiaofen6 
LANG: PYTHON2
PROG: milk2
"""

def get(start, end):
    # start = [300, 700, 1500]
    # end = [1000, 1200, 2100]
    assert(len(start) == len(end))
    max_continuous = end[0] - start[0]
    max_idle = 0
    for i in range(1, len(start)):
        if start[i] <= end[i-1]:
            start[i] = start[i-1]
            max_continuous = end[i] - start[i] if (end[i] - start[i]) > max_continuous else max_continuous
        else:
            max_idle = start[i] - end[i-1] if (start[i] - end[i-1]) > max_idle else max_idle
    return max_continuous, max_idle

data = []
with open("milk2.in", "r") as fin:
    for line in fin:
        data.append(line.strip())

N = int(data[0])
assert(1 <= N <= 5000)

start = []
end = []
for i in range(1, len(data)):
    x, y = map(int, data[i].split())
    start.append(x)
    end.append(y)

start.sort()
end.sort()

max_continuous, max_idle = get(start, end)

with open("milk2.out", "w") as fout:
    fout.write(str(max_continuous) + " " + str(max_idle) + "\n")
