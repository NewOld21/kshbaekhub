n =int(input())
a = list(map(int, input().split()))
cnt = n
for i in a :
    x = int(i)
    if x>2 :
        for j in range(2,x//2+1) :
            if x%j==0 :
                cnt-=1
                break
    elif x==1 :
        cnt-=1
print(cnt)     