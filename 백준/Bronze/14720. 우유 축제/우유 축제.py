import sys
N = int(sys.stdin.readline())
milk = list(map(int, sys.stdin.readline().split()))
type = [0,1,2]
cnt = 0 
for i in milk :
    if i == type[cnt%3] :
        cnt += 1

print(cnt)