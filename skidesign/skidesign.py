#!usr/bin/env python
# -*- coding: utf-8 -*-

"""
ID: xiaofen6
LANG: PYTHON2
PROG: skidesign
"""

def get_amount(hills):
    # hills = [1, 4, 20, 21, 24]
    # Enumeration from 0 to 100
    amounts = []
    for lowest_hill in range(1, 100):
        amount = 0
        for hill in hills:
            if hill < lowest_hill:
                amount += (lowest_hill - hill) ** 2
            elif (hill - lowest_hill) > 17:
                amount += (hill - lowest_hill - 17) ** 2
        amounts.append(amount)
    amounts.sort()
    return amounts[0]

    
if __name__ == "__main__":
    data = []

    with open("skidesign.in", "r") as fin:
        for line in fin:
            data.append(line.strip())

    N = int(data[0])

    Hills = []
    for i in range(1, N+1):
        Hills.append(int(data[i]))
    Hills.sort()

    minimum_amount = get_amount(Hills)

    with open("skidesign.out", "w") as fout:
        fout.write(str(minimum_amount) + "\n")

