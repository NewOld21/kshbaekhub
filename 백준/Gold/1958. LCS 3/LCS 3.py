import sys
from collections import deque
A = list(sys.stdin.readline().strip())
B = list(sys.stdin.readline().strip())
C = list(sys.stdin.readline().strip())
dp = [[[0]*(len(C)+1) for _ in range(len(B)+1)] for _ in range(len(A)+1)]

for i in range(1,len(A)+1) :
    for j in range(1,len(B)+1) :
        for r in range(1, len(C)+1) :
            if A[i-1] == B[j-1] ==C[r-1]:
                dp[i][j][r] = dp[i-1][j-1][r-1] + 1
            else :
                dp[i][j][r] = max(dp[i-1][j][r], dp[i][j-1][r], dp[i][j][r-1])
print(dp[len(A)][len(B)][len(C)])