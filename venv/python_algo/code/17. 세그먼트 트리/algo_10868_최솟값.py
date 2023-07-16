# https://velog.io/@ggb05224/백준-10868-최솟값python


import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
INF = sys.maxsize

# N개의 정수, 순서쌍 갯수 M개 (구간갯수)
N, M = map(int, input().split())
data = [0] + [int(input()) for _ in range(N)]
tree = [0] * (N * 4)


# 세그먼트 트리 생성 & 초기화
def init(start, end, index):
    # 해당 구간이 리프노드라면
    if start == end:
        tree[index] = data[start]
        return tree[index]

    # 리프노드가 아니라면 리프노드가 될 때까지 두개의 서브트리로 나눈다.
    mid = (start + end) // 2
    tree[index] = min(init(start, mid, index * 2), init(mid + 1, end, index * 2 + 1))
    return tree[index]


# 특정 구간의 최솟값을 구하는 함수
def find(start, end, index, left, right):
    # 범위를 완전히 벗어난 경우(범위가 오른쪽으로 넘어갔거나, 왼쪽으로 넘어간 경우)
    if left > end or right < start:
        return INF

    # 범위 안에 있는 경우(left, right 사이에 start, end가 있는 경우)
    if left <= start and end <= right:
        return tree[index]

    # 그렇지 않는 경우 구간을 좀 더 좁혀서 확인한다.
    mid = (start + end) // 2
    return min(find(start, mid, index * 2, left, right), find(mid + 1, end, index * 2 + 1, left, right))


# 트리 생성
init(1, N, 1)

for _ in range(M):
    # a번째 정수부터 b번째 정수까지
    a, b = map(int, input().split())

    # a~b사이에서 최솟값 찾기
    print(find(1, N, 1, a, b))


