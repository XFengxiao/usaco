#!usr/bin/env python
# -*- coding: utf-8 -*-

"""
ID: xiaofen6 
LANG: PYTHON2
PROG: crypt1
"""

def check_one(three, one, numbers):
    pro = three * one
    if pro >= 1000:
        return False
    else:
        for i in str(pro):
            if int(i) not in numbers:
                return False
    return True

def check_two(three, two, numbers):
    # three --> 234
    # two --> 55
    # numbers --> a list [1,2,3]
    pro = three * two
    two_1, two_2 = map(int, str(two))
    if check_one(three, two_2, numbers) and check_one(three, two_1, numbers):
        if pro < 10000:
            pro_set = set(map(int, str(pro)))
            if pro_set.issubset(set(numbers)):
                return True
    return False

def get_three_num(numbers):
    # numbers --> [2,3,4...]
    # return three num int
    three_num = []
    for i in numbers:
        for j in numbers:
            for k in numbers:
                three_num.append(i*100+j*10+k)
    return three_num

def get_two_num(numbers):
    two_num = []
    for i in numbers:
        for j in numbers:
            two_num.append(i*10+j)
    return two_num

if __name__ == "__main__":

    count = 0
    data = []

    with open("crypt1.in", "r") as fin:
        for line in fin:
            data.append(line.strip())

    N = int(data[0])

    numbers = map(int, data[1].split())

    two_num = get_two_num(numbers)
    three_num = get_three_num(numbers)

    for thr in three_num:
        for tw in two_num:
            if check_two(thr, tw, numbers):
                count += 1

    with open("crypt1.out", "w") as fout:
        fout.write(str(count) + "\n")

