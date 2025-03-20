import sys
N = int(sys.stdin.readline())
stack = []
for _ in range(N) :
    n = int(sys.stdin.readline())
    if n==0 :
        if len(stack)>0 :
            stack.pop()
    else :
        stack.append(n)

print(sum(stack))