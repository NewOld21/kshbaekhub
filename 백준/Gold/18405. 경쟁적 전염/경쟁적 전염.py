import sys
from collections import deque
import heapq
N, K = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
S, X, Y = map(int, sys.stdin.readline().split())
X = X -1
Y = Y -1

q = []
for i in range(N) :
    for j in range(N) :
        if graph[i][j] != 0 :
            heapq.heappush(q,[0,graph[i][j],i,j])

dx = [0,0,1,-1]
dy = [1,-1,0,0]
cnt = 0
while q : 
    h, t, a, b = heapq.heappop(q)
    if h == S :
        break
    for i in range(4) :
        nx = a + dx[i]
        ny = b + dy[i]
        if 0<= nx < N and 0<= ny < N :
            if graph[nx][ny] == 0 :
                graph[nx][ny] = t
                heapq.heappush(q,[h+1, t,nx,ny])

print(graph[X][Y])