n = int(input())
a = list(map(int, input().split()))
use_a = [0] * len(a) 
sub = [0] * len(a)
max = [0]

def max_sub(a,n) :
    if n<len(a) :
        for i in range(len(a)) :
            if use_a[i] == sub[n] == 0 : 
                sub[n] = a[i]
                use_a[i] = 1
                max_sub(a, n+1)
                sub[n] = 0
                use_a[i] = 0
    else :
        m = 0
        for i in range(len(sub)-1) :
            m += abs(sub[i] -sub[i+1])
        if m> max[0] :
            max[0] = m

max_sub(a,0)
print(max[0])