import sys
n = []
for i in range(int(input())) :
    a = int(sys.stdin.readline())
    n.append(a)
n.sort()
for q in n :
    print(q)