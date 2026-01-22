import sys

T = int(sys.stdin.readline())
dx = [-1, 0, 1]

for _ in range(T) :
    x, y = map(int, sys.stdin.readline().split())
    far = y - x
    jump = 0
   
    while True :
        if far <= jump**2 + jump :
            break
        jump += 1
        
    if far <= jump**2 :
        print(jump*2 - 1)
    else :
        print(jump*2)