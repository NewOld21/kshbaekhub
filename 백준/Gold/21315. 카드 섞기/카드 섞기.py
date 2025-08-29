import sys
input = sys.stdin.readline

n = int(input())                           # 카드 개수
after = list(map(int, input().split()))    # 목표 카드 순서
arr = [i+1 for i in range(n)]              # 초기 카드 순서 [1, 2, 3, ..., n]

def bland_card(prev, i, k):

    if i > k + 1:             # (재귀 종료 조건) 모든 단계 완료
        return prev

    if i == 1:                # 첫 번째 단계에서는 맨 뒤에서 2^k 장 잘라내기
        cnt = 2 ** k
    else:                     # i번째 단계에서는 2^(k-i+1) 장 잘라내기
        cnt = 2 ** (k-i+1)

    size = len(prev)
    next = prev[size-cnt:]    # 잘라낸 부분
    rest = prev[:size-cnt]    # 남은 부분

    # 잘린 부분(next)을 앞으로, 나머지(rest)는 뒤로
    return bland_card(next, i+1, k) + rest

def sol():
    # 가능한 모든 (k1, k2) 조합 탐색
    k1 = 1
    while 2**k1 < n:                       # 첫 번째 섞기 깊이 후보
        first = bland_card(arr, 1, k1)     # 첫 번째 섞기

        k2 = 1
        while 2 ** k2 < n:                 # 두 번째 섞기 깊이 후보
            second = bland_card(first, 1, k2)  # 두 번째 섞기

            if second == after:            # 목표 카드 순서 달성
                print(k1, k2)
                return
            k2 += 1
        k1 += 1

sol()
