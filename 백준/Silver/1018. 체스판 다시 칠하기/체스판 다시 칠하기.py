N, M = map(int, input().split())
p = []
check1 = []
check2 = []

for i in range(N) :
    p.append(input())

count = []
for i in range(N-7) :
    for j in range(M-7) :
        cnt1 = 0
        cnt2 = 0
        for x in range(i,i+8) :
            for y in range(j, j+8) :
                if (x+y)%2==0 :
                    if p[x][y] != 'W' :
                        cnt1 +=1
                    else :
                        cnt2 +=1
                else :
                    if p[x][y] != 'B' :
                        cnt1 +=1
                    else :
                        cnt2 +=1
        count.append(min(cnt1,cnt2))
print(min(count))