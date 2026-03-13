import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

box = []
q = deque()

for i in range(M) :
    b = list(map(int, sys.stdin.readline().split()))
    if 1 in b :
        for j in range(N) :
            if b[j] == 1 :
                q.append([i,j,0])
    box.append(b)

dx = [0,0,1,-1]
dy = [1,-1,0,0]
cnt = 0

while q :
    x, y, n = q.popleft()
    cnt = n
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<M and 0<=ny<N and box[nx][ny] == 0 :
            box[nx][ny] = 1
            q.append([nx,ny,n+1])
for b in box :
    if 0 in b :
        cnt = -1

print(cnt)