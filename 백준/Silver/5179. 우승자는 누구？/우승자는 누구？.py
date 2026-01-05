import sys
input = sys.stdin.readline

K = int(input())
for test in range(K):
    M, N, P = map(int, input().split())
    
    # 각 참가자별로 [각 문제 점수, 각 문제 정답여부, 푼 문제 수]
    participants = {}
    
    for _ in range(N):
        p, m, t, j = input().split()
        p = int(p)
        t = int(t)
        j = int(j)
        m_index = ord(m) - 65  # A=0, B=1, ...
        
        if p not in participants:
            participants[p] = [[0] * M, [False] * M, 0]
        
        if j == 1 and not participants[p][1][m_index]:  # 정답이고 아직 안 맞춘 문제
            participants[p][1][m_index] = True
            participants[p][2] += 1
            participants[p][0][m_index] += t  # 시간만 더함
        elif j == 0 and not participants[p][1][m_index]:  # 오답이고 아직 안 맞춘 문제
            participants[p][0][m_index] += 20  # 패널티만 더함
    
    # 결과 계산
    result = []
    for participant_id in range(1, P+1):
        if participant_id in participants:
            data = participants[participant_id]
            total_time = sum(data[0][i] for i in range(M) if data[1][i])  # 맞춘 문제만 합산
            solved_count = data[2]
        else:
            total_time = 0
            solved_count = 0
        result.append((participant_id, solved_count, total_time))
    
    # 정렬: 푼 문제 수 내림차순, 총점 오름차순
    result.sort(key=lambda x: (-x[1], x[2]))
    
    print(f'Data Set {test + 1}:')
    for participant_id, solved, total in result:
        print(participant_id, solved, total)
    
    if test != K - 1:  # 마지막 테스트케이스가 아닐 때만
        print()