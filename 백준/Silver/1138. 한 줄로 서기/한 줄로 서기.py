import sys

N = int(sys.stdin.readline())

mem = list(map(int, sys.stdin.readline().split()))

spot = [0 for _ in range(N)]

for i in range(N) :
    if mem[i] == 0 :
        for j in range(N) :
            if spot[j] == 0 :
                spot[j] = i+1
                break
    else :
        cnt = mem[i]
        for j in range(N) :
            if spot[j] == 0 :
                if cnt > 0 :
                    cnt -= 1
                else :
                    spot[j] = i+1
                    break
print(*spot)