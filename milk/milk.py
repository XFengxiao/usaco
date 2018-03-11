#!usr/bin/env python
# -*- coding: utf-8 -*-

"""
ID: xiaofen6
LANG: PYTHON2
PROG: milk
"""

def get_minimum_value(p, a, n):
    # p --> price list
    # a --> amount list
    # n --> total num
    total = zip(p, a)
    total.sort()

    amount = []
    minimum_value = 0
    for x, y in total:
        if sum(amount) < n:
            amount.append(y)
            if sum(amount) > n:
                amount[-1] = n - sum(amount[:-1])
        elif sum(amount) == n:
            break
        else:
            amount[-1] = n - sum(amount[:-1])
            break
    for i in range(len(amount)):
        minimum_value += (total[i][0] * amount[i])
    return minimum_value

if __name__ == "__main__":
    data = []
    P = []
    A = []

    with open("milk.in", "r") as fin:
        for line in fin:
            data.append(line.strip())
    
    N, M = map(int, data[0].split())
    #print N, M
    
    for d in data[1:]:
        num_1, num_2 = map(int, d.split())
        P.append(num_1)
        A.append(num_2)
    #print P
    #print A
    
    minimum_value = get_minimum_value(P, A, N)
    #print minimum_value
    
    with open("milk.out", "w") as fout:
        fout.write(str(minimum_value) + "\n")
    
