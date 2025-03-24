import sys 
N = int(sys.stdin.readline())
W = list(map(int, sys.stdin.readline().split()))

pl = 0
pr = N-1 
W.sort()
min = 2000000000
ans = [0] * 2
while pl<pr : 
    pc = W[pl] + W[pr]
    if abs(pc) < abs(min) :
        min = pc
        ans[0] = W[pl]
        ans[1] = W[pr]

    if pc>0 :
        pr = pr - 1
    elif pc< 0 :
        pl = pl + 1
    else :
        break

print(f'{ans[0]} {ans[1]}')