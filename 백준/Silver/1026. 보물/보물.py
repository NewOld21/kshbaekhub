import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))
A.sort()
B.sort(reverse=True)
cnt = 0 
for i in range(N) :
    cnt += A[i]*B[i]
print(cnt)