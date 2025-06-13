import sys
N = int(sys.stdin.readline())
cnt = 2
n = N
while(cnt<=n) :
    if N % cnt == 0 :
        print(cnt)
        N = N // cnt
    else :
        cnt += 1
    if N == 1 :
        break