# 아아니 이게 뭐야
# N명의 학생들에게 나누어 주려고 한다. 이때, 보석을 받지 못하는 학생이 있어도 된다. 하지만, 학생은 항상 같은 색상의 보석만 가져간다.
# 보석을 받지 못한 학생이 있어도 된다는게 무슨소리야
# 그러면 그냥 다 안줘버리고 한놈만 보석 하나 줘버려도 되는거 아님??????? ㄹㅇ????????
# ㄹㅇ 이해가 안가네 ㅋ
# https://kimmeh1.tistory.com/374
# 허참 허참 이해가 안간다~
import sys,math

if __name__ == "__main__":
    input= sys.stdin.readline
    n, m = map(int, input().split())
    jewelry = [int(input()) for _ in range(m)]
    lt = 1
    rt = max(jewelry)
    res = sys.maxsize
    while lt <= rt:
        mid = lt + (rt - lt) // 2
        cnt = 0
        for x in jewelry:
            if x % mid == 0:
                cnt += x // mid
            else:
                cnt += (x // mid)+1

        if cnt > n:
            lt = mid + 1
        else:
            res = min(mid, res)
            rt = mid - 1

    print(res)