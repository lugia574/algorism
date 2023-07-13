# 난 무슨 구간합인줄 알았음
# 근데 아무리 봐도 이게 이상한거야
# 출력해야하는거랑 값 변경하는게 막 섞여있어
# 이러면 값 변경할때마다 새로 구간합을 구해야하는데
# 최악의 경우 매번 돌아야한더는거자나

# 그래서 보니가 이건 구간트리(Segment Tree)를 이용하는 문제라네
# https://one10004.tistory.com/241
# https://www.youtube.com/watch?v=075fcq7oCC8
# 세그먼트 트리는 완전 이진 트리를 기반으로 주어진 쿼리에 빠르게 응답하기 위해 만들어진 자료구조
# 각 노드는 구간, 혹은 그 구간의 정보(구간합, 구간의 최솟값 등에 대한)를 저장하고 있는 자료구조

# 이걸 좀 더 어렵게 풀려면
# https://www.youtube.com/watch?v=fg2iGP4e2mc
# Binary Indexed Tree 라는 풀이 방법인데
# 복잡도가 log 까지 가버림 미쳐버림



import sys

def init(start, end, node):
    if start == end:
        tree[node] = nums[start - 1]
        return
    mid = (start + end) // 2
    init(start, mid, node*2)
    init(mid+1, end, node*2 + 1)

    tree[node] = tree[node*2] + tree[node*2 + 1]

# 세그먼트 트리 업데이트
# lt: 노드의 왼쪽 구간
# rt: 노드의 오른쪽 구간
# node: 현재 노드
# idx: 바꿀 값의 인덱스
# val: 바꿀 값
def update(lt, rt, node, idx, val):
    if lt == rt == idx:
        tree[node] = val
        return

    # 현재 노드의 구간에 idx가 포함되지 않을 경우
    # 작업 없이 종료
    if idx < lt or rt < idx:
        return

    mid = (lt + rt) // 2
    update(lt, mid, node*2, idx, val)
    update(mid+1, rt, node * 2 + 1, idx, val)
    tree[node] = tree[node*2] + tree[node*2 + 1]

# 세그먼트 트리의 구간합
# lt: 구하고자 하는 구간합의 왼쪽 구간
# rt: 구하고자 하는 구간합의 오른쪽 구간
# node: 현재 노드
# nodeLf: 노드의 왼쪽 구간
# nodeRt: 노드의 오른쪽 구간
def merge(lt, rt, node, nodeLt, nodeRt):
    # 구하고자 하는 구간합의 구간 안에 현재 노드의 구간이 포함되지 않는다면
    # 0을 반환한다.
    if rt < nodeLt or nodeRt < lt:
        return 0

    # 구하고자 하는 구간합의 구간 안에 현재 노드의 구간이 포함된다면
    # 현재 노드의 값을 반환한다.
    if lt <= nodeLt and nodeRt <= rt:
        return tree[node]

    # 구간이 겹치는 경우에는 자식 노드에 대하여 sum 함수를 호출한다.
    mid = (nodeRt + nodeLt) // 2
    return merge(lt, rt, node*2, nodeLt, mid) + merge(lt, rt, node*2+ 1, mid + 1, nodeRt)

if __name__ == "__main__":
    input = sys.stdin.readline
    n, m, k = map(int, input().split())
    nums = [int(input()) for _ in range(n)]
    tree = [0 for _ in range(n*4)]

    init(1, n, 1)

    # print(tree)
    for _ in range(m + k):
        t, x, y = map(int, input().split())
        if t == 1:
            update(1, n, 1, x, y)
        else:
            print(merge(x, y, 1, 1, n))