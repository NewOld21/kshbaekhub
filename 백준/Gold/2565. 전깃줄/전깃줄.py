import sys

N = int(sys.stdin.readline())

line = []
for _ in range(N) :
    a,b = map(int, sys.stdin.readline().split())
    line.append([a,b])

line.sort()
dp = [1 for _ in range(N)]

for i in range(1,N) :
    for j in range(0,i) :
        if line[j][1] < line[i][1] :
            dp[i] = max(dp[i], dp[j] + 1)

print(N - max(dp))
