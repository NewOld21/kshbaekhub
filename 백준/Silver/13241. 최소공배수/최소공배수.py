import sys
a,b = map(int, sys.stdin.readline().split())

def gcd(x,y) :
    while True :
        x,y = sorted([x,y])
        if x==0 :
            break
        y = y%x
    return y

n = gcd(a,b)
if n==1 :
    print(a*b)
else : 
    a = a//n
    b = b//n
    print(a*b*n)