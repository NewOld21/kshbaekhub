import sys
N, M  = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]

for i in range(M) :
    s, e = map(int, sys.stdin.readline().split())
    graph[s].append(e)

dist = [[sys.maxsize]*(N+1) for _ in range(N+1)]

for i in range(N+1) :
    dist[i][i] = 0
    for j in graph[i] :
        dist[i][j] = 1

for k in range(1, N+1) :
    for i in range(1, N+1) :
        for j in range(1, N+1) :
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
cnt = 0
for i in range(1, N+1) :
        cnt1 = (N+1)/2
        for j in range(1, N+1) :
            if dist[i][j] != sys.maxsize and i != j :
                  cnt1 -= 1
        if cnt1 <= 0 :
             cnt += 1
    
for i in range(1, N+1) :
        cnt2 = (N+1)/2
        for j in range(1, N+1) :
            if dist[j][i] != sys.maxsize and i != j :
                  cnt2 -= 1
        if cnt2 <= 0 :
             cnt += 1

print(cnt)