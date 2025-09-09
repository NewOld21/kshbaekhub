import sys

N = int(sys.stdin.readline())

top = [[0 for _ in range(N)] for _ in range(N)] 
for i in range(N) :
    num = list(map(int, sys.stdin.readline().split()))
    for j in range(len(num)) :
        mx = max(top[i-1][j-1], top[i-1][j])
        top[i][j] = num[j] + mx
    

print(max(top[-1]))