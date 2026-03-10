import sys

line_f = list(sys.stdin.readline().strip())
line_b = []


M = int(sys.stdin.readline())

for _ in range(M) :
    m = sys.stdin.readline().split()
    if m[0] == 'L' :
        if line_f :
            s = line_f.pop()
            line_b.append(s)

    elif m[0] == 'D' :
        if line_b :
            s = line_b.pop()
            line_f.append(s)

    elif m[0] == 'B' :
        if line_f :
            s = line_f.pop()

    elif m[0] == 'P' :
        line_f.append(m[1])

for i in line_f :
    print(i, end='')
while line_b :
    s = line_b.pop()
    print(s, end='')