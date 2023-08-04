# 대충 이게 N 이 500,000 인데 무조건 2N 인거니 1,000,000 백만 이라고 봐도 무방하지 않을까
# 그럼 2중 포문으로 돌려서 count 해서 값 출력 같은건 불가능하다 봐야겠지
# dp 도 마찬가지일꺼고 애초에 dp 로 풀순 있나? 점화식이 안되는데?
# 최소를 찾는것도 아니니 다익스트라 같은건 필요없고
# 근데 이게 왜 세그먼트 트리인지 모르겟어
# 뭘로 구간을 나눈다는거야
# 구간을 나눌 수 있어야 세그먼트 트리가 되는거 아녀 합이든 곱이든 최소이든
# 보니까 솔직히 어렵다
# 이걸 보고 푼다고 해서 다음에는 안보고 풀수 있을까?
# 참내 이해도 못했는데 시초란다
# https://hooongs.tistory.com/118
# 솔직히 이해가 잘 안가 결국 계산값이 4인데 왜 3이냐
# 글고 이건 펜윅트리로 해야할듯
# https://juhongyee.tistory.com/15?category=1108511
import sys, math

def update(cur, start, end, idx):
    if idx < start or idx > end:
        return 0
    if start == end:
        tree[cur] = 1
        return tree[cur]

    mid = start + (end - start) // 2
    update(cur*2, start, mid, idx)
    update(cur*2+1, mid+1, end, idx)
    tree[cur] = tree[cur*2] + tree[cur*2+1]
    return tree[cur]

def query(cur, start, end, left, right):
    if right < start or end < left:
        return 0
    if left <= start and end <= right:
        return tree[cur]

    mid = start + (end - start) // 2
    lt = query(cur*2, start, mid, left, right)
    rt = query(cur*2+1, mid+1, end, left, right)

    tree[cur] = lt + rt
    return tree[cur]


if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    arrA = list(map(int, input().split()))

    arrB = {}
    for i, x in enumerate(map(int, input().split())):
        arrB[x] = i

    h = int(math.ceil(math.log2(n)))
    size = 1 << (h+1)
    tree = [0] * size
    answer = 0

    for num in arrA:
        idx = arrB[num]
        answer += query(1, 1, n, idx, n)

        update(1, 1, n, idx)

    print(answer)
    print(tree)