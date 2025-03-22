import sys
import heapq
N = int(sys.stdin.readline())
q = []
for _ in range(N) :
    n = int(sys.stdin.readline())
    heapq.heappush(q,n)
cnt = 0
if N==1 :
    cnt = 0
elif N ==2 :
    cnt = q[0]+q[1]
else :
    while len(q)>1 :
        a = heapq.heappop(q)
        b = heapq.heappop(q)
        cnt += a+b
        heapq.heappush(q,a+b)
print(cnt)