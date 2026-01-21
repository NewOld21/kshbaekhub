import sys
input = sys.stdin.readline

N, T = map(int, input().split())

driver = []

for _ in range(N):
    name, far = input().split()
    driver.append([int(far), name])

for i in range(1, N):
    driver[i][0] = (driver[i - 1][0] - driver[i][0]) % T   # ✅ while 제거

driver.sort()

ans = []
for i in range(N - 1):
    if 0 < driver[i + 1][0] - driver[i][0] <= 1000:
        ans.append(driver[i][1])

if 0 < (T - driver[N - 1][0]) <= 1000:
    ans.append(driver[N - 1][1])

ans.sort()
print(*ans) if ans else print(-1)
