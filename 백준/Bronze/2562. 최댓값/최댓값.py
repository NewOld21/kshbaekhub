max = 0
max_num = 0
for i in range(9) :
    x = int(input())
    if max < x :
        max = x
        max_num = i
print(max)
print(max_num+1)

        