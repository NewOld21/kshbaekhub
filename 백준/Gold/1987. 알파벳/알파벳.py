import sys
N, M = map(int, sys.stdin.readline().split())
graph = [list(sys.stdin.readline().strip())for _ in range(N)]

mx = 0
dx = [0,0,1,-1]
dy = [1,-1,0,0]
use = set()
use.add(graph[0][0])

def dfs(x,y,cnt) :
    global mx
    mx = max(mx, cnt)
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<N and 0<=ny<M :
            if graph[nx][ny] not in use :
                use.add(graph[nx][ny])
                dfs(nx,ny,cnt+1)
                use.remove(graph[nx][ny])

dfs(0,0,1)
print(mx)