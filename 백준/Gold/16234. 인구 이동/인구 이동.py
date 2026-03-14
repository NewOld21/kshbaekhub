def union(x, y):
    population = 0
    unions = []
    queue = [(x, y)]
    while queue:
        i, j = queue.pop(0)
        unions.append((i, j))
        population += A[i][j]
        for di, dj in direction:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj] and L <= abs(A[i][j] - A[ni][nj]) <= R:
                visited[ni][nj] = 1
                queue.append((ni, nj))

    # [A-1] 국경이 열린다면 인구 이동 실시
    cnt = len(unions)
    if cnt > 1:
        new_population = population // cnt
        for i, j in unions:
            A[i][j] = new_population
        return True
    return False

# [0] 입력값 할당
N, L, R = map(int, input().split())
A = []
for _ in range(N):
    A.append(list(map(int, input().split())))

# [1] 인구 이동이 일어나지 않을 때까지 반복
direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
answer = 0
while True:
    visited = [[0] * N for _ in range(N)]
    union_flag = False
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                visited[i][j] = 1
                if union(i, j):
                    union_flag = True

    if not union_flag:
        break
    answer += 1

print(answer)