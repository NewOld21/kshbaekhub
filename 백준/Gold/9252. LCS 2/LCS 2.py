import sys
from collections import deque
A = list(sys.stdin.readline().strip())
B = list(sys.stdin.readline().strip())

dp = [[0]*(len(B)+1) for _ in range(len(A)+1)]

for i in range(1,len(A)+1) :
    for j in range(1,len(B)+1) :
        if A[i-1] == B[j-1] :
            dp[i][j] = dp[i-1][j-1] + 1
        else :
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
print(dp[len(A)][len(B)])

ans = deque()
x = len(A)
y = len(B)
while len(ans) < dp[len(A)][len(B)] :
    if A[x-1] == B[y-1] :
        ans.appendleft(A[x-1])
        x -= 1
        y -= 1
    else :
        if dp[x-1][y] > dp[x][y-1] : 
            x -= 1
        else :
            y -= 1 
print(''.join(ans))