import sys
sys.setrecursionlimit(10**6)
N = int(sys.stdin.readline())
arr = [0] * (N+1)
arr[1] = 1
def p(n) :
    if n == 0 :
        return arr[0]
    elif n == 1 :
        return arr[1]
    else :
        if arr[n-1] != 0 :
            a = arr[n-1]
        else :
            a = p(n-1)
        if arr[n-2] != 0 :
            b = arr[n-2]
        else :
            b = p(n-2)
        arr[n]= a+b
        return arr[n]
ans = p(N)
print(ans)