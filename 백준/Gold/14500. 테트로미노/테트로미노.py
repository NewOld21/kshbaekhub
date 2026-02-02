import sys

N, M = map(int, sys.stdin.readline().split())

paper = []

for _ in range(N) :
    paper.append(list(map(int, sys.stdin.readline().split())))

mx = [0]

num_mx = max(map(max, paper))

check = [[0 for _ in range(M)] for _ in range(N)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]


def tetro(x,y, s, cnt) :
    if s + num_mx * (4 - cnt) <= mx[0]:
        return
    if cnt == 4 :
        if mx[0] < s :
            mx[0] = s
        return
    
    check[x][y] = 1 
    near = []
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0<= ny < M :
            near.append(paper[nx][ny])
            if check[nx][ny] == 0 :
                tetro(nx,ny,s+paper[nx][ny],cnt+1)
            
    
    if cnt == 1 and len(near) >= 3:
        if len(near) == 4 :
            near.sort()
            near[0]= 0
        near_sum = paper[x][y] + sum(near)
        if mx[0] < near_sum :
            mx[0] = near_sum
    check[x][y]= 0



for i in range(N) :
    for j in range(M) :
        tetro(i,j,paper[i][j],1)

print(mx[0])