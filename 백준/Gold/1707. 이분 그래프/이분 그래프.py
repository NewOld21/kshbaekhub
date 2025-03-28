import sys
sys.setrecursionlimit(10**6)
def dfs(n,c) :
    global check, cnt
    check[n] = c
    for i in tree[n] :
        if check[n] == check[i] :
            cnt = 10
        if check[i] == 0 :
            dfs(i,3-c)
               


T = int(sys.stdin.readline())

for _ in range(T) :
    V, E = map(int, sys.stdin.readline().split())
    tree = [[] for _ in range(V+1)]

    for _ in range(E) :
        a, b = map(int, sys.stdin.readline().split())
        tree[a].append(b)
        tree[b].append(a)

    check = [0] * (V+1)  
    cnt = 0
    for i in range(1,V+1) : #아직 방문을 안한 점은 연결 요소가 아직 안된 점
        if check[i]==0 :
            dfs(i,1)

    print('YES' if cnt == 0 else 'NO')