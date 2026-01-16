import sys


N = int(sys.stdin.readline())
crane = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
box = list(map(int, sys.stdin.readline().split()))
crane.sort(reverse=True)
box.sort(reverse=True)
carry = [0] * M
cnt = 0
time = 0


if crane[0] < box[0]:
    print(-1)
    exit()


check = [0] * (N + 1)
check[-1] = 100001
for b in range(M) :
        for c in range(N) :
            if box[b] <= crane[c]  :
                if check[c] >= check[c+1] and box[b] <= crane[c+1] :
                     continue
                else :
                     check[c] += 1
                     break

check[-1] = -1
print(max(check))