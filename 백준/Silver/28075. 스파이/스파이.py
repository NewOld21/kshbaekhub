import sys
N, M = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

q = [[0,0,-1]]
cnt = 0
while q :
    n, m, x  = q.pop()
    if n == N :
        if M <= m :
            cnt += 1
        continue
    for i in range(2) :
        for j in range(3) :
            if i == 0 :
                if j == x :
                    q.append([n+1,m+(A[j]//2),j])
                else :
                    q.append([n+1,m+A[j],j])
            else :
                if j == x :
                    q.append([n+1,m+(B[j]//2),j])
                else :
                    q.append([n+1,m+B[j],j])

print(cnt)