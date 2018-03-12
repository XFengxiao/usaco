#!usr/bin/env python
# -*- coding: utf-8 -*-

"""
ID: xiaofen6 
LANG: PYTHON2
PROG: combo 
"""

def pro(x, y):
    return x * y

def get_same(password1, password2, n):
    # password1,password2 a three numbers list [2,3,4]
    same_password = []
    for i in range(3):
        if (password1[i] < 5 and password2[i] > n-4) or (password1[i] > n-4 and password2[i] < 5): 
            ab = password2[i] + n - password1[i] if password1[i] > password2[i] else password1[i] + n - password2[i]
        else:
            ab = abs(password1[i] - password2[i]) 
        if ab >= 5:
            return 0
        else:
            same_password.append(5 - ab)
    return reduce(pro, same_password)

if __name__ == "__main__":
    data = []
    with open("combo.in", "r") as fin:
        for line in fin:
            data.append(line.strip())

    N = int(data[0])

    assert(0 <= N <= 100)

    pwd1 = map(int, data[1].split())
    pwd2 = map(int, data[2].split())

    with open("combo.out", "w") as fout:
        if N <= 5:
            fout.write(str(N*N*N) + "\n")
        else:
            num = 250 - get_same(pwd1, pwd2, N)
            fout.write(str(num) + "\n")
