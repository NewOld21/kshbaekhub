import sys
s = []
n = [[] for i in range(51)] 
for i in range(int(sys.stdin.readline())) :
    a = input()
    l = len(a)-1
    if n[l].count(a) == 0 :
        n[l].append(a)

for i in n :
    if len(i) != 0 :
        i.sort()
        for j in i :
            print(j)