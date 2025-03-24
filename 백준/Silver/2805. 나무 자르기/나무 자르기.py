import sys
N, M = map(int, sys.stdin.readline().split())
tree = list(map(int, sys.stdin.readline().split()))

pl = 0 
pr = max(tree)

while pl<= pr :
    pc = (pl + pr) // 2
    cut = 0
    for i in range(N) :
        if tree[i] - pc > 0 :
            cut += tree[i] - pc
    if M<=cut :
        pl = pc + 1
    else :
        pr = pc - 1

print(pr)