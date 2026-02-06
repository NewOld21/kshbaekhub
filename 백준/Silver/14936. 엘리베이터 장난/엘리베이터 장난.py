import sys

N, m = map(int, sys.stdin.readline().split())

seq = [0] * 4
check = [0] * 4
seq[0]= N
seq[1] = N//2
seq[2]= N//2 if N%2==0 else N//2 + 1
if N%3 < 1 :
    seq[3] = N // 3
else :
    seq[3] = N//3 + 1


cnt = 1

if m >= seq[0] :
    cnt += 1
if m >= seq[1] and N > 1:
    cnt += 1
if m >= seq[2] and N > 1 :
    cnt += 1 
if m >= seq[3] and N > 2 :
    cnt += 1
if m >= seq[0] + seq[3] and N > 2 :
    cnt += 1
if m >= seq[1] + seq[3] and N > 2 :
    cnt += 1
if m >= seq[2] + seq[3] and N > 2:
    cnt += 1

print(cnt)