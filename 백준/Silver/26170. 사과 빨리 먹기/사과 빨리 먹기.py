import sys, heapq

board = []
for _ in range(5) :
    row = list(map(int, sys.stdin.readline().split()))
    board.append(row)

r, c = map(int, sys.stdin.readline().split())

dx = [0,0,1,-1]
dy = [1,-1,0,0]
mn = [sys.maxsize]
board[r][c] = -1

def apple_eat(move, eat, x, y) :
    if eat == 3 :
        mn[0] = min(move, mn[0])
    
    for i in range(4) :
        nx = dx[i] + x
        ny = dy[i] + y
        if 0<=nx<5 and 0<=ny<5 :
            if board[nx][ny] == 1 :
                board[nx][ny] = -1
                apple_eat(move+1, eat+1, nx,ny)
                board[nx][ny] = 1
            elif board[nx][ny] == 0 :
                board[nx][ny] = -1
                apple_eat(move+1, eat, nx,ny)
                board[nx][ny] = 0

apple_eat(0, 0, r, c)
if mn[0] < sys.maxsize :
    print(mn[0])
else :
    print(-1)