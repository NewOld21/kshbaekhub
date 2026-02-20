import sys, math

N, M = map(int, sys.stdin.readline().split())
num = []
tree_size =  1 << (math.ceil(math.log2(N)) + 1 )
tree_max = [0] * tree_size
tree_min = [0] * tree_size

def init(a, tree_min,tree_max, node, start, end):
    if start == end:
        tree_min[node] = a[start]
        tree_max[node] = a[start]
    else:
        init(a, tree_min, tree_max, node*2, start, (start+end)//2)
        init(a, tree_min, tree_max, node*2+1, (start+end)//2+1, end)
        tree_min[node] = min(tree_min[node*2], tree_min[node*2+1])
        tree_max[node] = max(tree_max[node*2], tree_max[node*2+1])

def query_min(tree, node, start, end, left, right):
    if left > end or right < start:
        return -1
    if left <= start and end <= right:
        return tree[node]
    lmin = query_min(tree, node*2, start, (start+end)//2, left, right)
    rmin = query_min(tree, node*2+1, (start+end)//2+1, end, left, right)
    if lmin == -1:
        return rmin
    elif rmin == -1:
        return lmin
    else:
        return min(lmin, rmin)

def query_max(tree, node, start, end, left, right):
    if left > end or right < start:
        return -1
    if left <= start and end <= right:
        return tree[node]
    lmax = query_max(tree, node*2, start, (start+end)//2, left, right)
    rmax = query_max(tree, node*2+1, (start+end)//2+1, end, left, right)
    if lmax == -1:
        return rmax
    elif rmax == -1:
        return lmax
    else:
        return max(lmax, rmax)
    
for _ in range(N) :
    n = int(sys.stdin.readline())
    num.append(n)

init(num, tree_min, tree_max, 1, 0, N-1)
    
for _ in range(M) :
    x,y = map(int, sys.stdin.readline().split())
    mn = query_min(tree_min, 1, 0, N-1, x-1,y-1)
    mx = query_max(tree_max, 1, 0, N-1, x-1,y-1)
    print(mn,mx)
