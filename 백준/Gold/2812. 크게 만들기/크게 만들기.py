import sys
from collections import deque
N, K = map(int, sys.stdin.readline().split())
num = sys.stdin.readline()
stack = deque()
for i in range(N) :
    while stack and stack[-1]<num[i] and K>0 :
        stack.pop()
        K -= 1
    stack.append(num[i])
if K>0 :
    for i in range(K) :
        stack.pop()
print(''.join(stack))