import sys

n, m = map(int, sys.stdin.readline().split())

picture = []

for _ in range(n) :
    picture.append(list(map(int, sys.stdin.readline().split())))

dx = [0, 0, 1, -1]
dy = [1, -1 ,0, 0]

cnt = 0
mx = 0

for a in range(n) :
    for b in range(m) :
        if picture[a][b] == 1 :
            picture[a][b] = -1
            q = [[a,b]]
            cnt += 1
            size = 0
            while q : 
                x, y = q.pop()
                size += 1
                for i in range(4) :
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < n and 0<= ny < m  and picture[nx][ny] == 1 :
                        picture[nx][ny] = -1
                        q.append([nx,  ny])
            mx = max(mx, size)

print(cnt)
print(mx)