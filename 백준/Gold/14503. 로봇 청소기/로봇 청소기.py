import sys

N, M = map(int, sys.stdin.readline().split())

x,y,n = map(int, sys.stdin.readline().split())

room = [ ]
for i in range(N) :
    room.append(list(map(int, sys.stdin.readline().split())))

cnt = 0
dx = [-1,0,1,0]
dy = [0,1,0,-1]

back = [[1,0],[0,-1], [-1,0],[0,1]]

while (True) :
    if room[x][y] == 0 :
        room[x][y] = 2
        cnt += 1
    clean = 0
    for i in range(4) :
        nn = (n-i-1)
        if nn<0 :
            nn = nn + 4
        nx = x + dx[nn]
        ny = y + dy[nn]
        if room[nx][ny] == 0 : 
            n = nn 
            x = nx
            y = ny
            clean = 1
            break
    if clean>0 :
        continue
    else :
        x = x + back[n][0]
        y = y + back[n][1]
        if room[x][y] == 1 :
            break

print(cnt)