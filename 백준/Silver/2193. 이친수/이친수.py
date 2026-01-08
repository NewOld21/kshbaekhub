import sys
from collections import deque

N = int(sys.stdin.readline())

Lee = [0] * (N+1)
Lee[1] = 1

if N > 1 :
    for i in range(2,N+1) :
        Lee[i] = Lee[i-1] + Lee[i-2]


print(Lee[N])