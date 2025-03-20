import sys
input = sys.stdin.readline
from itertools import combinations
# 1. 입력받기
N, S = map(int, input().split())
num_list = list(map(int, input().split()))
count = 0
# 2. 길이가 1 부터 N까지인 부분수열의 모든 경우의 수 탐색 =>조합
# 3. 각 경우의 수별 합계 계산
# 4. 그 합계가 S와 동일하다면 count += 1
for i in range(1, N + 1):
  combis = combinations(num_list, i)
  for comb in combis:
    total = sum(comb)
    if total == S:
      count += 1
print(count)