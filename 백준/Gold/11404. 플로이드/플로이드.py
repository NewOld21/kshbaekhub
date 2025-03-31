import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

bus = [[sys.maxsize] * (N+1) for _ in range(N+1)]
for i in range(1, N+1) :
    bus[i][i] = 0

for i in range(M) :
    a, b, c = map(int, sys.stdin.readline().split())
    bus[a][b] = min(bus[a][b] ,c)



#플로이드 워샬
for r in range(1, N+1) :
    for i in range(1, N+1) :
        for j in range(1, N+1) :
            bus[i][j] = min(bus[i][j], bus[i][r] + bus[r][j])

#출력
for i in range(1,N+1) :
    for j in range(1,N+1) :
        if bus[i][j] == sys.maxsize :
            print(0, end=' ')
        else :
            print(bus[i][j], end=' ')
    print()