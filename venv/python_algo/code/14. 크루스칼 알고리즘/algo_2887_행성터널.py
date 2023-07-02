# 이건 좀 신기하게 좌표간의 거리로 장난질
# 이제까지는 다 주어진 것들에 간단히 sort 하고 유니온 합집합 했음
# 되는 문제들이였지만
# 이 문제는 직접 데이터 가공을 해서 해야한다는 문제임
# 딱 프로그래머스에서 좋아할만한 형태의 문제 여기서 하나 요소 하나 더 들어가면 딱임

import sys


def find_parent(x, parent):
    if x != parent[x]:
        parent[x] = find_parent(parent[x], parent)
    return parent[x]


def union_parent(a, b, parent):
    a = find_parent(a, parent)
    b = find_parent(b, parent)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


if __name__ == "__main__":
    # input
    n = int(sys.stdin.readline())
    c = []
    for i in range(n):
        x, y, z = map(int, sys.stdin.readline().split())
        c.append((x, y, z, i))  # 좌표값, 인덱스

    # 데이터 가공
    # 각 좌표별로 정렬한 후 거리를 계산해서 edge를 만든다.
    edges = []
    for i in range(3):
        c.sort(key=lambda x:x[i])
        for j in range(1, n):
            edges.append((abs(c[j - 1][i] - c[j][i]), c[j - 1][3], c[j][3]))

    parent = [i for i in range(n)]
    total = 0
    edges.sort()
    #print(edges)
    for i in range(len(edges)):
        if find_parent(edges[i][1], parent) != find_parent(edges[i][2], parent):
            union_parent(edges[i][1], edges[i][2], parent)
            total += edges[i][0]
    print(total)