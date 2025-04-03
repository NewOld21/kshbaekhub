import sys

N = int(sys.stdin.readline())

if N == 1:
    print(1)
    exit()
elif N == 2:
    print(2)
    exit()

arr = [0] * (N + 1)
arr[1] = 1
arr[2] = 2

for i in range(3, N + 1):
    arr[i] = (arr[i - 1] + arr[i - 2]) % 15746  # 매번 나머지 연산 적용

print(arr[N])