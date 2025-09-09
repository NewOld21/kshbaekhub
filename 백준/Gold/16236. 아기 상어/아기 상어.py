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
        else :
            fish[sea[i][j]].append([i,j])

def bfs(x,y) :
    global shark
    check = [[0 for _ in range(N)] for _ in range(N)] 
    q = []
    heapq.heappush(q, [0,shark[0], shark[1]])
    check[shark[0]][shark[1]] = 1

    while q : 
        c,a,b = heapq.heappop(q)

        if a == x and b == y :
            return c
        
        for i in range(4) :
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<=nx<N and 0<=ny<N and check[nx][ny] == 0 and sea[nx][ny] <= shark[2]:
                check[nx][ny] = 1
                heapq.heappush(q,[c+1,nx,ny])

    return -1

ans = 0

while True :
    size = shark[2] - 1
    mn_x, mn_y = 21, 21
    mn = sys.maxsize
    if size > 6 :
        size = 6
    for i in range(1,size+1) :
        for x,y in fish[i] :
            if sea[x][y] == -1 :
                continue
            cnt = bfs(x,y)
            if cnt == -1 :
                continue
            if mn > cnt :
                mn = cnt
                mn_x, mn_y = x, y
            elif mn == cnt :
                if mn_x > x :
                    mn_x = x
                    mn_y = y
                elif mn_x == x :
                    if mn_y > y :
                        mn_y = y
    
    if mn_x != 21 and mn_y != 21 :
        ans += mn
        sea[shark[0]][shark[1]] = -1
        shark[0], shark[1] = mn_x, mn_y
        sea[mn_x][mn_y] = -1
        if shark[3] - 1 == 0 :
            shark[2] += 1
            shark[3] = shark[2]
        else :
            shark[3] -= 1
    else :
        break


print(ans)