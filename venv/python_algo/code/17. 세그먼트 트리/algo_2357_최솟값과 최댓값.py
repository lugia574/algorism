# 받은 배열의 a ~ b 사이의 최댓값, 최솟값을 구하라라는 문제인디
# 이게 단순히 매번 min(arr[a-1:b]), max 해서 해결 할 문제가 딱 봐도 아님
# 무조건 터짐
# 이걸 해결할 방법은 바로 세그먼트 트리
# 세그먼트 트리는 기본적으로 값은 초기화해서 집어 넣어야함

import sys

def query(cm, node, lt, rt, x, y):
    if x <= lt and rt <= y:
        return minTree[node] if cm == 1 else maxTree[node]
    if y < lt or x > rt:
        return sys.maxsize if cm == 1 else 0
    mid = lt + (rt - lt) // 2
    return merge(cm, query(cm, node*2, lt, mid, x, y), query(cm, node*2+1, mid+1, rt, x, y))

def merge(cm, x, y):
    return min(x, y) if cm == 1 else max(x, y)


def init(cm, node, lt, rt):
    mid = lt + (rt - lt) // 2

    if cm == 1:
        if lt == rt:
            minTree[node] = arr[lt]
            return minTree[node]
        minTree[node] = merge(cm, init(1, node*2, lt, mid), init(1, node*2+1, mid+1, rt))
        return minTree[node]

    else:
        if lt == rt:
            maxTree[node] = arr[lt]
            return maxTree[node]
        maxTree[node] = merge(cm, init(0, node * 2, lt, mid), init(0, node * 2 + 1, mid + 1, rt))
        return maxTree[node]

if __name__ == "__main__":
    input = sys.stdin.readline
    n, m = map(int, input().split())
    arr = [int(input()) for _ in range(n)]
    minTree = [0] * (n*4+1)
    maxTree = [0] * (n*4+1)

    init(1, 1, 0, n - 1)
    init(0, 1, 0, n - 1)

    for _ in range(m):
        a, b = map(int, input().split())

        print(query(1, 1, 0, n-1, a-1, b-1), query(0, 1, 0, n-1, a-1, b-1))
