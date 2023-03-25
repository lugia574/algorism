# 1. 아이디어
# BFS DFS 둘다 풀 수 있을듯
# 무조건 1 번부터 시작해서 걸리게 된 컴퓨터 의 수 출력이니가
# 1 번부터 싹 돌리면서 q 에 박아 check 된것들은 빼버리고 check 안된것들만 cnt 세면 되겠네

import sys
from collections import deque

def BFS(n, node):
    cnt = 0
    q = deque()
    check = [0] * (n + 1)
    check[1] = 1
    q.append(node[1])

    while q:
        nd = q.popleft()
        for i in nd:
            if check[i] == 0:
                check[i] = 1
                cnt += 1
                q.append(node[i])

    return cnt

if __name__ == "__main__":
    n = int(input())
    edge = int(input())
    node = [[]for _ in range(n + 1)]

    for _ in range(edge):
        node1, node2 = map(int, input().split())
        node[node1].append(node2)
        node[node2].append(node1)

    res = BFS(n, edge, node)
    print(res)

