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

b_index = strings.find('b')
r_index = strings.find('r')

# BEGIN = b_index if b_index > r_index else r_index
if b_index == r_index == -1:
    BEGIN = 0
else:
    BEGIN = b_index if b_index > r_index else r_index

# set flag
flag = ["r", "w"] if strings[BEGIN] == "r" else ["b", "w"]
# strings = "wwwbbrwrbrbrrbrbrwrwwrbwrwrrb | wwwbb" + " "
strings = data[1] + strings[:BEGIN] + " "
# the pointer of strings
p = BEGIN

count = 0
for ch in strings[BEGIN:]:
    if ch in flag:
        count += 1
    else:
        beads.append(strings[p:p+count])
        p += count
        count = 1
        flag = ["b", "w"] if "r" in flag else ["r", "w"]

# beads = ['rwr', 'b', 'r', 'b', 'rr', 'b', 'r', 'b', 'rwrwwr', 'bw', 'rwrr', 'bwwwbb']

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
    if len(lst)<= 2:
        for i in range(len(lst)):
            max += len(lst[i])
    else:
        for i in range(len(lst)):
            max = my_len(i) if max < my_len(i) else max
    return max

maximum = get_max(beads)

with open("beads.out", "w") as fout:
    fout.write(str(maximum) + "\n")
