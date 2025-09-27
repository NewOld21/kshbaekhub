import sys

N = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
K = int(sys.stdin.readline())


dp = [sys.maxsize] * (num[-1] * K + 2)

for i in range(1,len(dp)) :
    if i in num :
        dp[i] = 1
    else :
        for n in num :
            if i > n :
                dp[i] = min(dp[i], dp[i-n] + 1)
ans = num[-1] * 5  + 1
for i in range(1,len(dp)) :
    if dp[i] > K :
        ans = i
        break

if ans % 2 == 0 :
    print('holsoon win at', ans)
else :
    print('jjaksoon win at', ans)