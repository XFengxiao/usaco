#!usr/bin/env python
# -*- coding: utf-8 -*-

N = 0

def close(a, b):
    if abs(a-b) <=2:
        return True
    if abs(a-b) >= N-2:
        return True
    return False

def close_enough(n1, n2, n3, 
        c1, c2, c3):
    return close(n1, c1) and close(n2, c2) and close(n3, c3)

if __name__ == "__main__":
    data = []

    with open("combo.in", "r") as fin:
        for line in fin:
            data.append(line.strip())

    N = int(data[0])
    f1, f2, f3 = map(int, data[1].split())
    m1, m2, m3 = map(int, data[2].split())

    total = 0

    for i in range(1, N+1):
        for j in range(1, N+1):
            for k in range(1, N+1):
                if close_enough(i, j, k, f1, f2, f3) or close_enough(i, j, k, m1, m2, m3):
                    total += 1

    with open("combo.out", "w") as fout:
        fout.write(str(total) + "\n")
