import sys
N, K = map(int,sys.stdin.readline().split())
q = [[0,0]]
for _ in range(N) :
    w,v = map(int, sys.stdin.readline().split())
    q.append([w,v])

dp = [[0]*(K+1) for _ in range(N+1)]

for i in range(N+1):
    w,v = q[i]
    for k in range(K+1): 
        if k>=w :
            dp[i][k] = max(dp[i-1][k], dp[i-1][k-w] + v) 
        else :
            dp[i][k] = dp[i-1][k]

print(dp[N][K]) 