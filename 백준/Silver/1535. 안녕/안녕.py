import sys
N = int(sys.stdin.readline())
p = [[]for _ in range(N+1)]

dp = [[0] *100 for _ in range(N+1)]
for _ in range(2) :
    inp = list(map(int, sys.stdin.readline().split()))
    for i in range(1,N+1) :
        p[i].append(inp[i-1])

for i in range(1,N+1) :
    hp, point = p[i]
    for k in range(1,100) :
        if k>=hp :
            dp[i][k] = max(dp[i-1][k], dp[i-1][k-hp] + point)
        else :
            dp[i][k] = dp[i-1][k]
print(dp[N][99])