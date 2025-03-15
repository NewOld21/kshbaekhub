import sys
import math

# 🔹 에라토스테네스의 체로 
def sieve(n):
    prime = [True] * (n+1)
    prime[0] = prime[1] = False  
    for i in range(2, int(math.sqrt(n)) + 1):
        if prime[i]:  # i가 소수라면
            for j in range(i * i, n + 1, i):  
                prime[j] = False
    return prime

MAX_N = 10000  
is_prime = sieve(MAX_N)

# 🔹 골드바흐 파티션 찾기
def find_partition(n):
    for i in range(n // 2, 1, -1):  
        if is_prime[i] and is_prime[n - i]: 
            return i, n - i

T = int(sys.stdin.readline().strip())
for _ in range(T):
    num = int(sys.stdin.readline().strip())
    a, b = find_partition(num)
    print(a, b)