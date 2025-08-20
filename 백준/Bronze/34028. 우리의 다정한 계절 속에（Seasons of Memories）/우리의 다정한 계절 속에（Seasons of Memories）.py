import sys

Y, M, D = map(int, sys.stdin.readline().split())

cnt = 0
if Y > 2015 : 
    cnt += (Y - 2015) * 4

if M < 3 :
    cnt += 1
elif 3 <= M < 6 :
    cnt += 2
elif 6<= M < 9 : 
    cnt += 3
elif 9<= M < 12 :
    cnt += 4
elif M == 12 : 
    cnt += 5

print(cnt)