import sys

def set(a) :
    if a==n :
        return
    for i in range(3) : 
            arr[a]=num[i]
            if sum(arr) == n  :
                cnt[0] +=1 
            set(a+1)
            arr[a] = 0

for _ in range(int(sys.stdin.readline())) :
    n = int(sys.stdin.readline())
    cnt = [0]
    num = [1,2,3]
    p = 0
    arr= [0] * n
    cnt = [0]
    set(0)
    print(cnt[0])