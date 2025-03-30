import sys 
import heapq
N = int(sys.stdin.readline())
m = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(N)]

q = []
heapq.heappush(q, [0,0,0])

dx = [0, 0, 1, -1]
dy = [1,-1, 0, 0]

ans = []
def bfs() :

    while q :
        cnt, x, y = heapq.heappop(q)
        if x == N-1 and y == N-1 :
            ans.append(cnt)
            continue
        if -1<x<N and -1<y<N and m[x][y]>-1:
            if m[x][y] == 0 :
                cnt += 1
            m[x][y] = -1
            for i in range(4) :
                heapq.heappush(q, [cnt, (x+dx[i]), (y+dy[i])])


bfs()
print(min(ans))