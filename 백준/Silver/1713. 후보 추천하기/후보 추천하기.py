import sys
import heapq

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
reco = list(map(int, sys.stdin.readline().split()))
score = []
std = [0] * 101
photo = [0] * 101

for i in range(M):
    std[reco[i]] += 1
    cur = std[reco[i]]

    if photo[reco[i]] == 0:
        if len(score) == N:
            r, t, s = heapq.heappop(score)
            photo[s] = 0         
            std[s] = 0
        heapq.heappush(score, [cur, i + 1, reco[i]])
        photo[reco[i]] = 1       
    else:
        tmp = []
        while score:
            r, t, s = heapq.heappop(score)
            if s == reco[i]:
                tmp.append([cur, t, s])  # 추천 수 갱신
            else:
                tmp.append([r, t, s])
        for item in tmp:
            heapq.heappush(score, item)

ans = []
while score:
    rr, tt, ss = heapq.heappop(score)
    if ss != 0:
        ans.append(ss)

ans.sort()
print(*ans)
