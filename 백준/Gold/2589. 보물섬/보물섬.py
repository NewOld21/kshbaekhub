import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
maps = []
for _ in range(N) :
    maps.append(list(sys.stdin.readline().strip()))

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(i,j) :
    q = deque()
    q.append([i,j])
    check = [[-1 for _ in range(M)] for _ in range(N)]
    check[i][j] = 0
    cnt = 0
    while q : 
        x, y = q.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < N and 0<= ny < M and maps[nx][ny] == 'L' and check[nx][ny] == -1 :
                q.append([nx,ny])
                check[nx][ny] = check[x][y] + 1
                cnt = max(cnt, check[nx][ny])
    return cnt

result = 0
for i in range(N) :
    for j in range(M) :
        if maps[i][j] == 'L' :
            result = max(bfs(i,j), result)
 
print(result)