import sys
import heapq
T = int(sys.stdin.readline())

def dist(a, b):
    return sum(x != y for x, y in zip(a, b))

for _ in range(T):
    N = int(sys.stdin.readline())
    if N > 32:
        print(0)
        sys.stdin.readline()  # 입력 소모
        continue
    per = list(sys.stdin.readline().split())
    dif = [[0 for _ in range(N)] for _ in range(N)]
    q = []
    for i in range(N):
        for j in range(i+1, N):
            for idx in range(4):
                if per[i][idx] != per[j][idx]:
                    dif[i][j] += 1
                    dif[j][i] += 1
            heapq.heappush(q, [dif[i][j], 1, i, j])

    ans = sys.maxsize
    while q:
        d, n, x, y = heapq.heappop(q)
        if n == 0:
            ans = min(ans, d)
        else:
            for i in range(N):
                if i != x and i != y:
                    total = d + dif[x][i] + dif[y][i]
                    heapq.heappush(q, [total, 0, -1, -1])  # 항상 4개
    print(ans)
