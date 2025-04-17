import sys
import math
while(True) :
    N = int(sys.stdin.readline())
    if N==0 :
        break
    NN = 2 * N

    arr = [0] * (NN+1)
    arr[1] = 1 

    for i in range(2, int(math.sqrt(NN)) + 1):
       if arr[i] == 1: 
           continue
       for j in range(2 * i, NN + 1, i):
            arr[j] = 1

    cnt = 0
    for i in range(2,NN+1) :
        if i<=N :
            continue
        if arr[i] == 0 :
            cnt+=1

    print(cnt)
        
