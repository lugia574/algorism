# 와 이렇게 하니까 시초 걸림
# mlogN 이라면서요
# 아 그래서 걍 https://takeu.tistory.com/313 이거 보고 복붙함
# 그래서 아래 코드랑은 좀 다름

import math, sys
sys.setrecursionlimit(int(1e9))

def merge(x, y):
    return x+y

def init(node, start, end):
    if start == end:
        tree[node] = arr[start]
        return tree[node]
    mid = start + (end - start) // 2
    ltMerge = init(node * 2, start, mid)
    rtMerge = init(node * 2+1, mid+1, end)
    tree[node] = merge(ltMerge, rtMerge)
    return tree[node]

def query(lt, rt, node, nodeLt, nodeRt):
    if rt < nodeLt or nodeRt < lt:
        return 0
    if lt <= nodeLt and nodeRt <= rt:
        return tree[node]

    mid = nodeLt + (nodeRt - nodeLt) // 2
    ltMerge = query(lt, rt, node * 2, nodeLt, mid)
    rtMerge = query(lt, rt, node * 2 + 1, mid+1, nodeRt)
    return merge(ltMerge, rtMerge)

def update(index, newVal, node, nodeLt, nodeRt):
    if index < nodeLt or nodeRt < index:
        return tree[node]

    if nodeLt == nodeRt:
        tree[node] = newVal
        return tree[node]

    mid = nodeLt + (nodeRt - nodeLt) // 2
    ltMerge = update(index, newVal, node * 2, nodeLt, mid)
    rtMerge = update(index, newVal, node * 2 + 1, mid+1, nodeRt)

    tree[node] = merge(ltMerge, rtMerge)
    return tree[node]

if __name__ == "__main__":
    n, q = map(int, input().split())
    arr = list(map(int, input().split()))
    h = int(math.ceil(math.log2(n)))
    treeSize = 1 << (h+1)
    tree = [0] * treeSize

    init(1, 0, n-1)

    for _ in range(q):
        x, y, a, b = map(int, input().split())
        if x <= y:
            print(query(x-1, y-1, 1, 0, n-1))
        else:
            print(query(y-1, x-1, 1, 0, n-1))

        update(a-1, b, 1, 0, n-1)


