import sys

N, M = map(int, sys.stdin.readline().split())

maze = []
dp = [[0 for _ in range(M+1)] for _ in range(N+1)]

for _ in range(N) :
    m = list(map(int, sys.stdin.readline().split()))
    maze.append(m)



for i in range(N) :
    for j in range(M) :
        dp[i][j] = max(dp[i][j] + maze[i][j], dp[i-1][j] + maze[i][j], dp[i][j-1] + maze[i][j], dp[i-1][j-1] + maze[i][j])


print(dp[-2][-2]) 