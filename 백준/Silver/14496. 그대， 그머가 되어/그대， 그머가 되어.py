import sys
from collections import deque

a, b = map(int, sys.stdin.readline().split())
N, M = map(int, sys.stdin.readline().split())

num = [[] for _ in range(N+1)]

for _ in range(M) :
    x, y = map(int, sys.stdin.readline().split())
    num[x].append(y)
    num[y].append(x)

q = deque()
q.append([a,0])
check = [0] * (N+1)
check[a] = 1
mn = sys.maxsize

while q :
    n, cnt = q.popleft()
    if n == b :
        mn = min(mn, cnt)
    else :
        for i in num[n] :
            if check[i] == 0 :
                check[i] = 1
                q.append([i,cnt+1])


if mn == sys.maxsize :
    print(-1)
else :
    print(mn)

