import sys
from collections import deque
import heapq

for _ in range(int(sys.stdin.readline())) :
    N, M = map(int, sys.stdin.readline().split())
    prints = list(map(int, sys.stdin.readline().split()))
    index = [i for i in range(N)]
    max = []
    Q = deque()
    cnt = 0
    for i in range(N) :
        heapq.heappush(max, -prints[i])
        Q.append([prints[i], index[i]])

    while True :
        p = Q.popleft()
        if p[0] == -max[0] :
            cnt +=1
            heapq.heappop(max)
            if p[1] == M :
                break
        else :
            Q.append(p)
    print(cnt)