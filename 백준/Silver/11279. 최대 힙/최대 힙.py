import sys
import heapq
N = int(sys.stdin.readline())
q = []
for _ in range(N) :
    n = int(sys.stdin.readline())
    if n==0 :
        if q :
            a = (-heapq.heappop(q))
        else :
            a = 0
        print(a)
    else :
        heapq.heappush(q, -n)