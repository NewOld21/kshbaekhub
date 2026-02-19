import sys
from collections import deque

T = int(sys.stdin.readline())

for _ in range(T):
    coin = []
    for _ in range(3):
        coin.append(sys.stdin.readline().split())  

    x =[0,1,2,0,0,0,0,0]
    y =[0,0,0,0,1,2,0,2]
    dx = [0,0,0,1,1,1,1,1]
    dy = [1,1,1,0,0,0,1,-1]

    ans = []
    check = [0] * 8
    q = deque()
    q.append([0, coin, check])

    while q:
        cnt, cur_coin, cur_check = q.popleft()

        flat = [c for row in cur_coin for c in row]
        if all(v == 'H' for v in flat) or all(v == 'T' for v in flat):
            ans.append(cnt)
            continue

        for i in range(8):
            if cur_check[i] == 0:
                c = [row[:] for row in cur_coin]
                new_check = cur_check[:]
                new_check[i] = 1

                nx, ny = x[i], y[i]
                for j in range(3):
                    if j > 0:
                        nx += dx[i]
                        ny += dy[i]
                    c[nx][ny] = 'T' if c[nx][ny] == 'H' else 'H'

                q.append([cnt + 1, c, new_check])

    if ans :
        print(min(ans))
    else :
        print(-1)
