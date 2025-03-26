import sys
M, N, L = map(int, sys.stdin.readline().split())
Mx = list(map(int, sys.stdin.readline().split()))
Nxy = []
ans = 0
for i in range(N) :
    x,y = map(int, sys.stdin.readline().split())
    Nxy.append([x,y])

for i in range(M) :
    x = Mx[i]
    for j in range(N) :
        nx, ny = Nxy[j][0], Nxy[j][1]
        if Nxy[j][0]>0 and Nxy[j][1]>0 and (abs(x-nx) + ny) <= L :
            ans+= 1
            Nxy[j][0], Nxy[j][1] = -1, -1

print(ans)