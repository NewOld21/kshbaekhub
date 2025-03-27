import sys
sys.setrecursionlimit(10**9)  # 재귀 한도 증가
input = sys.stdin.read  # 빠른 입력

# 입력 받기 (한 번에 읽고, 줄 단위로 변환)
pre = list(map(int, input().split()))

def postOrder(start, end):
    """ 후위 순회 (재귀 사용) """
    if start > end:
        return
    
    root = pre[start]  # 현재 서브트리의 루트 노드
    div = end + 1  # 오른쪽 서브트리 시작점

    # 오른쪽 서브트리 찾기
    for i in range(start + 1, end + 1):
        if pre[i] > root:
            div = i
            break

    postOrder(start + 1, div - 1)  # 왼쪽 서브트리
    postOrder(div, end)  # 오른쪽 서브트리
    print(root)  # 루트 출력 (후위 순회)

postOrder(0, len(pre) - 1)  # 전체 트리에 대해 후위 순회 실행