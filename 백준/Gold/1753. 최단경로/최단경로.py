import sys
import heapq
V, E = map(int, sys.stdin.readline().split())
S = int(sys.stdin.readline())
Node = [[] for _ in range(V+1)]

for i in range(E) :
    a, b, c = map(int, sys.stdin.readline().split())
    Node[a].append([b,c])

ans = [sys.maxsize] * (V+1)
ans[S] = 0
check = [0] * (V+1)
q = []
heapq.heappush(q, [0,S])

while q :
    x,n = heapq.heappop(q)
    if check[n] == 0 :
        check[n] = 1
        for i in Node[n] :
            e, c = i[0], i[1]
            ans[e] = min(ans[e], ans[n] + c)
            heapq.heappush(q,[ans[e],e])

for i in range(1, V+1) :
    if ans[i] == sys.maxsize :
        print('INF')
    else :        
        print(ans[i])