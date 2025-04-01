import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())
maps = [list(map(str, list(sys.stdin.readline().strip()))) for _ in range(N)]
water_table = [[2500]* (M) for _ in range(N)]
start = []
water = deque()
for i in range(N) :
    for j in range(M) :
        if maps[i][j] == 'S' :
            start = [i,j]
        if maps[i][j] == '*' :
            water.append([i,j,0])


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
ans = 'KAKTUS'


while water : 
    a, b, t = water.popleft()
    water_table[a][b] = t
    for i in range(4) :
        nx = a + dx[i]
        ny = b + dy[i]
        if 0 <= nx < N and 0 <= ny < M :
            if maps[nx][ny] == '.' and water_table[nx][ny] > t+1 :
                water_table[nx][ny] = t+1
                water.append([nx, ny, t+1])


q = deque([(start[0], start[1], 0)])


visited = [[False]* (M) for _ in range(N)]
visited[start[0]][start[1]] = True
ans = "KAKTUS"

while q:
    x, y, t = q.popleft()

    if maps[x][y] == 'D': 
        ans = t
        break

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < N and 0 <= ny < M:
            if (maps[nx][ny] == 'D') or (maps[nx][ny] == '.' and water_table[nx][ny] > t + 1):
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny, t + 1))

print(ans)