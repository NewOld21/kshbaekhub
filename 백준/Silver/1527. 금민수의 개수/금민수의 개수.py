import sys
from collections import deque
x, y = map(int, sys.stdin.readline().split())

cnt = 0
num = deque()
num.append(4)
num.append(7)
while num :
    n = num.popleft()
    if x <= n <= y :
        cnt += 1
    if n * 10 + 4 <= y :
        num.append(n * 10 + 4)
    if n * 10 + 7 <= y :
        num.append(n * 10 + 7)

print(cnt)


