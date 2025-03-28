import sys
N = int(sys.stdin.readline())
tree = {}
for i in range(N) :
    n, left ,right = sys.stdin.readline().split()
    tree[n] = [left, right]

Pre = []
def preOder(n) :
    if n=='.' :
        return
    
    left, right = tree[n]
    
    Pre.append(n)
    preOder(left)
    preOder(right)

In = []
def inOder(n) :
    if n=='.' :
        return
    
    left, right = tree[n]
    
    inOder(left)
    In.append(n)
    inOder(right)

Post = []
def postOder(n) :
    if n=='.' :
        return
    
    left, right = tree[n]
    
    postOder(left)
    postOder(right)
    Post.append(n)

preOder('A')
inOder('A')
postOder('A')

print(''.join(Pre))
print(''.join(In))
print(''.join(Post))
