import sys
sys.setrecursionlimit(10**9)
def bfs() :
    global checkb, b, q
    while q :
        cur = q.pop(0)
        b.append(cur)
        for i in range(1, N+1) :
            if checkb[i]==0 and tree[cur][i] == 1 :
                checkb[i] = 1
                q.append(i)
def dfs(n) :
    global checkd, d
    checkd[n] = 1
    d.append(n)
    for i in range(1, N+1) :
        if checkd[i]==0 and tree[n][i] == 1 :
            dfs(i)



N, M, V = map(int, sys.stdin.readline().split())

tree = [[0] *(N+1) for _ in range(N+1)] 

for _ in range(M) :
    a, b = map(int, sys.stdin.readline().split())
    tree[a][b] = 1
    tree[b][a] = 1

d = []
checkd = [0] * (N+1)
dfs(V)

checkb = [0] * (N+1)
q = [V]
checkb[V] = 1
b = []
bfs()

print(*d)
print(*b)