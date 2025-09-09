import sys

N = int(sys.stdin.readline())
V = int(sys.stdin.readline())

dp = [0 for _ in range(N+1)]
vip = []
for _ in range(V) :
    vv = int(sys.stdin.readline())
    vip.append(vv)

dp = [0 for _ in range(N+1)]
dp[0] = 1
dp[1] = 1
for i in range(2,N+1) :
    dp[i] = dp[i-2] + dp[i-1]


ans = 1
pre_v = 0
if V > 0 :
    for v in vip :
        n = v-pre_v-1
        pre_v =v
        ans *= dp[n]
    ans*= dp[N-pre_v]
else :
    ans = dp[N]

print(ans)