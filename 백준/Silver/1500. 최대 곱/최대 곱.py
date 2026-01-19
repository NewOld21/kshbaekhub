import sys

S, K = map(int, sys.stdin.readline().split())


cnt = 1
for i in range(K,0,-1) :
    n = (S//i  if S%i==0 else S//i + 1) 
    cnt = cnt * n
    S -= n
    
print(cnt)
