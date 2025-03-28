import sys
from queue import PriorityQueue  #우선순위 큐 사용

sys.setrecursionlimit(10**9)

V, E = map(int,sys.stdin.readline().split())
edge = PriorityQueue()
parent = [i for i in range(V+1)] 
for i in range(E) :
    a, b, c = map(int, sys.stdin.readline().split())
    edge.put((c,a,b)) # 가중치를 제일 앞으로  => 가중치가 작은 것부터 꺼낼 예정

def find(a) :   
    if a == parent[a] :
        return a
    else :
        parent[a] = find(parent[a])
        return parent[a]
    
def union(a,b) :
    a = find(a)
    b = find(b)

    if a != b :
        parent[b] = a

cnt = 0
min = 0

while cnt < V-1 :
    c, start, end = edge.get()

    if find(start) != find(end) :
        union(start, end)
        cnt += 1
        min += c

print(min)