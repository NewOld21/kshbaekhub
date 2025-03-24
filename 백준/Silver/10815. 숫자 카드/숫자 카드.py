import sys
N = int(sys.stdin.readline())
n_num = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
m_num = list(map(int, sys.stdin.readline().split()))

ans = [0] * M
n_num.sort()
for i in range(M) : 
    pl = 0 
    pr = N - 1
    while pl<=pr :
        pc = (pl + pr) // 2
        if m_num[i] == n_num[pc] :
            ans[i] = 1
            break
        elif m_num[i] > n_num[pc] :
            pl = pc + 1
        else :
            pr = pc - 1
    
print(*ans)