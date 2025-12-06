import sys

N, D = map(int, sys.stdin.readline().split())

road = []

for i in range(N) :
    s, e, d = map(int, sys.stdin.readline().split())
    if e <= D :
        road.append([s,e,d])

dp = [sys.maxsize for _ in range(D+1)]
dp[0] = 0

for i in range(D+1) :
    if i > 0 :
        dp[i] = min(dp[i], dp[i-1] + 1)
    for s, e, d in road :
        if i == s :
            dp[e] = min(dp[e], dp[i] + d)
    
print(dp[-1])