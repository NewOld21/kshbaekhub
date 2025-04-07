import sys
N = int(sys.stdin.readline())
m = list(map(int,sys.stdin.readline().split() ))

type = [0,1,2]
cnt = 0
t=0
for i in range(N) :
    if m[i] == type[t%3] :
        cnt += 1
        t += 1

print(cnt)