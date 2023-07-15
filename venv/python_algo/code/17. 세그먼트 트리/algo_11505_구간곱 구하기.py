# https://blogeon.tistory.com/entry/%EB%B0%B1%EC%A4%80-%EA%B3%A8%EB%93%9C1-11505%EB%B2%88-%EA%B5%AC%EA%B0%84-%EA%B3%B1-%EA%B5%AC%ED%95%98%EA%B8%B0-Python3-%ED%8C%8C%EC%9D%B4%EC%8D%AC
import sys

def merge(x,y):
    return (x * y) % 1000000007

def init(node,left,right):
    if left == right:
        stree[node] = arr[left]
        return stree[node]
    mid = right + (left - right)//2
    stree[node] = merge(init(node*2,left,mid),init(node*2+1,mid+1,right))
    return stree[node]

def query(node,left,right,x,y):
    if x <= left and right <= y:
        return stree[node]
    if y < left or x > right:
        return 1
    mid = right + (left - right)//2
    return merge(query(node * 2, left, mid, x, y), query(node * 2 + 1, mid + 1, right, x, y))

def update(node,left,right,x,y):
    if left == right == x:
        stree[node] = y
        return stree[node]
    if x < left or x > right:
        return stree[node]
    mid = right + (left - right)//2
    stree[node] = merge(update(node*2,left,mid,x,y),update(node*2+1,mid+1,right,x,y))
    return stree[node]

if __name__ == "__main__":
    input = sys.stdin.readline
    n,m,k = map(int,input().split())
    arr = [int(input()) for _ in range(n)]
    stree = [1] * (n*4+1)

    init(1, 0, n-1)

    for _ in range(m+k):
        a,b,c = map(int,input().split())
        if a == 1:
            arr[b-1] = c
            update(1, 0, n-1, b-1, c)
            continue
        print(query(1, 0, n-1, b-1, c-1))