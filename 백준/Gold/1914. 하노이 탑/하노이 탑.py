n = int(input())
def move(a, x, y) :
    if a>1 :
        move(a-1, x, 6-x-y)
    print(f"{x} {y}")
    if a>1 :
        move(a-1, 6-x-y, y)

print(2**n-1)
if n<21 :
    move(n,1,3)