import sys
N = int(sys.stdin.readline())
stack = []
for _ in range(N) :
    n = int(sys.stdin.readline())
    stack.append(n)
h = stack.pop()
cnt = 1
for i in range(len(stack)) :
    n = stack.pop()
    if n>h :
        cnt +=1
        h=n
print(cnt)