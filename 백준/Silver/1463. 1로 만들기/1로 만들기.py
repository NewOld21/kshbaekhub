import sys
N = int(sys.stdin.readline())

dp = [0] * (N+1)

for i in range(2, N+1):
    # 기본적으로는 1을 빼는 연산
    dp[i] = dp[i-1] + 1

    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)


    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)

print(dp[N])