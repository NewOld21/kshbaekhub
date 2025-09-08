import sys, copy
from collections import deque

N, M = map(int, sys.stdin.readline().split())
maps = []
for _ in range(N) :
    maps.append(list(map(int, sys.stdin.readline().split())))

dx = [0,0,-1,1]
dy = [1,-1,0,0]


def bfs() :
    global ans
    q = deque()
    cnt = 0
    mapss = copy.deepcopy(maps)
    for i in range(N) :
        for j in range(M) :
            if mapss[i][j] == 2 :
                q.append([i,j])  
            elif mapss[i][j] == 0 : 
                cnt += 1

    while q : 
        x, y = q.popleft()
        if mapss[x][y] == 2 :
            for r in range(4) :
                nx = x + dx[r]
                ny = y + dy[r]
                if 0<=nx<N and 0<=ny<M and mapss[nx][ny] == 0 :
                    mapss[nx][ny] = 2
                    q.append([nx,ny]) 
                    cnt -= 1
    
    ans = max(ans, cnt)
    

def wall(n) :
    if n == 3 :
        bfs()
        return

    for i in range(N) :
        for j in range(M) :
            if maps[i][j] == 0 :
                maps[i][j] = 1
                wall(n+1)
                maps[i][j] = 0


ans = 0
wall(0)


print(ans)

