import sys
n = int(sys.stdin.readline())
a = [0] *10001
for _ in range(n) :
    a[int(sys.stdin.readline())] +=1 
for i in range(len(a)) :
    if a[i]!=0 :
        for j in range(a[i]) :
            print(i)