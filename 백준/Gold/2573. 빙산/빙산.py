import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

iceberg = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

ice = deque()  # 빙하

for i in range(N) :
    for j in range(M) :
        if iceberg[i][j] > 0 :
            ice.append([i,j,iceberg[i][j]])
time = [0]

dx = [0, 0, 1, -1]
dy = [1, -1, 0 ,0]

def after_year(n) : #시간에 따른 빙하 높이

    time[0] += 1
    ice_e = []
    for i in range(n) :
        x, y, h = ice.popleft()
        cnt = 0 
        for j in range(4) :
            nx = x + dx[j]
            ny = y + dy[j]

            if 0<= nx <N and 0<= ny < M :
                if iceberg[nx][ny] == 0 :
                    cnt += 1
        if h - cnt > 0 :
            ice.append([x,y,h-cnt])
            iceberg[x][y] = h-cnt
        else :
            ice_e.append([x,y])
    for x,y in ice_e :
        iceberg[x][y] = 0

def dfs(x,y,n) : # 한 빙하를 기준으로 남은 빙하를 다 거치는지 확인
    global check, ice_n
    stack = []
    stack.append([x,y,n])
    while stack :
        xx, yy, nn = stack.pop()
        if nn >= ice_n or (xx,yy) in check :
            continue
        check.add((xx,yy))   #방문 여부 체크
        for i in range(4) :
            nx = xx + dx[i]
            ny = yy + dy[i]
            if 0<= nx <N and 0<= ny < M :
                if iceberg[nx][ny] > 0 :
                        stack.append([nx,ny,nn+1])

ans = 0 
while ice :
    ice_n = len(ice)
    after_year(ice_n)
    if ice :
        ice_n = len(ice)
        check = set()
        dfs(ice[0][0], ice[0][1], 0)
        if len(check) < len(ice) :
            ans = time[0]
            break

print(ans)