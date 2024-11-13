# 이런 문제를 전에도 한번 풀어본거 같은데
# 기억이 안나네 물론 그때도 이분탐색으로는 안풀었을껄
# 아마도 dp 나 BFS 로 풀지 않았을까
# 1 ≤ N ≤ 100,000, 1 ≤ M ≤ 1,000,000,000 이니까 시복 log 로 되는 방식으로 풀어야함
# 그게 이분탐색이겠고 아니면 세그먼트? 흠 뭘 기준으로 나누는데 세그먼트여 합도 아닌데
# 솔직히 이거 카테고리 이분탐색으로 안들어갔음 BFS 로 어떻게든 몸 비틀려고 했을꺼임
# 이걸 이분탐색으로 한다고 해도 어떻게 접근할껀데 lt, rt 0, 최장시간으로 잡는다고 해도 어떻게 업다운을 할껀데
# 이걸 내가 하지를 못해요
# https://wooono.tistory.com/629
# total 은 mid시간 동안 검사할 수 있는 총 사람의 수
# 이건 나중에 다시 풀어보자 너무 내가 무능하다 진짜
import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    n, m = map(int, input().split())
    times = [int(input()) for _ in range(n)]

    lt = 0
    rt = res = max(times) * m

    while lt <= rt:
        total = 0
        mid = lt + (rt - lt) // 2

        for i in range(n):
            total += mid // times[i]

        if total >= m:
            rt = mid - 1
            res = min(res, mid)
        else:
            lt = mid + 1

    print(res)


    