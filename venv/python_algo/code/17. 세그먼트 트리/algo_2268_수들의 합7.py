# 이거 딱 봐도 세그먼트 트리자너
import sys, math

def query(cur, start, end, left, right):
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return tree[cur]

    mid = start + (end - start) // 2
    lt = query(cur*2, start, mid, left, right)
    rt = query(cur*2+1, mid+1, end, left, right)
    return lt + rt

def update(cur, start, end, idx, val):
    if idx < start or idx > end:
        return
    if start == end:
        tree[cur] = val
        return

    mid = start + (end - start) // 2
    update(cur*2, start, mid, idx, val)
    update(cur*2+1, mid+1, end, idx, val)
    tree[cur] = tree[cur*2] + tree[cur*2+1]
    return


if __name__ == "__main__":
    input = sys.stdin.readline
    n, m = map(int, input().split())
    arr = [0] * (n+1)
    h = int(math.ceil(math.log2(n))) + 1
    size = 1 << h
    tree = [0] * size

    for _ in range(m):
        order, a, b = map(int, input().split())
        if order == 0:
            if a > b:
                a, b = b, a
            # sum
            print(query(1, 1, n, a, b))

        else:
            # modify
            arr[a] = b
            update(1, 1, n, a, b)