import sys
import heapq

N = int(sys.stdin.readline())

arr = []
for _ in range(N) :
    x = int(sys.stdin.readline())
    if x == 0 :
        if arr :
            ans = heapq.heappop(arr)
            print(ans[-1])
        else :
            print(0)
    elif x < 0  :
        heapq.heappush(arr, [-x, x])

    else :
        heapq.heappush(arr, [x, x])
