# https://seongonion.tistory.com/103
# https://www.youtube.com/watch?v=QFKIl1AbqBI
# 백트레킹 문제
import sys

def check(x):
    for i in range(x):
        if chess[x] == chess[i] or abs(chess[x] - chess[i]) == abs(x - i):
            return False

    return True


def queens(x):
    global res
    if x == n:
        res += 1
        return
    else:
        for i in range(n):
            chess[x] = i
            if check(x):
                queens(x + 1)


if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    chess = [0] * n
    res = 0

    queens(0)
    print(res)