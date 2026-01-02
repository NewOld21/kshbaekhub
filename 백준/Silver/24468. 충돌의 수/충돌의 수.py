import sys

L, N, T = map(int, sys.stdin.readline().split())
ball = []
location = []

for _ in range(N) :
    b, l = sys.stdin.readline().split()
    ball.append(int(b))
    location.append(l)

cnt = 0

for _ in range(T) :

    line = [0] * (L+1)
    for i in range(N) :
        if location[i] == 'L' :
            ball[i] -= 1
        else : 
            ball[i] += 1
        if ball[i] == 0 :
            location[i] = 'R'
        elif ball[i] == L :
            location[i] = 'L'
        line[ball[i]] += 1

    for i in range(1,L) :
        if line[i] > 1 :
            cnt += 1
            for j in range(N) :
                if i == ball[j] :
                    if location[j] == 'L' :
                        location[j] = 'R'
                    else : 
                        location[j] = 'L'

print(cnt)