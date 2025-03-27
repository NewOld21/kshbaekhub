import sys 
N = int(sys.stdin.readline())
p_tree = []
c_tree = []

for i in range(N) :
    n, left ,right = sys.stdin.readline().split()
    p_tree.append(n)
    c_tree.append([left, right])
Pre = []
In = []
Post = []
#전위 순회회
def preOder(num) :
    root = p_tree[num]
    left = c_tree[num][0]
    right = c_tree[num][1]
    Pre.append(root)
    if left != '.' :
        for i in range(N) :
            if left == p_tree[i] :
                left_idx = i
                break
        preOder(left_idx)
    if right != '.' :
        for i in range(N) :
            if right == p_tree[i] :
                right_idx = i
                break
        preOder(right_idx)
    
    return

preOder(0)
print(''.join(Pre))

#중위 순회
def inOder(num) :
    root = p_tree[num]
    left = c_tree[num][0]
    right = c_tree[num][1]
    if left != '.' :
        for i in range(N) :
            if left == p_tree[i] :
                left_idx = i
                break
        inOder(left_idx)
    In.append(root)
    if right != '.' :
        for i in range(N) :
            if right == p_tree[i] :
                right_idx = i
                break
        inOder(right_idx)
    
    return

inOder(0)
print(''.join(In))

#후위위 순회
def postOder(num) :
    root = p_tree[num]
    left = c_tree[num][0]
    right = c_tree[num][1]
    if left != '.' :
        for i in range(N) :
            if left == p_tree[i] :
                left_idx = i
                break
        postOder(left_idx)
    if right != '.' :
        for i in range(N) :
            if right == p_tree[i] :
                right_idx = i
                break
        postOder(right_idx)
    Post.append(root)
    return

postOder(0)
print(''.join(Post))