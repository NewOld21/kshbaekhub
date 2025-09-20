import sys
sys.setrecursionlimit(10**6)
N, M = map(int, sys.stdin.readline().split())

vill = []

for _ in range(N) :
    vill.append(list(map(int, sys.stdin.readline().split())))

chicken = []
home = []

for i in range(N) :
    for j in range(N) :
        if vill[i][j] == 1 :
            home.append([i,j])
        elif vill[i][j] == 2 :
            chicken.append([i,j])

ans = []

def chicken_far(idx, n, check) :
    if n == M :
        cnt = 0
        for a,b in home :
            mn = sys.maxsize
            for i in range(len(chicken)) :
                if check[i] == 1 :
                    x,y = chicken[i]
                    mn = min(mn, abs(a-x) + abs(b-y))
            cnt += mn
        ans.append(cnt)
        return
    else :
        for i in range(idx+1, len(chicken)) :
            check[i] = 1
            chicken_far(i,n+1,check)
            check[i] = 0


for i in range(len(chicken)) :
    check = [0 for _ in range(len(chicken))]
    check[i] = 1
    chicken_far(i,1,check)

print(min(ans))