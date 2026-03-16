import sys

T = int(sys.stdin.readline())

for _ in range(T) :
    N = int(sys.stdin.readline())
    types = {}
    if N == 0 :
        print(0)
        continue

    for _ in range(N) :
        name, type = sys.stdin.readline().split()

        if type in types :
            types[type] += 1
        else :
            types[type] = 1
    
    ans = 1
    for n in types.values() :
        ans *= (n+1) 
        
    print(ans-1)