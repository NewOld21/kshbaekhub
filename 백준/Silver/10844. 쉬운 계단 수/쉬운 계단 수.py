import sys

N = int(sys.stdin.readline())

dp = [[0] * (10) for _ in range(N+1)]

for i in range(1,10) :
    dp[1][i] = 1

if N > 1 :
    for i in range(2,N+1) :
        for j in range(10) :
            if j == 0 : # 0의 경우에 수는 1일 때
                dp[i][j] = dp[i-1][1]
            elif j == 9 : # 9의 경우에 수는 8일 때
                dp[i][j] = dp[i-1][8]
            else : # 나머지의 경우에 수는 -1, +1 일 때
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
print(sum(dp[N])%1000000000)