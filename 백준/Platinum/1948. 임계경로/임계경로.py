import  sys
from collections import deque
import heapq
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
graph = [[]for _ in range(N+1)]
in_degree = [0] * (N+1) 
for i in range(M) :
    a,b,c = map(int, sys.stdin.readline().split())
    in_degree[b] += 1
    graph[a].append([b, c])
S, E = map(int, sys.stdin.readline().split())

q = deque()

q.append(S)

max_r = 0
max_t = [0] * (N+1)
ans = [] 
check = [[] for _ in range(N+1)]
while q:
    n = q.popleft()
    if n == E :
        continue
    for e, c in graph[n] :
        if max_t[e] < max_t[n]+ c :
            check[e] = [n]  # 지나온 도로 초기화
            max_t[e] = max_t[n] + c
        elif max_t[e] == max_t[n]+ c :
            check[e].append(n) # 지나온 도로 추가
        in_degree[e] -= 1
        if in_degree[e] == 0 :
            q.append(e)

q.append(E)
cnt = set()
while q :           # 지나온 도로 개수 구하기
    n = q.popleft()
    for i in check[n] :
        if (n,i) not in cnt :
            cnt.add((n,i))
            q.append(i)

print(max_t[E])
print(len(cnt))