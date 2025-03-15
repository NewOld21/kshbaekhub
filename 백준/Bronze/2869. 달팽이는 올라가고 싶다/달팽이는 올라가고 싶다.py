a, b, c = map(int, input().split())
cnt = (c - a) // (a - b) + 1  
if (c - a) % (a - b) != 0:
    cnt += 1
print(cnt)