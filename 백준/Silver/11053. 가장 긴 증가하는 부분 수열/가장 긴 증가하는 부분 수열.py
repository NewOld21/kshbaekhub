import sys
N = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))

arr = [num[0]]

def binary_s(n) :
    pl = 0
    pr = len(arr) - 1
    while pl<=pr :
        pc = (pl + pr) // 2
        if arr[pc]>=n :
            pr = pc - 1
        else :
            pl = pc + 1
    return pl
if N == 1:
    print(1)
else :
    for i in range(1,len(num)) :
        if num[i]>arr[-1] :
            arr.append(num[i])
        else :
            inx = binary_s(num[i])
            arr[inx] = num[i]
    print(len(arr))