import sys
from collections import deque
N = int(sys.stdin.readline())
q = deque()
for i in range(1,N+1) :
    q.append(i)
check = 0
while len(q)>1 :
    if check == 0 :
        check = q.popleft()
    else :
        q.append(q.popleft())
        check = 0

print(q.popleft())