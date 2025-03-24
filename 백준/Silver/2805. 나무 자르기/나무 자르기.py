import sys

# 입력 받기
N, M = map(int, sys.stdin.readline().split())
tree = list(map(int, sys.stdin.readline().split()))

# 이진 탐색을 위한 변수 설정
low, high = 0, max(tree)

# 이진 탐색 수행
while low <= high:
    mid = (low + high) // 2  # 절단기 높이 설정
    cut = sum(t - mid for t in tree if t > mid)  # 자른 나무 길이 계산

    if cut >= M:
        low = mid + 1  # 더 높은 높이도 가능할지 탐색
    else:
        high = mid - 1  # 너무 많이 잘랐으면 높이를 낮춤

# 최적 절단기 높이 출력
print(high)