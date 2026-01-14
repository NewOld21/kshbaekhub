import sys

X, Y = map(int, sys.stdin.readline().split())
N = int(sys.stdin.readline())

store_x = []
store_y = []

for _ in range(N) :
    x,y = map(int, sys.stdin.readline().split())
    store_x.append(x)
    store_y.append(y)

YDG = list(map(int,sys.stdin.readline().split()))

cnt = 0
half_x = X//2
half_y = Y//2
for i in range(N) :
    if YDG[0] == store_x[i] :
            cnt += min(abs(YDG[1] - store_y[i]), X*2 + Y*2 - abs(YDG[1] - store_y[i]))

    elif YDG[0] == 1 :
        if store_x[i] == 2 :
            cnt += Y + min(YDG[1] + store_y[i], X*2 - YDG[1] - store_y[i])

        elif store_x[i] == 3 :
            cnt += min(YDG[1] + store_y[i], X*2 - YDG[1] + Y*2 - store_y[i])
        else :
            cnt += min(X - YDG[1] + store_y[i], X + YDG[1] + Y*2 - store_y[i])

    elif YDG[0] == 2 :
        if store_x[i] == 1 :
            cnt += Y + min(YDG[1] + store_y[i], X*2 - YDG[1] - store_y[i])

        elif store_x[i] == 3 :
            cnt += min(YDG[1] + Y - store_y[i], X*2 - YDG[1] + Y + store_y[i])
        else :
            cnt += min(X - YDG[1] + Y - store_y[i], X + YDG[1] + Y + store_y[i])

    elif YDG[0] == 3 :
        if store_x[i] == 4 :
            cnt += X + min(YDG[1] + store_y[i], Y*2 - YDG[1] - store_y[i])

        elif store_x[i] == 1 :
            cnt += min(YDG[1] + store_y[i], Y*2 - YDG[1] + X*2 - store_y[i])
        else :
            cnt += min(Y - YDG[1] + store_y[i], Y + YDG[1] + X*2 - store_y[i])

    elif YDG[0] == 4 :
        if store_x[i] == 3 :
            cnt += X + min(YDG[1] + store_y[i], Y*2 - YDG[1] - store_y[i])

        elif store_x[i] == 1 :
            cnt += min(YDG[1] + X - store_y[i], Y*2 - YDG[1] + X + store_y[i])
        else :
            cnt += min(Y - YDG[1] + X - store_y[i], Y + YDG[1] + X + store_y[i])
            
print(cnt)          