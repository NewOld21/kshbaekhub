a = int(input())
b = int(input())
c = int(input())
num = str(a*b*c)
list1 = [0] * 10
for i in num : 
    list1[int(i)] +=1
for i in list1 :
    print(i)
    