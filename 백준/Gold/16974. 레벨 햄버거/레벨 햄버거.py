import sys
sys.setrecursionlimit(10**6)

N, X = map(int, sys.stdin.readline().split())

burger_len = [0] * (N+1)
burger_len[0] = 1

burger_pat = [0] * (N+1)
burger_pat[0] = 1
for i in range(1,N+1) :
    burger_len[i] = burger_len[i-1] * 2 + 3
    burger_pat[i] = burger_pat[i-1] * 2 + 1

def burger(n,x) :
    
    ## x = 1개 or 0개 // 레벨 0 햄버거는 패티만 있기 때문에 x를 return
    if n == 0 :
        return x
    
    ## x가 1개 일 때에는 레벨 N의 햄버거는 무조건 빵으로 시작하기 때문에 0 return
    if x == 1 :
        return 0
    
    ## x가 레벨 N의 가운데 패티 전보다 작으면 왼쪽 레벨 N-1 버거 안에서 x까지만 먹기 때문에 재귀
    elif x<= burger_len[n-1] + 1 :
        return burger(n-1,x-1)
    
    ## x가 레벨 N의 가운데 패티와 같으면 왼쪽 레벨 N-1 버거 패티 + 가운데 패티 1개 
    elif x== burger_len[n-1] + 2 :
        return burger_pat[n-1] + 1
    
    ## x가 오른쪽 끝에 있는 빵보다 작을 경우 가운데 패티에 왼쪽 레벨 N-1 버거 패티 + 가운데 패티 1개 + 재귀(오른쪽 패티안에 x까지만)
    elif x <= burger_len[n-1] * 2 + 2 :
        return burger_pat[n-1] + burger(n-1, x-burger_len[n-1]-2) + 1
    else :
        return burger_pat[n]
        
    


print(burger(N, X))