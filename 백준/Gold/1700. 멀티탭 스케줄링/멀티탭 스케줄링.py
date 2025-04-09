import sys
N, M = map(int, sys.stdin.readline().split())
it = list(map(int, sys.stdin.readline().split()))
cnt = [0] * (max(it)+1)
for i in it :
    cnt[i] += 1
check = set()

ans = 0
for i in range(M) :
    if it[i] in check :
            cnt[it[i]] -= 1
            continue
    
    if len(check) < N :
        check.add(it[i])
    else :
        c = set()
        for j in range(len(cnt)) :
            if cnt[j] == 0 :
                if j in check :
                    ans += 1 
                    check.remove(j)
                    break
            else :
                if j in check :
                    c.add(j)
        if len(check)==N :
            num = it[i+1:]
            for n in num :
                if len(c) == 1 :
                    break
                if n in check and n in c: 
                    c.remove(n)
            ans += 1 
            check.remove(c.pop())
        cnt[it[i]] -= 1
        check.add(it[i])

print(ans)
