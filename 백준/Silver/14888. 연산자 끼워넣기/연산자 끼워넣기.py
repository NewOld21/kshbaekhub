import sys 
N = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
Operater = list(map(int, sys.stdin.readline().split()))

mx = -1e9
mn = 1e9

def set(a, temp) :
    global mx, mn
    if a == N-1 :
        mx = max(temp, mx)
        mn = min(temp, mn)
        return 
    else :
        if Operater[0] != 0 :
            Operater[0] -= 1
            set(a+1, temp + num[a+1])
            Operater[0] += 1

        if Operater[1] != 0 :
            Operater[1] -= 1
            set(a+1, temp - num[a+1])
            Operater[1] += 1

        if Operater[2] != 0 :
            Operater[2] -= 1
            set(a+1, temp * num[a+1])
            Operater[2] += 1

        if Operater[3] != 0 :
            Operater[3] -= 1
            set(a+1, int(temp / num[a+1]))
            Operater[3] += 1
  

set(0, num[0])
print(mx)
print(mn)

