import sys
sys.setrecursionlimit(10**6)
N = int(sys.stdin.readline())
tree = [[] for i in range(N+1)]
for _ in range(N-1) :
    a, b = map(int, sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)

check = [0] * (N+1)
def dfs(n,p) :
    check[n] = p
    for i in tree[n] :
        if check[i] == 0 :
            dfs(i,n)
dfs(1,1)
for i in range(2,N+1) :
    print(check[i])
