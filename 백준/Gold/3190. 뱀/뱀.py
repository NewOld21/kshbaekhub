import sys
from collections import deque
N = int(sys.stdin.readline())
A = []
S = []
for _ in range(int(sys.stdin.readline())) :
    A.append(list(map(int, sys.stdin.readline().split())))
for _ in range(int(sys.stdin.readline())) :
    S.append(list(sys.stdin.readline().split()))

Q = deque()
x, y = 1,1           #뱀 위치 초기화화
after_t = 0          #이전 시간
cnt = 0              # 시간 측정
type = 1             #방향 설정 변수
dx = [1, 0, -1, 0]   #방향 오른쪽, 위, 왼쪽, 아래
dy = [0, 1, 0, -1]
while 0<x<=N and 0<y<=N :
    Q.append([x,y])
    if after_t < len(S) :
        if int(S[after_t][0]) == cnt :
            if S[after_t][1] == 'D' :
                type -= 1
            elif S[after_t][1] == 'L' :
                type += 1
            after_t +=1
    type = type % 4 #인덱스 0~3 
    x += dx[type]
    y += dy[type]
    cnt +=1
    if Q :
        for i in Q :
            if x==i[0] and y==i[1] :
                print(cnt)
                exit()
    a,b = Q.popleft()
    if A:
        for i in A : 
            if x==i[0] and y==i[1] :
                Q.appendleft([a,b])
                i[0], i[1] = 0,0

print(cnt)