import sys

N = int(sys.stdin.readline())
cnt = 666 
while True :
    if '666' in str(cnt) :
        N -= 1
        if N == 0 :
            print(cnt)
            break
    
    cnt += 1
