import sys
import heapq

N = int(sys.stdin.readline())

sea = []

for _ in range(N) :
    sea.append(list(map(int, sys.stdin.readline().split())))

dx = [0,0,-1,1]
dy = [1,-1,0,0]

fish = [[] for _ in range(7)]

shark = [0,0,2,2] ## x좌표, y좌표, 크기, 먹이

for i in range(N) :
    for j in range(N) :
        if sea[i][j] == 9 :
            shark[0], shark[1] = i,j


def bfs(x,y) :
    global shark
    check = [[0 for _ in range(N)] for _ in range(N)] 
    q = []
    heapq.heappush(q, [0,x, y])
    check[shark[0]][shark[1]] = 1

    while q : 
        c,a,b = heapq.heappop(q)

        if 0 < sea[a][b] < shark[2] :
            return [c,a,b]
        
        for i in range(4) :
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<=nx<N and 0<=ny<N and check[nx][ny] == 0 and sea[nx][ny] <= shark[2]:
                check[nx][ny] = 1
                heapq.heappush(q,[c+1,nx,ny])

    return [-1]

ans = 0

while True :
    cnt = bfs(shark[0],shark[1])
    if cnt[0] == -1 :
        break
    ans += cnt[0]
    sea[shark[0]][shark[1]] = -1
    shark[0], shark[1] = cnt[1], cnt[2]
    sea[cnt[1]][cnt[2]] = -1
    if shark[3] - 1 == 0 :
        shark[2] += 1
        shark[3] = shark[2]
    else :
        shark[3] -= 1

print(ans)