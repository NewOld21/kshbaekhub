import sys
sys.setrecursionlimit(10**6)

N, M = map(int, sys.stdin.readline().split())

tree = [[] for _ in range(N+1)]

for _ in range(N-1) : 
    s, e, c = map(int, sys.stdin.readline().split())
    tree[s].append([e,c])
    tree[e].append([s,c])


def dfs(e, n, c, check) : 
    if n==e :
        return c
    ans = 0
    for x,r in tree[n] :
        if check[x] == 0 :
            check[x] = 1
            ans += dfs(e, x, c+r, check)
    return ans

for _ in range(M) :
    a, b = map(int, sys.stdin.readline().split())
    check = [0 for _ in range(N+1)]
    check[a] = 1
    print(dfs(b, a, 0, check))
   