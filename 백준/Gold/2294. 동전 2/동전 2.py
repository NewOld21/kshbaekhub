import sys
from collections import deque 
N, K = map(int, sys.stdin.readline().split())
coin = []
q = deque()
for i in range(N) :
    c = int(sys.stdin.readline())
    if c>K :
        continue
    coin.append(c)
    q.append([c,1])
sum = [sys.maxsize] * (K+1)
def bfs() :
    mi = sys.maxsize
    while q :
        k,n = q.popleft()
        sum[k] = n
        if k == K :
            mi = min(mi, n)
        else :
            for i in range(len(coin)) :
                if k+coin[i] <=K and n+1<mi:
                    if sum[k+coin[i]] > n+1 :
                        sum[k+coin[i]] = n+1
                        q.append([k+coin[i], n+1])
    return mi

ans = bfs()
if ans == sys.maxsize :
    ans = -1
print(ans)
