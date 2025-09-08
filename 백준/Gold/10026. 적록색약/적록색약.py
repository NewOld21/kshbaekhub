import sys
from collections import deque
sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline())
color = []

for _ in range(N) :
    color.append(list(sys.stdin.readline().strip()))

dx = [0,0,1,-1]
dy = [1,-1,0,0]

cnt1 = 0
cnt2 = 0

q2 = deque()
check1 = [[0 for _ in range(N)] for _ in range(N)]
check2 = [[0 for _ in range(N)] for _ in range(N)]

def dfs1(x,y,c) :
    q1 = deque()
    q1.append([x,y])
    while q1 :
        a, b = q1.popleft()
        for i in range(4) :
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<=nx<N and 0<=ny<N and check1[nx][ny] == 0 and color[nx][ny] == c :
                check1[nx][ny] = 1
                dfs1(nx,ny,c)


def dfs2(x,y,c) :
    q2 = deque()
    q2.append([x,y])
    while q2 :
        a, b = q2.popleft()
        for i in range(4) :
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<=nx<N and 0<=ny<N and check2[nx][ny] == 0 :
                if c == 0 :
                    if color[nx][ny] != 'B' :
                        check2[nx][ny] = 1
                        dfs2(nx,ny,c)
                else : 
                    if color[nx][ny] == 'B' :
                        check2[nx][ny] = 1
                        dfs2(nx,ny,c)
    

for i in range(N) :
    for j in range(N) :
        if check1[i][j] == 0 :
            check1[i][j] = 1
            dfs1(i,j,color[i][j])
            cnt1 += 1
        if check2[i][j] == 0 :
            check2[i][j] = 1
            if color[i][j] == 'B' :
                dfs2(i,j,1)
            else :
                dfs2(i,j,0)
            cnt2 += 1

print(cnt1, cnt2)


