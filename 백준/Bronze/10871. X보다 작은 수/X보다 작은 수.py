N, X = map(int, input().split(' '))
a = input().split(' ')
for i in range(N) :
    if int(a[i]) < X :
        print(a[i])