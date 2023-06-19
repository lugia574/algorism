# https://velog.io/@uoayop/BOJ-1072-게임Python
import sys

def winrate(x, y):
    z = (y * 100) // x
    if z >= 99:
        return -1

    rt = x
    lt = 1
    answer = 0

    while lt <= rt:
        mid = (rt + lt) // 2
        midAvg = (y + mid) * 100 // (x+mid)
        if midAvg <= z:
            lt = mid + 1
        else:
            answer = mid
            rt = mid - 1

    return answer
if __name__ == "__main__":
    input = sys.stdin.readline
    x, y = map(int, input().split())
    answer = winrate(x, y)
    print(answer)


