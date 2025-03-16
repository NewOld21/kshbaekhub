import sys
result = 0
num = int(sys.stdin.readline())
if num<100 :
    result = num
else : 
    for n in range(num,99,-1) :      
        a = []
        for i in str(n) :
            a.append(int(i))
        if (a[0]-a[1]) == (a[1]-a[2]) :
            result +=1
    result += 99  
print(result)