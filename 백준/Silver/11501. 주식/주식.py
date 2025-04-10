import sys
for _ in range(int(sys.stdin.readline())) :
    N = int(sys.stdin.readline())
    day = list(map(int,sys.stdin.readline().split()))
    mx = day[N-1]
    price = 0
 
    for i in range(N-1,-1,-1) : 
        if day[i] < mx :
            price += mx - day[i]
        elif day[i]>mx :
            mx = day[i]
    print(price)