import sys
n = sys.stdin.readline().strip()
stack = []

for i in n :
    if i in '[(' :
        stack.append(i)
    else :
        if not stack :
            print(0)
            exit()
        temp = 0
        while stack :
            top =stack.pop()
            if isinstance(top,int) :
                temp += top
            else :
                if (top=='(' and i==')') : 
                    stack.append(2 if temp==0 else 2*temp)
                    break
                elif (top=='[' and i==']') :
                    stack.append(3 if temp==0 else 3*temp)
                    break
                else  :
                    print(0)
                    exit()
        else :
            print(0)
            exit()
cnt = 0
for i in stack : 
    if isinstance(i,int) :
        cnt += i
    else :
        print(0)
        exit()
print(cnt)