import sys
from collections import deque
N, M, K, S = map(int, sys.stdin.readline().split())
citys = [[] for _ in range(N+1)]

for i in range(M) :
    a, b = map(int, sys.stdin.readline().split())
    citys[a].append(b)

q = deque([(S,K)]) 
check = [0] * (N+1)
check[S] = 1
ans = []

def bfs() :
    while q:
        n, k = q.popleft()
        if k == 0 :
            ans.append(n)
            continue
        for i in citys[n] :
            if check[i] == 0:
                check[i] = 1
                q.append([i,k-1])
bfs()
ans.sort()
if ans :
    for i in ans :
        print(i)
else :
    print(-1)
