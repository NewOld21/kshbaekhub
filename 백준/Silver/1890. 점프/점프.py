import sys

N = int(sys.stdin.readline())
m = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
M = len(m[0])
dp = [[0]*(M) for _ in range(N)]

dp[0][0] = 1
for i in range(N) :
    for j in range(M) :
        s = m[i][j]
        if dp[i][j] == 0 or s==0 :
            continue
        else :
            if i+s<N :
                dp[i+s][j] +=  dp[i][j]
            if j+s<M :
                dp[i][j+s] +=  dp[i][j]
                    

print(dp[-1][-1])