import sys
sys.setrecursionlimit(10**9)
V, E = map(int, sys.stdin.readline().split())

edge = [[0]*(V+1) for _ in range(V+1)] 
for i in range(E) :
    a, b = map(int, sys.stdin.readline().split())
    edge[a][b] = 1
    edge[b][a] = 1

check = [0] * (V+1)
cnt = 0

def dfs(n) :
    check[n] = 1
    for i in range(1, V+1) :
        if edge[n][i] == 1 and check[i] == 0 :
            dfs(i)


for i in range(1,V+1) :
    if check[i]==0 :
        cnt += 1
        dfs(i)

print(cnt)