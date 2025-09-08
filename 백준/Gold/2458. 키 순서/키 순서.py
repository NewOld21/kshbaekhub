import sys
N, M =map(int, sys.stdin.readline().split())
std = [[sys.maxsize for _ in range(N+1)] for _ in range(N+1)]

for _ in range(M) :
    s, e =map(int, sys.stdin.readline().split())
    std[s][e] = 1

for i in range(1, N+1) :
    std[i][i] = 0

for i in range(1,N+1) :   
    for s in range(1, N+1) :
        for e in range(1, N+1) :
            std[s][e] = min(std[s][e], std[s][i] + std[i][e])

ans = N
for i in range(1, N+1) :
    for j in range(1, N+1) :
        if std[i][j] < sys.maxsize or std[j][i] < sys.maxsize :
            continue
        else :
            ans -= 1
            break

print(ans)