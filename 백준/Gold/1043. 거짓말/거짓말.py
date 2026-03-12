import sys

N, M = map(int, sys.stdin.readline().split())

know_p = set(list(map(int, sys.stdin.readline().split()))[1:])

lie_party = [0] * M 
party = []
for _ in range(M) :
    p = list(map(int, sys.stdin.readline().split()))[1:]
    party.append(p)

for _ in range(M) :
    for i in range(M) :
        for p in party[i] :
            if p in know_p :
                lie_party[i] = 1
                for r in party[i] :
                    know_p.add(r)

cnt = 0
for l in lie_party :
    if l == 0 :
        cnt += 1

print(cnt)