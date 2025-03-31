import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())
std = [[] for i in range(N+1)]
cnt = [0] * (N+1)   #in-degree
for i in range(M) :
    a, b = map(int, sys.stdin.readline().split())
    std[a].append(b)
    cnt[b] += 1

#  위상 정렬
q = deque()
for i in range(1,N+1) :
    if cnt[i] == 0 :
        q.append(i)

ans = []
while q :
    n = q.popleft()
    print(n, end=' ')
    for j in std[n] :
        cnt[j] -= 1
        if cnt[j] == 0 :
            q.append(j)