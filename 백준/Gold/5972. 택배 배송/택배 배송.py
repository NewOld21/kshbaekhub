import sys
import heapq
N, M = map(int, sys.stdin.readline().split())

road = [[] for _ in range(N+1)]

for _ in range(M) :
    s, e, c = map(int, sys.stdin.readline().split())
    road[s].append([e,c])
    road[e].append([s,c])


check = [sys.maxsize for _ in range(N+1)]
visit = [0 for _ in range(N+1)]
q = []

heapq.heappush(q, [0,1])
check[1] = 0

while q :
    r, cur = heapq.heappop(q)
    if check[cur] < r :
        continue
    for i,j in road[cur] :
        if check[i] > r + j :
            check[i] =  r + j
            heapq.heappush(q,[check[i],i])
   

print(check[-1])
