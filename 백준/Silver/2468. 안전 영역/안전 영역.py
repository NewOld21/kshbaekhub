import sys
sys.setrecursionlimit(10**6)
N = int(sys.stdin.readline())
sp = [list(map(int,sys.stdin.readline().split()) ) for i in range(N)]
check = [[0]*N for _ in range(N)]
max_s = [0]
maxs = [1]

def h_rain(n) :
    if n<101 :
        for i in range(N) :
            for j in range(N) :
                if sp[i][j]<=n :
                    sp[i][j] = 0
        for i in range(N) :
            for j in range(N) :
                if sp[i][j]>0 and check[i][j]<n:
                    f_place(n,i,j)
                    max_s[0] +=1
        if max_s[0] == 0 :
            return
        maxs.append(max_s[0])
        max_s[0] = 0
        h_rain(n+1)
    else :
        maxs.append(1)
        return
def f_place(n,x,y) :
    if -1<x<N and -1<y<N  :
        a,b = sp[x][y], check[x][y]
        if a>0 and b<n :
            check[x][y] = n
            f_place(n,x+1,y)
            f_place(n,x-1,y)
            f_place(n,x,y-1)
            f_place(n,x,y+1)
    return

h_rain(1)
print(max(maxs))