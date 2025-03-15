a = input().split(' ')
v =len(a)
if a[len(a)-1] == '' :
    v-=1
if a[0] == '' :
    v-=1
print(v)