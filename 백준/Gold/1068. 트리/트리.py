import sys

N = int(sys.stdin.readline())
P = list(map(int, sys.stdin.readline().split()))
D = int(sys.stdin.readline())

tree = [[] for _ in range(N)]
top = -1

for i in range(N) :
    if i == D :
        continue
    root = P[i]
    if root > -1 and root != D:
        tree[root].append(i)
    if root == -1 and i !=D:
        top = i

cnt = 0

if top > -1 :
    q = [top]

    while q :
        t = q.pop()
        if tree[t] :
            for i in tree[t] :
                q.append(i)
        else :
            cnt += 1
print(cnt)