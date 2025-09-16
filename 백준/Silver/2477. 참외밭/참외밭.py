import sys
from collections import deque

N = int(sys.stdin.readline())

input = deque()
h = 0
w = 0
way = [0 for _ in range(5)]
for  _ in range(6) :
    a, l = map(int, sys.stdin.readline().split())
    input.append([a,l])
    way[a] += 1
    if a == 1 :
        w += l
    elif a == 3 :
        h += l

x,y = 0, 0
for i in range(6) :
    d, ln = input[i]

    if d < 3 and ln == w :
        if i < 5 :
            x = abs(input[i-1][1] - input[i+1][1])
        else :
            x = abs(input[i-1][1] - input[0][1])
    
    if d > 2 and ln == h :
        if i < 5 :
            y = abs(input[i-1][1] - input[i+1][1])
        else :
            y = abs(input[i-1][1] - input[0][1])
 
print(((h * w) - (x * y)) * N)