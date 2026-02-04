import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())

q = deque()
q.append(N)
ans = 'NO'
h = set()

while q : 
    heart = q.popleft()
    if heart == M :
        ans = 'YES'
        break
    elif heart < M*2 - 1: 
        continue
    if heart % 2 == 1 and heart//2+1 not in h: 
        h.add(heart//2+1)
        q.append(heart//2+1)
    if heart//2 not in h :
        h.add(heart//2)
        q.append(heart//2)

print(ans)