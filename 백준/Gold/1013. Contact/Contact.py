import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = sys.stdin.readline().strip()
    l = len(N)

    type = 0        # 0: 새 패턴 시작, 1: 100 뒤 0+ 처리 중, 2: 1+ 처리 중 # 01은 항상 바로 바로 처리
    cnt = 0
    ans = 0
    ones_len = 0   

    while cnt < l:
        if type == 0:
            if N[cnt] == '0':
                if cnt + 1 >= l or N[cnt + 1] != '1':
                    ans = 1
                    break
                cnt += 2
                continue

            else:  # N[cnt] == '1'
                if cnt + 2 >= l or not (N[cnt + 1] == '0' and N[cnt + 2] == '0'):
                    ans = 1
                    break
                type = 1
                cnt += 3         
                continue

        elif type == 1:
            if cnt >= l:
                ans = 1
                break

            if N[cnt] == '0':
                cnt += 1
                continue

            if N[cnt] == '1':
                type = 2
                ones_len = 1
                cnt += 1
                continue

            ans = 1
            break

        else:  # type == 2
            if N[cnt] == '1':
                ones_len += 1
                cnt += 1
                continue

            if cnt + 1 < l and N[cnt + 1] == '1':
                type = 0
                cnt += 2          
                continue

           
            if cnt + 1 < l and N[cnt + 1] == '0':
                if ones_len >= 2:
                    type = 0
                    cnt -= 1     
                    continue
                else:
                    
                    ans = 1
                    break
            ans = 1
            break

    if ans == 1 or type == 1:
        print('NO')
    else :
        print('YES')