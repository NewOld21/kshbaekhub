import sys
from collections import deque

N, L, R = map(int, sys.stdin.readline().split())

coun = []

for _ in range(N) :
    c = list(map(int, sys.stdin.readline().split()))
    coun.append(c)

dx = [0,0,1,-1]
dy = [1,-1,0,0]

pos = True
ans = -1
while pos :
    check = [[0 for _ in range(N)] for _ in range(N)]
    ans += 1
    pos = False
    for i in range(N) :
        for j in range(N) :
            if check[i][j] == 0 :
                q = [[i,j]]
                set_q = [[i,j]]
                check[i][j] = 1
                cnt = coun[i][j]
                while q :
                    x,y = q.pop()
                    for r in range(4) :
                        nx = x + dx[r]
                        ny = y + dy[r]
                        
                        if 0<= nx <N and 0<= ny < N and check[nx][ny] == 0 :
                            if L <= abs(coun[x][y] - coun[nx][ny]) <= R :
                                check[nx][ny] = 1
                                cnt += coun[nx][ny]
                                q.append([nx,ny])
                                set_q.append([nx,ny])

                if len(set_q) > 1 :
                    for x,y in set_q :
                        coun[x][y] = cnt//len(set_q)
                    pos = True

print(ans)