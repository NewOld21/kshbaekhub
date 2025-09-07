import sys 

N, M = map(int, sys.stdin.readline().split())
box = []

for _ in range(M) :
    b = int(sys.stdin.readline())
    box.append(b)

right = max(box)
left = 1


while(left <= right) :
    sum = 0
    mid = (left + right) // 2
    for i in range(M) :
        sum += box[i] // mid
        if box[i] % mid != 0 :
            sum += 1

    if sum > N:
        left = mid + 1

    else :
        right = mid - 1

print(left)
