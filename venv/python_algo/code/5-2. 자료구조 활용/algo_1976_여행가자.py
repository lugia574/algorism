# 그래프 탐색인가 싶었는데
# 유니온 알고리즘으로 풀면 보다 싶게 풀수 있다는데
# 흠 나는 우선 node 다 박고
# 루트 제일 0 번째부터 돌아서 하나하나 체크를 쭉 하는 식으로 DFS 나 BFS 돌릴려고했음
# 그럼 유니온 파인드는 무엇이냐
# https://www.youtube.com/watch?v=AMByrd53PHM

# 대충 각 노드의 부모를 찾는거임
# 부모는 연결 노드의 가장 적은 값
# 그리고 이들이 같은 부모를 공유하고 있다면 연결되어 있다는거지

# 문제에서 1은 연결되어 있는다 소리니까
# 각 도시가 어떤 도시랑 연결 되어 있냐를 받아서 해당 도시 y 와 연결된 도시 x 를 union 해줘

# 그렇게 각 집합을 다 정리 한 다음에
# 여행하는 루트의 포문을 돌면서 find 해주면
# 각 부모 노들을 뱉을텐데 이게 다 같은 부모노드여야 연결되어 있다는거니까
# 해당 집합 갯수가 무조건 하나여야함

import sys

def find(x):
    if x == parent[x]:
        return x
    p = find(parent[x])
    parent[x] = p
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)

    if a == b:
        return
    if a < b:
        parent[b] = a
    else:
        parent[a] = b



if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    m = int(input())
    parent = [i for i in range(n+1)]

    for y in range(1, n+1):
        maps = list(map(int, input().split()))

        for x in range(1, n+1):
            if maps[x-1] == 1:
                union(y, x)
            #print(y, x, parent)

    route = list(map(int, input().split()))
    result = set([find(i) for i in route])
    print("YES" if len(result) == 1 else "NO")


