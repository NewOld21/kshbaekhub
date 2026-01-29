import sys

N = int(sys.stdin.readline())
shop = []
for _ in range(N) :
    n = int(sys.stdin.readline())
    shop.append(n)

dp_yum = [0] * N
dp_no = [0] * N
dp_seq = [0] * N
dp_yum[0] = shop[0]

for i in range(1,N) :
    dp_yum[i] = dp_no[i-1] + shop[i]
    dp_no[i] = max(dp_no[i-1], dp_yum[i-1], dp_seq[i-1])
    dp_seq[i] = dp_yum[i-1] + shop[i]//2

print(max(dp_no[-1], dp_seq[-1], dp_yum[-1]))