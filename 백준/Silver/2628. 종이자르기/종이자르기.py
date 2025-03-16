import sys
w, h = map(int, sys.stdin.readline().split())
x = [0,w]
y = [0,h]
for i in range(int(input())) :
    a, b = map(int, sys.stdin.readline().split())
    if a == 0 :
        y.append(b)
    else :
        x.append(b)
result = 0
x.sort()
y.sort()
for i in range(len(x)-1) :
    c = x[i] - x[i+1]
    for j in range(len(y)-1) :
        d = y[j] - y[j+1]
        if result< (c*d) :
            result = c*d
print(result)