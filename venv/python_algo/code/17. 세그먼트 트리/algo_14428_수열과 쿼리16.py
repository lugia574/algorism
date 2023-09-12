# 17번과 다르게 얘는 index 를 뽑아야하네 흠흠
# 아아아 그러한 값이 여러개인 경우에는 인덱스가 작은 것
import sys, math

def update(node, start, end, index):
    if index < start or index > end:
        return 0
    if start == end:
        tree[node] = index
        return

    mid = start + (end - start) // 2
    update(node*2, start, mid, index)
    update(node*2+1, mid+1, end, index)
    tree[node] = tree[node*2] if arr[tree[node*2]] <= arr[tree[node*2+1]] else tree[node*2+1]

def query(node, start, end, left, right):
    if start > right or end < left:
        return 0
    if left <= start and end <= right:
        return tree[node]

    mid = start + (end - start)//2
    lt = query(node*2, start, mid, left, right)
    rt = query(node*2+1, mid+1, end, left, right)
    return lt if arr[lt] <= arr[rt] else rt

def init(node, start, end):
    if start == end:
        tree[node] = start
        return

    mid = start + (end - start) // 2
    init(node*2, start, mid)
    init(node*2+1, mid+1, end)
    tree[node] = tree[node*2] if arr[tree[node*2]] <= arr[tree[node*2+1]] else tree[node*2+1]


if __name__ == "__main__":
    input = sys.stdin.readline
    INF = sys.maxsize
    n = int(input())
    h = math.ceil(math.log2(n)) + 1
    size = 1 << h
    tree = [0] * size
    arr = [INF] + list(map(int, input().split()))

    init(1, 1, n)
    for _ in range(int(input())):
        order, a, b = map(int,input().split())
        if order == 1:
            arr[a] = b
            # update
            update(1, 1, n, a)
        else:
            # query
            print(query(1, 1, n, a, b))
