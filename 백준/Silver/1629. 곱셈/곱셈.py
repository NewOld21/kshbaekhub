import sys
A, B, C = map(int, sys.stdin.readline().split())
bb = {}
def calculate(a,b,c) :
    if b>1 :
        if b not in bb :
            num1 = calculate(a, b//2, c)
            if b % 2 == 0 :
                a = (num1 * num1) % c
            else :  
                a = (num1 * num1 * a) % c
            bb[b] = a
        else : 
            return bb[b]
    else : 
        a = a % c
        bb[b] =a
    return a
    
print(calculate(A, B, C))