# 나 이거 대체 무슨식으로 전개되는지 전혀 이해가 안갔는데
# https://velog.io/@solser12/백준-2243-사탕상자-JAVA
# 이걸 보니까 이해함
# 대충 말로 설명을 하자면
# 왼쪽부터 쭉 나열을 한다고 해보자 맛-갯수 순으로
# 1-3, 2-4, 3-1, 4-1, 5-4  // 대충 이렇다고 해보자
# 여기서 등수는 즉 왼쪽순으로 갯수에 따라 간다 1~3위까지는 맛이 1 이고
# 4위부터는 7위까지는 2, 8위는 3 이렇게
# 그렇기에 구간합으로
# 1-3, 2-4 의 갯수를 더한 것의 의미는 1 ~ 7 까지 등수를 말한다고 할 수 있다
# 반대쪽은 8, 9 등을 말하는거고 또 이 둘을 합치면 1 ~ 9 까지라고 할 수 있음
# 그러면 이상태에서 만약 8등을 찾는다고 해보자 그럼 8은 9 보다 작으니까 1~9 안에 들어옴
# 여기서 왼쪽 1~7 을 비교해서 8이 더 크니까 오른쪽으로 가는거임
# 자 그럼 오른쪽으로 갔을땐 어떻게 해야할까
# tree 에는 등수를 기록한게 아니라 갯수를 기록할꺼니까 8이 오르쪽으로 갔다면 맞이하는건 1, 1 일 상태일텐데
# 오른쪽으로 가게 되면 왼쪽값을 빼주면 됨 (rank - left)


import sys
sys.setrecursionlimit(int(1e9))

class SegmentTree:
    def __init__(self, arr, N):
        self.arr = arr
        self.tree = [0] * (N * 4)

    def query(self, cur, start, end, rank):
        if start == end:
            return start

        mid = start + (end - start) // 2
        left = self.tree[cur * 2]
        if left >= rank:
            return self.query(cur*2, start, mid, rank)
        return self.query(cur*2+1, mid+1, end, rank - left)

    def update(self, cur, start, end, idx, diff):
        if end < idx or idx < start:
            pass
        elif start == end:
            self.tree[cur] += diff
        else:
            mid = start + (end - start) // 2
            left = self.update(cur*2, start, mid, idx, diff)
            right = self.update(cur*2+1, mid+1, end, idx, diff)
            self.tree[cur] = left + right
        return self.tree[cur]

if __name__ == "__main__":
    input = sys.stdin.readline
    t = int(input())

    N = 1_000_000 + 1
    tree = SegmentTree([0] * N, N)
    answer = []

    for _ in range(t):
        order, *content = map(int, input().split())
        if order == 1:
            # 사탕 꺼내기
            out = tree.query(1, 1, N, content[0])
            print(out)
            tree.update(1, 1, N, out, -1)

        else:
            tree.update(1, 1, N, content[0], content[1])
