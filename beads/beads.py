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

strings = data[1]
# strings = "wwwbbrwrbrbrrbrbrwrwwrbwrwrrb"

flag = ["r", "w"]

b_index = strings.index('b')
r_index = strings.index('r')

BEGIN = b_index if b_index > r_index else r_index
# the pointer of strings
p = BEGIN

count = 0
for ch in strings[BEGIN:]:
    if ch in flag:
        count += 1
    else:
        beads.append(strings[p:p+count])
        p += count
        count = 0
        flag = ["b", "w"] if "r" in flag else ["r", "w"]

print beads
