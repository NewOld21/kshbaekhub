import sys
String = input()
bomb = input()

stack = []

for i in range(len(String)) :
    stack.append(String[i])
    if stack[-1] == bomb[-1] :
        text = stack[-len(bomb):] 
        if ''.join(text) == bomb:
            del stack[-len(bomb):] 
                
if not stack :
    print('FRULA')
else :
    print(''.join(stack))