N = int(input())
for i in range(N) :
    a = list(input())
    o = 1
    s = 0
    for x in range(len(a)) :
        if a[x]=='O' :
            s += o
            o += 1
        else :
            o = 1
    print(s)