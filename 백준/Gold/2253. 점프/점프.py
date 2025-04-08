import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
check = [[] for _ in range(N + 1)]
small_rock = set()
for _ in range(M):
    small = int(sys.stdin.readline())
    small_rock.add(small)
ans = -1
queue = deque([(1, 0, 0)])
while queue:
    location, jump, n = queue.popleft()
    for x in [jump + 1, jump, jump - 1]:
        if x > 0:
            next_location = location + x
            if next_location == N:
                    ans = n + 1
                    queue.clear()
                    break
            if next_location < N and next_location not in small_rock and x not in check[next_location]:
                check[next_location].append(x)
                queue.append((next_location, x, n + 1))
print(ans)