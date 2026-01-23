import sys

N, M, B = map(int, sys.stdin.readline().split())

grd = []

for _ in range(N) :
    grd.append(list(map(int, sys.stdin.readline().split())))

time = sys.maxsize
height = 0

for h in range(257) :
    t = 0
    use_block = B
    for i in range(N) :
        for j in range(M) : 
            if h > grd[i][j] :
                diff = h - grd[i][j] 
                t += diff
                use_block -= diff
            elif h < grd[i][j] :
                diff = grd[i][j] - h
                t += diff * 2
                use_block += diff
    if use_block >= 0 :
        time = min(time, t)
        if time == t : 
            height = h
print(time, height)