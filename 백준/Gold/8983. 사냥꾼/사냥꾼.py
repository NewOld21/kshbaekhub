import sys
M, N, L = map(int, sys.stdin.readline().split())
Mx = list(map(int, sys.stdin.readline().split()))
Nxy = []
ans = [0]
for i in range(N) :
    x,y = map(int, sys.stdin.readline().split())
    Nxy.append([x,y])
Mx.sort()
def binary_s(x,y) :
    pl = 0
    pr = M-1
    while pl<= pr:
        pc = (pl+pr) //2
        if (abs(Mx[pc]- x) +y) <= L :
            ans[0] += 1
            break
        else : 
            if Mx[pc]- x > 0 :
                pr = pc - 1
            else :
                pl = pc + 1       
    return


for i in range(N) :
    x = Nxy[i][0]
    y = Nxy[i][1]
    binary_s(x,y)
    

print(ans[0])