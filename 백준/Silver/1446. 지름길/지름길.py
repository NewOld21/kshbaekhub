import sys
import heapq
N, D = map(int, sys.stdin.readline().split())

road = [[] for _ in range(D+1)]
distance = [sys.maxsize for _ in range(D+1)]
distance[0] = 0
for _ in range(N) :
    x,y,z = map(int, sys.stdin.readline().split())
    if y <= D : 
        road[x].append([y,z])

for i in range(0,D+1) :
    if i > 0 :
        distance[i] = min(distance[i], distance[i-1] + 1)
    for e,w in road[i] :
        distance[e] = min(distance[i] + w, distance[e])


print(distance[-1])



