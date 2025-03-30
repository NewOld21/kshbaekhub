import sys
N, M = map(int, sys.stdin.readline().split())
maze = [[0]*(M+1) for _ in range(N+1)]

for i in range(1,N+1) :
    num = input()
    for j in range(1, M+1) :
        maze[i][j] = int(num[j-1])

dx = [1, 0,-1,0]
dy = [0, 1, 0, -1]
ans = []
q = [[1,1,0]]
def bfs() :
    while q :
        x, y, cnt = q.pop(0)
        if x==N and y==M :
            cnt +=1 
            ans.append(cnt)
            return 
        if 0<x<=N and 0<y<=M and maze[x][y] == 1:
            maze[x][y] = 0
            cnt +=1
            for i in range(4) :
                q.append([(x + dx[i]), (y + dy[i]), cnt])
bfs()
if ans :
    print(min(ans))
else :
    print(-1)