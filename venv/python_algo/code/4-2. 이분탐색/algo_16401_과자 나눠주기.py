# 떡볶이 문제보다 약간 심화같은데
# 나눠줘야 할 인원은 막 4명인데 과자는 3개야
# 즉 나머지값도 취급해주는다는 소리 아님?
# 하지만~ 잘 해결했습니다요~ 는 안됨 ㅋ
# lt 를 0 으로 둬서 틀렸었네
# 그것도 모르고 헛짓함 ㅋ
import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    m, n = map(int, input().split())
    arr = list(map(int, input().split()))
    lt = 1
    rt = max(arr)
    res = 0

    while lt <= rt:
        mid = lt + (rt - lt) // 2
        cnt = 0
        for x in arr:
            if mid < 1:break
            if x >= mid:
                cnt += x // mid

        if cnt >= m:
            res = max(mid, res)
            lt = mid + 1
        else:
            rt = mid - 1

    print(res)

