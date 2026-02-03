import sys

B, A = map(int, sys.stdin.readline().split())

cnt = 1
while A > B :
    if A % 2 == 0 :
        A = A//2
    elif A%10 == 1 :
        A = A//10 
    else :
        break
    cnt += 1

if A == B :
    print(cnt)
else :
    print(-1)