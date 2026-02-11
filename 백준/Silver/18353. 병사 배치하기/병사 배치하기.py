import sys

N = int(sys.stdin.readline())
power = list(map(int, sys.stdin.readline().split()))

ans = [1] * N
for i in range(1,N) :
    for j in range(i) :
        if power[i] < power[j] :
            ans[i] = max(ans[i], ans[j]+1)
print(N-max(ans))