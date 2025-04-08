import sys
import heapq
for _ in range(int(sys.stdin.readline())) :
    N = int(sys.stdin.readline())
    a_grade = []
    for i in range(N) :
        a, b = map(int, sys.stdin.readline().split())
        heapq.heappush(a_grade,[a,b])

    x,y= heapq.heappop(a_grade)
    cnt = 1
    for _ in range(N-1) :
        ax,ay = heapq.heappop(a_grade)
        if ay<y :
            cnt +=1
            x, y = ax , ay
    print(cnt)