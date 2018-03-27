with open("ariprog.in", "r") as fin:
    N = fin.readline().strip()
    N = int(N)
    M = fin.readline().strip()
    M = int(M)

#_exist = [0] * (2*M*M+1)
_exist = dict()
for i in xrange(2*M*M+1):
    _exist[i] = 0

for i in xrange(M+1):
    for j in xrange(M+1):
        _exist[i*i+j*j] = 1

sequences = []
c = 0
m = M*M
for b in xrange(1, (2*M*M/(N-1))+1):
    for a in xrange(m):
        if not _exist[a]:
            continue
            
        #if a+(N-1)*b > 2*M*M:
        #    break
        #c += 1
        #flag = True
        #for n in xrange(1, N):
        #    if not _exist[a+n*b]:
        #        flag = False
        #        break
        #if flag:
        #    sequences.append([a,b])

print c
print (2*M*M/(N-1))+1
print sequences
#with open("ariprog.out", "w") as fout:
#    if not sequences:
#        fout.write("NONE" + "\n")
#    else:
#        for i, j in sequences:
#            fout.write(str(i) + ' ' + str(j) + '\n')

