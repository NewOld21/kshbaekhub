import sys
from collections import deque

N = int(sys.stdin.readline())
line = deque(map(int, sys.stdin.readline().split()))
space = deque()
cnt = 1
while N > cnt : 
    if cnt in line :
        n = line.popleft()
        if n == cnt :
            cnt += 1
            continue
        space.append(n)

    elif cnt in space : 
        n = space.pop()
        if n == cnt :
            cnt += 1
            continue
        else : 
            break

if cnt == N :
    print('Nice')
else :
    print('Sad')