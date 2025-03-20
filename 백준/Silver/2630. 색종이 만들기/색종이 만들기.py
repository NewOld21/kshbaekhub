import sys
N = int(sys.stdin.readline())
C_papaer = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
b_cnt = [0]
w_cnt = [0]
def check_color(n,x,y) :
    if n==0 :
        return
    color = C_papaer[x][y] 
    for i in range(n) :
        for j in range(n) :
            if color != C_papaer[x+i][y+j] :
                n= n//2
                check_color(n,x, y)
                check_color(n,x, y+n)
                check_color(n,x+n, y)
                check_color(n,x+n, y+n)
                return
            
    if color == 1 :
        b_cnt[0] += 1
    else :
        w_cnt[0] +=1
        
    return
            
check_color(N,0,0)
print(w_cnt[0])
print(b_cnt[0])