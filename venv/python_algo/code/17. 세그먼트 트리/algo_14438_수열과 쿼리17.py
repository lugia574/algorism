import sys, math

def query(node, start, end, left, right):
    if start > right or end < left:
        return INF
    if left <= start and end <= right:
        return tree[node]
    mid = start + (end - start)//2
    lt = query(node*2, start, mid, left, right)
    rt = query(node*2+1, mid+1, end, left, right)
    return min(lt, rt)

def update(node, start, end, index, val):
    if index < start or index > end:
        return
    if start == end:
        tree[node] = val
        return
    mid = start + (end - start) // 2
    update(node*2, start, mid, index, val)
    update(node*2+1, mid+1, end, index, val)
    tree[node] = min(tree[node*2], tree[node*2+1])
    return

def init(index, start, end):
    if start == end:
        tree[index] = arr[start]
        return

    mid = start + (end - start)//2
    init(index*2, start, mid)
    init(index*2+1, mid+1, end)
    tree[index] = min(tree[index*2], tree[index*2+1])

if __name__== "__main__":
    input = sys.stdin.readline
    INF = sys.maxsize
    n = int(input())
    arr = [0] + list(map(int, input().split()))
    h = int(math.ceil(math.log2(n))) + 1
    size = 1 << h
    tree = [INF] * size


    init(1, 1, n)

    for _ in range(int(input())):
        order, a, b = map(int, input().split())
        if order == 1:
            # update
            arr[a] = b
            update(1, 1, n, a, b)
        else:
            # minValue
            print(query(1, 1, n, a, b))
