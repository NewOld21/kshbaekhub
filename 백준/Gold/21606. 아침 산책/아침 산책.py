import sys
N = int(sys.stdin.readline())
place = input()
path = [[] for _ in range(N+1)]
for i in range(1,N) :
    a, b = map(int, sys.stdin.readline().split())
    path[a].append(b)
    path[b].append(a)

def dfs(n) :
    global check, cnt, place
    check[n] = 1
    for i in path[n] :
        if check[i] == 0 :
            check[i] = 1
            if place[i-1] == '1' :
                cnt += 1
                continue
            dfs(i)

cnt = 0
for i in range(1, N+1) :
    if place[i-1] == '1' :
        check = [0] * (N+1)
        dfs(i)
print(cnt)
