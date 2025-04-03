import sys
sys.setrecursionlimit(10**6)
N = int(sys.stdin.readline())

l = [3]  
k = 0  

while l[-1] < N:
    k += 1
    l.append(l[-1] * 2 + (k + 3))
   

def moo(k, N):
    if k == 0:
        return "moo"[N - 1]
    
    if N <= l[k - 1]:  
        return moo(k - 1, N)
    elif N > l[k - 1] + (k + 3):  
        return moo(k - 1, N - l[k - 1] - (k + 3))
    else: 
        if N - l[k - 1] == 1 : 
            return 'm' 
        else :
            return 'o'

print(moo(k, N))