import sys
from collections import deque
N, K = map(int, sys.stdin.readline().split())

q = []
ans = []
for i in range(1,N+1) :
    q.append(i)
check = K-1
while len(q)>0 :
    n =q.pop(check)
    ans.append(n)
    check +=K-1
    while check >= len(q) and len(q)!=0 :
        check = check - len(q)

print(f"<{', '.join(map(str,ans))}>")