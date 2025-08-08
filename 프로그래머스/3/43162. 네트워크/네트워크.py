from collections import deque
def solution(n, computers):
    answer = 0
    check = [0] * n

    for c in range(n) :
        if check[c] == 0 :
            print(c)
            answer += 1
            q = deque()
            q.append(c)
            while  q :
                i = q.popleft()
                check[i] = 1
                for x in range(n) :
                    if x!=i and computers[i][x] == 1 and  check[x] == 0 :
                        q.append(x)
                    
    return answer