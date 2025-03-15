for i in range(int(input())) :
    a = input().split(' ')
    p = ''
    for j in a[1] :
        p += j*int(a[0])
    print(p)
        