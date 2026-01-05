import sys
input = sys.stdin.readline

K = int(input())
for test in range(K):
    M, N, P = map(int, input().split())
    
    scores = [[0] * M for _ in range(P+1)]      
    solved = [[False] * M for _ in range(P+1)]  
    solve_count = [0] * (P+1)                   
    
    for _ in range(N):
        p, m, t, j = input().split()
        p = int(p)
        t = int(t)
        j = int(j)
        m_index = ord(m) - 65 
        
        if j == 1 and not solved[p][m_index]:  
            solved[p][m_index] = True
            solve_count[p] += 1
            scores[p][m_index] += t 
        elif j == 0 and not solved[p][m_index]: 
            scores[p][m_index] += 20 
    
    result = []
    for p in range(1, P+1):
        total_time = 0
        for m in range(M):
            if solved[p][m]: 
                total_time += scores[p][m]
        result.append((p, solve_count[p], total_time))
    

    result.sort(key=lambda x: (-x[1], x[2]))
    
    print(f'Data Set {test + 1}:')
    for participant_id, solved_cnt, total in result:
        print(participant_id, solved_cnt, total)
    
    if test != K - 1:
        print()