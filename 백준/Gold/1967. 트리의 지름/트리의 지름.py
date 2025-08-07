import sys
sys.setrecursionlimit(10**6)
N = int(sys.stdin.readline())
tree = [[] for _ in range(N+1)]

for _ in range(N-1) :
    x, y, c = map(int, sys.stdin.readline().split())
    tree[x].append([y,c])
    tree[y].append([x,c])

check = [-1] * (N+1)
check[1] = 0
def dfs(n,x) :
    for i,c in tree[n] : 
        if check[i] == -1 :
            check[i] = x + c
            dfs(i,x+c)
          

dfs(1,0)
mx = max(check)
mx_idx = check.index(mx)
check = [-1] * (N+1)
check[mx_idx] = 0
dfs(mx_idx,0)

print(max(check))