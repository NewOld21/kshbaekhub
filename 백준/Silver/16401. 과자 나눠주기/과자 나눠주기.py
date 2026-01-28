import sys

N, M = map(int, sys.stdin.readline().split())
snack = list(map(int, sys.stdin.readline().split()))

left = 1
right = max(snack)

while left <= right:
    mid = (left + right) // 2
    cnt = 0

    for i in snack:
        cnt += i // mid

    if cnt >= N:        
        left = mid + 1
    else:
        right = mid - 1

print(right)
