import sys
N = int(sys.stdin.readline())
w = [list(map(int, sys.stdin.readline().split())) for i in range(N)]

check = [0] * N
arr = [-1] * N
mins = []
def tsp(n) :
    if n<N :
        for i in range(N) :
            if check[i] == 0 and arr[n] == -1 :
                check[i] = 1
                arr[n] = i
                tsp(n+1)
                check[i] = 0
                arr[n] = -1
    else :
        m = 0
        for i in range(N-1) :
            if w[arr[i]][arr[i+1]] ==0 :
                m = -1
                break
            m += w[arr[i]][arr[i+1]]
        if m>0 and w[arr[N-1]][arr[0]]!=0:
            m +=w[arr[N-1]][arr[0]]
            mins.append(m)
tsp(0)
print(min(mins))