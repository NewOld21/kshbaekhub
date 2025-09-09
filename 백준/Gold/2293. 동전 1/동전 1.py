import sys

N, k = map(int, sys.stdin.readline().split())

coin = []
for _ in range(N) :
    n = int(sys.stdin.readline())
    coin.append(n)

coin.sort()
dp = [0 for _ in range(k+1)] 
dp[0] = 1

for c in coin :
    for i in range(c,k+1) :
        dp[i] += dp[i-c]
        

print(dp[-1])

