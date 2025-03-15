import sys
import math

# 🔹 에라토스테네스의 체로 미리 소수를 구함
def sieve(n):
    prime = [True] * (n+1)
    prime[0] = prime[1] = False  # 0과 1은 소수가 아님
    for i in range(2, int(math.sqrt(n)) + 1):
        if prime[i]:  # i가 소수라면
            for j in range(i * i, n + 1, i):  # i의 배수를 제거
                prime[j] = False
    return prime

# 🔹 입력값의 최댓값을 찾아서 소수 리스트를 한 번만 생성
MAX_N = 10000  # 문제에서 주어진 범위
is_prime = sieve(MAX_N)

# 🔹 골드바흐 파티션 찾기
def find_partition(n):
    for i in range(n // 2, 1, -1):  # n의 절반부터 작은 소수를 찾음
        if is_prime[i] and is_prime[n - i]:  # 두 수가 모두 소수이면 출력
            return i, n - i

# 🔹 여러 개의 테스트 케이스 처리
T = int(sys.stdin.readline().strip())
for _ in range(T):
    num = int(sys.stdin.readline().strip())
    a, b = find_partition(num)
    print(a, b)