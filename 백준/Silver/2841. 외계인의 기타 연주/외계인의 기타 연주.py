import sys, heapq

N, P = map(int, sys.stdin.readline().split())

line = []
fret = []



for _ in range(N) :
    l, f = map(int, sys.stdin.readline().split())
    line.append(l)
    fret.append(f)

guitar= [[] for _ in range(N) ]
cnt = 0

for i in range(N) :
    l = line[i]
    f = fret[i]
    if guitar[l] :
        while guitar[l] : 
            cur = -heapq.heappop(guitar[l])
            if cur < f :
                heapq.heappush(guitar[l], -cur)
                break
            elif cur == f : 
                cnt -= 1
                break
            else :
                cnt += 1
    heapq.heappush(guitar[l], -f)
    cnt += 1

print(cnt)