import sys

N, M = map(int, sys.stdin.readline().split())

war = []
for i in range(M) :
        war.append(list(sys.stdin.readline().strip()))


white = 0
blue = 0

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

        
for i in range(M) :
        for j in range(N) :
                if war[i][j] != '0' :
                        q = [[i,j]]
                        cnt = 1
                        color = war[i][j]
                        war[i][j] = '0'
                        while q :
                            x, y = q.pop()
                            for n in range(4) :
                                nx = x + dx[n]
                                ny = y + dy[n]
                                if 0 <= nx < M and 0 <= ny < N  and war[nx][ny] == color :
                                        q.append([nx, ny])
                                        war[nx][ny] = '0'
                                        cnt += 1

                        if color == 'W' :
                                white += cnt*cnt
                        else :
                                blue += cnt*cnt

print(white, blue)
                        