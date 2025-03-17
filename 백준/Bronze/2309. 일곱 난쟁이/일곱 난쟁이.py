import sys
a=[0] * 9
for i in range(9) :
    a[i] = int(sys.stdin.readline())
n = sum(a)-100
for i in range(9) :
    for j in range(1,9) :
        if n == (a[i]+a[j]) :
            a.pop(i)
            a.pop(j-1)
            break
    if len(a)==7 :
        break
a.sort()
for i in a :
    print(i)