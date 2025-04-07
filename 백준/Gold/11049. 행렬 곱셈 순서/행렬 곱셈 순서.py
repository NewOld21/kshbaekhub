import sys

N = int(sys.stdin.readline())
X = []
Y = []

for _ in range(N) :
    x,y = map(int, sys.stdin.readline().split())
    X.append(x)
    Y.append(y)

dp= [[-1]*(N) for _ in range(N)]

def excute(s,e) :
    result = sys.maxsize
    if dp[s][e] != -1 :
        return dp[s][e]
    if s == e :
        return 0
    for i in range(s, e) :
        cnt = X[s] *  Y[i]*  Y[e]
        result = min(result, excute(s,i) + excute(i+1, e) + cnt)
        dp[s][e] = result
    return result

print(excute(0,N-1))