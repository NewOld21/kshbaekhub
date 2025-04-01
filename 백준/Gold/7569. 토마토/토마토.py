import sys
from collections import deque
N, M, H = map(int, sys.stdin.readline().split())
tom_box = [[[0 for _ in range(N)] for _ in range(M)]for _ in range(H)]
check = []
q = deque()
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dh = [0, 0, 0, 0, 1, -1]
cnt = [0]

for h in range(H) :
    for m in range(M) :
        tom = list(map(int, sys.stdin.readline().split()))
        for n in range(N) :
            if tom[n] == 1 :
                q.append([h,m,n,1])
            tom_box[h][m][n] = tom[n]
ans = 0
while q :
    h, m, n, c = q.popleft()
    ans = max(ans,c)
    for i in range(6) :
        if 0 <= (h + dh[i]) < H and 0<= (m + dy[i]) < M and 0<= (n + dx[i]) < N :
            if tom_box[h+dh[i]][m+dy[i]][n+dx[i]] == 0 :
                tom_box[h+dh[i]][m+dy[i]][n+dx[i]] = c+1
                q.append([h+dh[i], m+dy[i], n+dx[i], c+1])
ans = ans-1         

for i in range(H) :
    for j in range(M) :
        if 0 in tom_box[i][j] :
            ans = -1
            break
       
print(ans)
