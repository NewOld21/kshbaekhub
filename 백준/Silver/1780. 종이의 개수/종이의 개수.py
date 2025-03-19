import sys
N = int(input())
p = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
cnt = [0] *3

def p_cut(n,x,y) :
    num = p[x][y]
    if n==1 :
         cnt[num] +=1
         return
    else :
        for i in range(n) :
            for j in range(n) : 
                if p[x+i][y+j] != num :
                    n = n//3
                    for a in range(3) :
                        for b in range(3) :
                            p_cut(n,x+(a*n),y+(b*n))
                    return
        
    cnt[num]+=1

p_cut(N,0,0)
print(cnt[-1])
print(cnt[0])
print(cnt[1])