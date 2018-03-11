#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
ID: xiaofen6
LANG: PYTHON2
PROG: barn1
"""
"""
这道题的解题思路同样有很多。关键他分布在贪心的这一章节，所以，我们就姑且使用贪心来做了，问题求的是最小的木板长度来把目前棚子中有牛

的地方封住，那么我们首先想到了贪心（PS:怎么贪心呢？）其实，只需要找到第一头牛和最后一头牛，然后让sum=end-start-1;也就是说，找到了第一个

和最后一个牛的位置，那么这就是一条由长长的大木板所覆盖的牛棚了，接下来，因为题目要求只是用M个木板，那么M个数量就决定了我们贪心的策略，

也就是说，这个关键的决策量对于其分布起了很大的作用，不难发现，M个木板中间必定存在M-1个空隙，然后，就是求出前M-1大的空隙，不断的更新

sum，这样，就可以得到我们最小的木板长度了。。。
"""

def get_minimum(stall_number, m):
    # stall_number = []
    # m = 3
    stall_number.sort()
    c = []
    minimum = stall_number[-1] - stall_number[0] + 1

    # c 存放所有的间隙
    for i in range(1, len(stall_number)):
        c.append(stall_number[i]-stall_number[i-1]-1)
    if c:
        c.sort()
    c = c[::-1]
    for i in c[:m-1]:
        minimum -= i
    return minimum

if __name__ == "__main__":

    data = []
    stall_number = []

    with open("barn1.in", "r") as fin:
        for line in fin:
            data.append(line.strip())
    
    M, S, C = map(int, data[0].split())
    for i in range(1, len(data)):
        stall_number.append(int(data[i]))
    
    with open("barn1.out", "w") as fout:
        minimum = get_minimum(stall_number, M)
        fout.write(str(minimum) + "\n")
