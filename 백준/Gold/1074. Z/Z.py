import sys
N, r, c = map(int, input().split())
n = 2**N
def z(n, x, y, b) :
    if n == 0:
        return(b)
    n = n//2
    if x<n and y<n :
        q = 1
    if x<n and y>=n :
        q = 2
        y -= n
    if x>=n and y<n :
        q = 3
        x -= n
    if x>=n and y>=n :
        q = 4
        x -= n
        y -= n
    b += (n**2) * (q-1)
    return z(n, x, y, b)

print(z(n,r,c,0))
