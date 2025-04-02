import sys
import heapq
N = int(sys.stdin.readline())
graph = [list(map(int,sys.stdin.readline().strip())) for _ in range(N)]
edge = [[] for _ in range(N)]
in_degree = [0] * N
for i  in range(N) :
    for j in range(N) :
        if graph[i][j] == 1 :
            in_degree[i] += 1
            edge[j].append(i)

q = []
for i in range(N) :
    if in_degree[i] == 0 :
        heapq.heappush(q, -i)
result = [0] * N
cnt = N
if len(q) == 0:
    result = -1
while q :
    n = -heapq.heappop(q)
    result[n] = cnt
    cnt -= 1
    for num in edge[n] :
        in_degree[num] -= 1
        if in_degree[num] == 0 :
            heapq.heappush(q, -num)

if result == -1 :
    print(-1)
else :
    print(*result)