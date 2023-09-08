# https://velog.io/@dhelee/백준-6064번-카잉달력-Python-브루트-포스
# 보면

import sys

def num(M, N, x, y):
    while x <= M * N:
        if (x - y) % N == 0:
            return x
        x += M
    return -1

if __name__ == "__main__":
    input = sys.stdin.readline
    for _ in range(int(input())):
        M, N, x, y = map(int, input().split())
        print(num(M, N, x, y))