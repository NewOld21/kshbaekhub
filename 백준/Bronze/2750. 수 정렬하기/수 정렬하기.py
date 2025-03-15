a = [0] * 2001
for i in range(int(input())) :
    n = int(input())
    if n<0 :
        a[1000+n] +=1
    elif n==0 :
        a[1000] += 1
    else :
        a[n+1000] +=1

for i in range(len(a)) :
    if i<1001 :
        if a[i]>0 :
            print(i-1000)
    elif i==1000 :
        print(0)
    else :
        if a[i]>0 :
            print(i-1000)
