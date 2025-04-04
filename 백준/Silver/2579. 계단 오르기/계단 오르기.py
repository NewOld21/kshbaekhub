import sys
N = int(sys.stdin.readline())
s = []
for i in range(N) :
    a = int(sys.stdin.readline())
    s.append(a)

D = [sys.maxsize] * N

if N>3 :
    D[0] = s[0]
    D[1] = s[1]
    D[2] = s[2]
    for i in range(3,N) : 
        D[i] = min(D[i-2],D[i-3]) + s[i]

    ans = min(D[N-3], D[N-2])
    ans = sum(s) - ans
elif N == 3 :
    D[0] = s[0]
    D[1] = s[1]
    ans = sum(s) - min(D[0],D[1])
else :
    ans = sum(s)
print(ans)