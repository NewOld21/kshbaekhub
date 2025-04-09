import sys
N = int(sys.stdin.readline())
lists = [[0,0]]
for i in range(N):
    t, m = map(int, sys.stdin.readline().split())
    lists.append([t,m])

dp = [0 for _ in range(N+1)]
for i in range(N+1) :
    if i+lists[i][0] > N+1 :
        lists[i][1] = 0

for i in range(N) :
    for j in range(i+lists[i][0],N+1) :
        if dp[j] < dp[i] + lists[j][1] :
            dp[j] = dp[i] + lists[j][1]
            

print(max(dp))