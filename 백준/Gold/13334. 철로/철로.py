import sys
import heapq

N = int(sys.stdin.readline())
homework = []

for _ in range(N):
    h, w = map(int, sys.stdin.readline().split())
    if h > w:
        h, w = w, h  # 항상 h가 작은 값이 되도록 정렬
    heapq.heappush(homework, (w, h))  # 종료점 기준으로 정렬

path = int(sys.stdin.readline())  
max_count = 0  
pq = []  # 포함 가능한 구간을 저장하는 우선순위 큐

while homework:
    end, start = heapq.heappop(homework)  # 종료점을 기준으로 작은 것부터 처리
    if end - start > path:
        continue  # 범위를 초과하면 무시

    heapq.heappush(pq, start)  # 시작점 추가

    # 유효 범위를 벗어난 원소 삭제 (슬라이딩 윈도우)
    while pq and pq[0] < end - path:
        heapq.heappop(pq)

    max_count = max(max_count, len(pq))

print(max_count)