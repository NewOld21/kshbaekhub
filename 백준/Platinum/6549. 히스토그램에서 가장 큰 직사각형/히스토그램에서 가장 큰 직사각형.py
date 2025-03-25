import sys

def make_r(height) :
    stack = []
    n = len(height)
    inx = 0
    while inx<n :
        if not stack or height[stack[-1]] <= height[inx] :
            stack.append(inx)
            inx +=1  
        else :
            h = height[stack.pop()]
            w = inx if not stack else inx - stack[-1] -1
            max_size.append(h*w)

    while stack :
        h = height[stack.pop()]
        w = inx if not stack else inx - stack[-1] -1
        max_size.append(h*w)
    return


while True :
    max_size = []
    N = list(map(int, sys.stdin.readline().split()))
    if N[0] == 0 :
        break
    make_r(N[1:])
    
    print(max(max_size))
