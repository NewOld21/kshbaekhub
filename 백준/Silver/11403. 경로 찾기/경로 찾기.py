import sys
N = int(sys.stdin.readline())
maps = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

for i in range(N) :
    for j in range(N) :
        for r in range(N) :
            if maps[j][i] == 1 and maps[i][r] == 1 :
                maps[j][r] = 1
for m in maps :
    print(*m)