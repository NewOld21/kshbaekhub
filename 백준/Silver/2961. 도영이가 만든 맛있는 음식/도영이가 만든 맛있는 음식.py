import sys

N = int(sys.stdin.readline())
S = []
B = []

for _ in range(N) :
    s, b = map(int, sys.stdin.readline().split())
    S.append(s)
    B.append(b)

mn = []

def choose(n, s,b,check) :
        mn.append(abs(s-b))
        for i in range(n+1,N) :
            if check[i] == 0 :
                check[i] = 1 
                choose(i, s*S[i], b+B[i], check)
                check[i] = 0

for i in range(N) :
    check = [0 for _ in range(N)]
    check[i] = 1
    choose(i, S[i], B[i], check)

print(min(mn))