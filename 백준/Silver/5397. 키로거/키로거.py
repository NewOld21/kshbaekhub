import sys

T = int(sys.stdin.readline())

for _ in range(T) :
    com = list(sys.stdin.readline().strip())

    pass1 = []
    pass2 = []

    for c in com :
        if c == '-' :
            if pass1 :
                pass1.pop()
        
        elif c == '<' :
            if pass1 :
                s = pass1.pop()
                pass2.append(s)

        elif c == '>' :
            if pass2 :
                s = pass2.pop()
                pass1.append(s)

        else :
            pass1.append(c)

    
    ans = ''.join(pass1+pass2[::-1])
    print(ans)