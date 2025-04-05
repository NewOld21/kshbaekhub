import sys
text = list(map(str,sys.stdin.readline().split('-')))
for i in range(len(text)) :
    text[i] = list(map(int, text[i].split('+')))
    text[i] = sum(text[i])
cnt = text[0]
for i in range(1,len(text)) :
    cnt -= text[i]

print(cnt)