import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())
graph = [list(map(str, sys.stdin.readline().strip())) for _ in range(N)]


cnt = 0
dx = [1,-1]
dy = [1,-1]


def dfs(x,y) :
    global cnt
    type = graph[x][y]
    graph[x][y] = 'X'
    if type == '-' :
        for i in range(2) :
            nx = x
            ny = y + dy[i]
            if 0<= nx < N and 0<= ny < M :
                if graph[nx][ny] =='-':
                    dfs(nx,ny)
                
    if type == '|' :
        for i in range(2) :
            nx = x + dx[i]
            ny = y 
            if 0<= nx < N and 0<= ny < M :
                if graph[nx][ny] =='|':
                    dfs(nx,ny)
                
            
for i in range(N) :
    for j in range(M) :
        if graph[i][j] != 'X' :
            dfs(i,j)
            cnt +=1
print(cnt)