cnt = [0] * 1000001

for i in range(1,1000001) :
    max = (1000001 // i) + 1
    for j in range(2,max) :
        idx = i * j + ((i-1)*i)//2
        if idx > 1000000 :
            break
        cnt[idx] += 1

while True :
    N = int(input())
    if N == 0 :
        break
    print(cnt[N])
