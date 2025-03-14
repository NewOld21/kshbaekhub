for i in range(int(input())) :
    a = list(map(int, input().split(' ')))
    s = 0
    p = 0
    for x in range(1,a[0]+1) :
        s+= a[x]
    s = s/a[0]
    for x in range(1,a[0]+1) :
        if s < a[x] :
            p+=1
    if p == 0 :
        print('0.000%')
    else :
        print(f'{100/(a[0]/p):.3f}%')