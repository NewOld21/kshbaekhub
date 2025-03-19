import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))
A.sort()
B.sort(reverse=True)
cnt = 0 
for i in range(N) :
    max = 0
    num = 0
    for j in range(len(B)) :
        if max<B[j] :
            max = B[j]
    cnt += A[i]*max
    B.remove(max)
print(cnt)