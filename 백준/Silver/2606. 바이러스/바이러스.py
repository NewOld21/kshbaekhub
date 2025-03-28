import sys

com = int(sys.stdin.readline())
connect = int(sys.stdin.readline())

edge = [[0]*(com+1) for _ in range(com+1)]

for _ in range(connect) :
    a, b = map(int, sys.stdin.readline().split())
    edge[a][b] = 1
    edge[b][a] = 1

q = [1]
check = [0] * (com+1) 
check[1] = 1
cnt = [0]
def bfs() :
    while q:
        n = q.pop(0)
        for i in range(1,com+1) :
            if edge[n][i] == 1 and check[i] == 0 :
                check[i] = 1
                q.append(i)
                cnt[0] +=1

bfs()
print(cnt[0])