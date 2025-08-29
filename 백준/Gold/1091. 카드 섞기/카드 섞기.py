import sys

n = int(sys.stdin.readline())
p = list(map(int, sys.stdin.readline().split()))
ori = p.copy()
s = list(map(int, sys.stdin.readline().split()))
g = [0, 1, 2] * (n // 3)
new = [0] * n
cnt = 0

while p != g:
    for i in range(n):
        new[s[i]] = p[i]
    p = new.copy()
    new = [0] * n
    cnt += 1
    if ori == p:
        cnt = -1
        break

print(cnt)
