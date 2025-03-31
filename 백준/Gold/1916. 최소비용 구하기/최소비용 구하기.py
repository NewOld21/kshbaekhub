import sys
import heapq
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
bus = [[] for i in range(N+1)]
ans= [sys.maxsize] * (N+1)
for i in range(M) :
    a, b, c = map(int, sys.stdin.readline().split())
    bus[a].append([c,b])

S, E = map(int, sys.stdin.readline().split())
q = []
check = [0] * (N+1)
ans[S] = 0
heapq.heappush(q, [0,S])

while q: 
    w, e = heapq.heappop(q)
    if check[e] == 1 :
        continue
    check[e] = 1
    for i in bus[e] :
        ans[i[1]] = min(ans[i[1]], ans[e] + i[0])
        heapq.heappush(q, [ans[i[1]], i[1]])
print(ans[E])