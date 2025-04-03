import sys
import heapq
N = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]

cnt = 2
dx = [0,0,1,-1]
dy = [1,-1,0,0]
def dfs(x,y) :
    global cnt, num
    type = graph[x][y]
    graph[x][y] = cnt
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<= nx < N and 0<= ny < N :
            if type == graph[nx][ny] :
                dfs(nx,ny)
                num +=1
q = []
for i in range(N) :
    for j in range(N) :
        if graph[i][j] == 1 :
            num = 1
            dfs(i,j)
            q.append(num)
            cnt +=1
q.sort()
print(cnt-2)
for i in q :
    print(i)