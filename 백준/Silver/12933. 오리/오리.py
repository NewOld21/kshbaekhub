import sys

duck = sys.stdin.readline().strip()
quack = ['q', 'u', 'a', 'c', 'k']
check = [0] * len(duck)
cnt = 0
ans = 0

while cnt < len(duck) :
    
    w = 0
    idx = 0

    for i in range(len(duck)) :
        if check[i] == 0 and duck[i] == quack[idx] :
            check[i] = 1
            w += 1
            idx += 1
            cnt += 1
            
            if idx == 5 :
                idx = 0 
    
    if w % 5 != 0 or w == 0 :
        ans = -1
        break

    ans += 1
print(ans)