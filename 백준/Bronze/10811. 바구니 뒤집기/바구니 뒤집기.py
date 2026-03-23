import sys

N, M = map(int, sys.stdin.readline().split())

num = [i for i in range(1,N+1)]

for _ in range(M) :
    x, y = map(int, sys.stdin.readline().split())
    if x == y :
        continue
    re = num[x-1:y:]
    re.reverse()
    for i in range(len(re)) :
        num[i+x-1] = re[i]

print(*num)
