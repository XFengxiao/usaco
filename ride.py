"""
ID: xiaofen6 
LANG: PYTHON2
PROG: ride
"""

message = []

with open('ride.in', 'r') as fin:
    for line in fin:
        message.append(line.strip())

comet = message[0]
group = message[1]

def str_to_num(s):
    # s: "ABC"
    # return [1,2,3]
    return [ord(ch)-64 for ch in s]

def my_multiply(x, y):
    return x*y

num_1 = reduce(my_multiply, str_to_num(comet))
num_2 = reduce(my_multiply, str_to_num(group))

with open('ride.out', 'w') as fout:
    if num_1 % 47 == num_2 % 47:
        fout.write("GO\n")
    else:
        fout.write("STAY\n")
