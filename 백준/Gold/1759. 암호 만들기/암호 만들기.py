import sys

L, C = map(int, sys.stdin.readline().split())
alph = list(sys.stdin.readline().split())

oneal = ['a', 'e', 'i', 'o', 'u']
alph.sort()
ans = []

def make_string(n, check, text) :
    if len(text) == L :
        cnt = 0
        for c in oneal :
            if c in text :
                cnt += 1
        if L-cnt >= 2 and cnt > 0:
            ans.append(text)
            return
    else :
        for i in range(n+1,C) :
            if check[i] == 0 :
                check[i] = 1
                make_string(i, check, text + alph[i])
                check[i] = 0


for i in range(0,C-L+1) : 
    check = [0 for _ in range(C)]
    check[i] = 1
    make_string(i, check, alph[i])


for t in ans :
    print(t)