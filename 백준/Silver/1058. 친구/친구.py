import sys

N = int(sys.stdin.readline())

friend = []
check = [[0 for _ in range(N)] for _ in range(N)]
for _ in range(N) :
    s = list(sys.stdin.readline().strip())
    friend.append(s)
    
for i in range(N) :
    for j in range(N) :
        for r in range(N) :
            if j == r :
                continue
            if friend[j][r] == 'Y' or (friend[j][i] == 'Y' and friend[i][r] == 'Y') :
                check[j][r] = 1

ans = 0
for i in check :
    ans = max(ans, sum(i))

print(ans)         