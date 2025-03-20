import sys
from collections import deque
N = int(sys.stdin.readline())
q = deque()
cnt = 0
for _ in range(N) :
    n = sys.stdin.readline().split()
    if n[0] == 'push' : 
        q.append(int(n[1]))
        cnt +=1
    elif n[0] == 'pop' :
        if cnt == 0 :
            print(-1)
        else :
            print(q.popleft())
            cnt -=1
    elif n[0] == 'size' :
        print(cnt)
    elif n[0] == 'empty' :
        if cnt == 0 :
            print(1)
        else :
            print(0)
    elif n[0] == 'front' :
        if cnt == 0 :
            print(-1)
        else :
            print(q[0])
    else :
        if cnt == 0 :
            print(-1)
        else :
            print(q[cnt-1])