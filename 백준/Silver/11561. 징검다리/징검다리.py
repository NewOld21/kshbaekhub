import sys

T =  int(sys.stdin.readline().strip())

for _ in range(T) :
    N = int(sys.stdin.readline().strip())

    if N >= 3 :
        left, right = 1, N
        while left <= right :
            mid = (left + right) // 2

            if (mid * (mid + 1)) // 2 > N :
                right = mid - 1

            else :
                left = mid + 1
        print(left-1)
    else :
        print(1)
