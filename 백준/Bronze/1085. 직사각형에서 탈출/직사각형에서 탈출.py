a = input().split(' ')
x = int(a[0])
y = int(a[1])
w = int(a[2])
h = int(a[3])
min = x
if min > (w-x) :
    min = w-x
if min > y :
    min = y
if min > h-y :
    min = h-y
print(min)
