import sys
N, M = map(int, sys.stdin.readline().split())

long = list(map(int, sys.stdin.readline().split()))
left = max(long)
right = sum(long)

ans = 0
while(left<=right) :
    mid = (left + right) // 2
    l_sum = 0
    cnt = 1
    for l in long :
        if l_sum +  l > mid :
            cnt += 1
            l_sum = 0
        l_sum += l
    

    if(cnt <= M) :
        right = mid - 1
        ans = mid
    else :
        left = mid + 1

print(ans)