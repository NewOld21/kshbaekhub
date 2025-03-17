import sys 
n = int(sys.stdin.readline())
pos = [False]*n
flag_a = [False] *(2*n-1)
flag_b = [False] *(2*n-1)

cnt = [0]

def set(a,n) :
    for i in range(n) :
        if(
            not pos[i] and
            not flag_a[a+i] and
            not flag_b[a-i+(n-1)] 
        ) :
            if a==n-1 :
                cnt[0] += 1
            else :
                pos[i] = flag_a[a+i] = flag_b[a-i+(n-1)] = True
                set(a+1,n)
                pos[i] = flag_a[a+i] = flag_b[a-i+(n-1)] = False
set(0,n)
print(cnt[0])
