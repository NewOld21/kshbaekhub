import sys, heapq

N = int(sys.stdin.readline())
cls = []
for _ in range(N) :
    s, e = map(int, sys.stdin.readline().split())
    heapq.heappush(cls, [s,e])

room = []
cnt = 1
while cls :
    start, end = heapq.heappop(cls)

    if room :
        e = heapq.heappop(room)
        if e > start :
            heapq.heappush(room,e)
            cnt += 1
        heapq.heappush(room,end)
    else :
        heapq.heappush(room, end)

print(cnt)