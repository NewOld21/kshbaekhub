import sys, heapq

M, S = map(int, sys.stdin.readline().split(':'))

S += M * 60

buttons = [30, 10, 60, 600]

q = []
heapq.heappush(q, [0,S,False])

while q :
    c, s, t = heapq.heappop(q)
    if  s == 0 :
        if t > 0 :
            print(c)
        else :
            print(c+1)
        break

    for i in buttons :
        if s//i > 0 : 
            if i == 30 :
                heapq.heappush(q, [c + s//i ,s%i, t+1]) 
            else :
                heapq.heappush(q, [c + s//i ,s%i, t]) 
