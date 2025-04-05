import sys
N, K = map(int, sys.stdin.readline().split())
coin = []
for i in range(N) :
    c = int(sys.stdin.readline())
    coin.append(c)
cnt = 0
for i in range(N-1,-1,-1) :
    if K>= coin[i] :
        cnt += K//coin[i]
        K = K % coin[i]
    if K==0 :
        break
print(cnt)