"""
ID: xiaofen6 
LANG: PYTHON2
PROG: beads
"""

# data in beads.in
data = []
# beads = ['rwr', 'b', 'rrw']
beads = []

with open('beads.in', 'r') as fin:
    for line in fin:
        data.append(line.strip())

N = int(data[0])
strings = data[1]
# print strings
# strings = "wwwbbrwrbrbrrbrbrwrwwrbwrwrrb"

flag = ["r", "w"]

b_index = strings.index('b')
r_index = strings.index('r')

BEGIN = b_index if b_index > r_index else r_index
strings = data[1] + strings[:BEGIN] + " "
# strings = "wwwbbrwrbrbrrbrbrwrwwrbwrwrrb | wwwbb" + " "
# the pointer of strings
p = BEGIN

count = 0
#for i in range(BEGIN, N):
#    if i == N - 1:
#        if strings[i] in flag:
#            beads.append(strings[p:p+count+1])
#        else:
#            beads.append(strings[p:p+count])
#            beads.append(strings[-1])
#    else:
#        if strings[i] in flag:
#            count += 1
#        else:
#            beads.append(strings[p:p+count])
#            p += count
#            count = 1
#            flag = ["b", "w"] if "r" in flag else ["r", "w"]
for ch in strings[BEGIN:]:
    if ch in flag:
        count += 1
    else:
        beads.append(strings[p:p+count])
        p += count
        count = 1
        flag = ["b", "w"] if "r" in flag else ["r", "w"]

# beads = ['rwr', 'b', 'r', 'b', 'rr', 'b', 'r', 'b', 'rwrwwr', 'bw', 'rwrr', 'bwwwbb']
print beads

def my_len(d):
    # d --> index of beads
    g = 0
    if beads[d-2].endswith('w'):
        g = beads[d-2].rfind('b') if beads[d-2].rfind('b') > beads[d-2].rfind('r') else beads[d-2].rfind('r')
        return len(beads[d]) + len(beads[d-1]) + len(beads[d-2]) - g - 1
    else:
        return len(beads[d]) + len(beads[d-1])

def get_max(lst):
    max = 0
    for i in range(len(beads)):
        if i == 0:
            max = my_len(0)
        else:
            max = my_len(i) if max < my_len(i) else max
    return max

maximum = get_max(beads)

print maximum
