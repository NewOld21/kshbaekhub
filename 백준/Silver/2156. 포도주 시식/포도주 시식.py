import sys

N = int(sys.stdin.readline())
wine = []
for _ in range(N) :
    n = int(sys.stdin.readline())
    wine.append(n)

drink = [0] * N
drink[0] = wine[0]
if N > 1 :
        drink[1] = wine[1] + wine[0]
if N > 2 :
    drink[2] = max(drink[1], wine[2]+ wine[1], drink[0] + wine[2])
    for i in range(3,N) :
        drink[i] = max(drink[i-1], drink[i-3] + wine[i] + wine[i-1], wine[i] + drink[i-2])


print(drink[-1])