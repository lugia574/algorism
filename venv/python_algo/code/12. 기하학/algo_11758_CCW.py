# https://degurii.tistory.com/47
# 기하학 알고리즘에서 가장 기본적인 개념이라는데?

import sys

def ccw(x1, x2, x3, y1, y2, y3):
    a = (x1 * y2) + (x2 * y3) + (x3 * y1)
    b = (x2 * y1) + (x3 * y2) + (x1 * y3)
    return a - b

if __name__ == "__main__":
    input = sys.stdin.readline

    line = []
    for _ in range(3):
        line.append(list(map(int, input().split())))

    answer = ccw(line[0][0], line[1][0], line[2][0], line[0][1], line[1][1], line[2][1])
    if answer == 0:
        print(0)
    else: print(1 if answer > 0 else -1)

