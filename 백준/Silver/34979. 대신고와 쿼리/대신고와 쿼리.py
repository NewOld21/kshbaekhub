import sys

N, Q = map(int, sys.stdin.readline().split())

floor = []
cls = [[0 for _ in range(N+1)] for _ in range(5)]
dx = [0,0,-1,1]
dy = [1,-1,0,0]
for _ in range(Q) :
    t = list(map(int, sys.stdin.readline().split()))
    if t[0] == 1 :
        a, b = t[1], t[2]
        cls[a][b] += 1
        for i in range(4) :
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 < nx < 5 and 0 < ny < N+1 :
                cls[nx][ny] += 1
    else :
        f = t[1]
        mx = max(cls[f])
        for x in range(1, N+1) :
            if mx == cls[f][x] :
                print(x)
                break
x, y = 0,0
mx = 0
for i in range(1,5) :
    mxf = max(cls[i])
    mx = max(mx, mxf)

for x in range(1,5) :
    for y in range(1,N+1) :
        if mx == cls[x][y] :
            print(x,y) 
            mx = -1
            break
    if mx == -1 :
        break