"""
ID: xiaofen6 
LANG: PYTHON2
PROG: friday
"""

def get_days(year, month):
    if((year%4 == 0 and year%100 != 0) or (year%400 == 0)):
        is_leap = True
    else:
        is_leap = False
    if month in [1,3,5,7,8,10,12]:
        return 31
    elif month == 2:
        if is_leap:
            return 29
        else:
            return 28
    return 30

with open("friday.in", "r") as fin:
    N = int(fin.readline().strip())

assert(N>0 and N<=400)

days = [0] * 7

week = 0

for i in range(1900, 1900+N):
    for j in range(1, 13):
        days[week%7] += 1
        week += get_days(i, j)

with open('friday.out', 'w') as fout:
    for p in range(6):
        fout.write(str(days[p]) + ' ')
    fout.write(str(days[6]) + '\n')
