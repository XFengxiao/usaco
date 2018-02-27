"""
ID: xiaofen6 
LANG: PYTHON2
PROG: gift1 
"""

message = []

with open("gift1.in", "r") as fin:
    for line in fin:
        message.append(line.strip())

# message pointer p
p = 0
num = int(message[p])
np = dict(zip(message[1:num+1],[0]*num))
# np = {'a':0,'b':0,'c':0}

group = []
p = p + num + 1 
# print p

while True:
    if p >= len(message) - 1:
        break
    else:
        num_1, num_2 = [int(n) for n in (message[p+1].split(' '))]
        l = []
        l.append(message[p])
        l.append(num_1)
        l.append(num_2)
        if num_2 == 0:
            group.append(l)
        else:
            for i in range(num_2):
                l.append(message[p+2+i])
            group.append(l)
        p = p + num_2 + 2



def dealing_money(person_name, money, people_num, *args):
    if people_num == 0 or money == 0:
        pass
    else:
        m = money % people_num
        reduce_money = money - m
        avg = reduce_money / people_num
        np[person_name] -= reduce_money
        for arg in args:
            np[arg] += avg

for g in group:
    # g = ['p_name',money,p_num,...]
    dealing_money(*g)

with open('gift1.out', 'w') as fout:
    for i in range(num):
        fout.write(message[i+1] + ' ' + str(np[message[i+1]]) + '\n')
