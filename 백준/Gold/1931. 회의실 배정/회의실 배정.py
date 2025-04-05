import sys 
import heapq
N = int(sys.stdin.readline())
time = []
for _  in range(N) :
    s, e = map(int, sys.stdin.readline().split())
    heapq.heappush(time, [e,s])

end = 0
cnt = 0
while time : 
    e,s = heapq.heappop(time)
    if end <= s :
        end = e  
        cnt += 1
print(cnt)
    