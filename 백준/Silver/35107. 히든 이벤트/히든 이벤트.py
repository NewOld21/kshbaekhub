import sys

N, M, K = map(int, sys.stdin.readline().split())

T = N - M
e = N - M 
nothing = 1
for k in range(1,K+1) :
    ans = 0
    if k <=  e:
        nothing *= T/N 
        T -= 1
        N -= 1
        ans = 1 - nothing
    else :
        ans = 1
    print(ans)