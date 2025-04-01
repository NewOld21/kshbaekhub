import sys
from collections import deque
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
in_d = [0] * (N+1)
graph = [[] for _ in range(N+1)]
ans = [0] * (N+1)
ind = set()
for _ in range(M) :
    a, b, c = map(int, sys.stdin.readline().split())
    in_d[b] += 1
    graph[a].append([c, b])
    ind.add(a)
  

q = deque()
for i in range(1, N+1) :
    if in_d[i] == 0 :
        q.append(i)

while q :
    n = q.popleft()
    for i in graph[n] :
        need ,num = i[0], i[1]
        if ans[n] == 0 :
            ans[num] = need
        else :
            ans[num] += (ans[n] * need)
        
        in_d[num] -= 1
        if in_d[num] == 0 :
            q.append(num)


for i in range(1, N+1) :
    if i in ind :
        continue
    print(f'{i} {ans[i]}')