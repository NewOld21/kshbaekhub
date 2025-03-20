p = []
p.append(input())
cnt = 0
back = int(p[0])
if int(p[0])<10 :
    p[0] = '0'+ p[0]

while True :
    c = 0
    for i in range(2) :
        c+=int(p[0][i])
    c=c%10
    p[0] = (p[0][1] + str(c))
    cnt +=1
    if back==int(p[0]) :
        break
print(cnt)