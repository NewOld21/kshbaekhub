import sys

N = list(sys.stdin.readline().strip().split("."))

ans = ''
for n in N :
    if n == '' :
        ans += '.'

    else :
        cnt = len(n)
        if cnt // 4 > 0 :
            ans += ('AAAA' * (cnt // 4)) 
            cnt = cnt % 4
        
        if cnt // 2 == 1 :
            ans += ('BB')
            cnt = cnt % 2
        
        if cnt != 0 :
            ans = -1 
            break
        ans += '.'

if ans != -1 :
    print(ans[:len(ans)-1])
else :
    print(-1)
