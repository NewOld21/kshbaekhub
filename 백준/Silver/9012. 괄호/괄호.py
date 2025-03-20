import sys
N = int(sys.stdin.readline())

for _ in range(N) :
    n = sys.stdin.readline()
    stack = []
    ans = 1
    for i in n :
        if i=='(' :
            stack.append('(')           
        elif i==')' :   
            if len(stack)==0 :
                ans = 0
                break
            else :
                stack.pop()
    if ans==1 and len(stack)==0 :
        print('YES')
    else :
        print('NO')