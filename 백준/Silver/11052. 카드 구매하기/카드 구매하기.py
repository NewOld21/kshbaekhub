import sys

N = int(sys.stdin.readline())
card = list(map(int, sys.stdin.readline().split()))

dp = [0 for _ in range(N+1)]

for i in range(1,N+1) :
    n = N//i 

    for j in range(i,N+1) : 
        dp[j] = max(dp[j], dp[j-i] + card[i-1])


print(dp[-1])