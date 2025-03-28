import sys
sys.setrecursionlimit(10**9)
N = int(sys.stdin.readline())
place = input()
path = [[] for _ in range(N+1)]
check = [0] * (N+1)
for i in range(1,N) :
    a, b = map(int, sys.stdin.readline().split())
    path[a].append(b)
    path[b].append(a)

def dfs(n) :
    res = 0
    for i in path[n] :
        if place[i-1] == '0' :
            if check[i] == 0 :
                check[i] = 1
                res += dfs(i)
        else :
            res += 1
    return res
            
ans = 0
for i in range(1, N+1) :
    if place[i-1] == '0' :
        if check[i] == 0 :
            check[i] = 1
            cnt = dfs(i)
            ans += cnt * (cnt-1)
            dfs(i)
    else :
        for j in path[i] :
            if place[j-1] == '1' :
                ans +=1
print(ans)