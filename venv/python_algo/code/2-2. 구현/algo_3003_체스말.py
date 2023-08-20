# 총 16개 있고 각 킹1 퀸1 룩2 비숍2 나이트2 폰8 개로 구성
# 흰색 체스가 주어졌을때 몇개를 더하거나 빼야 올바르게 되냐 구함
# 너무 쉬운데?

import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    arr = list(map(int, input().split()))
    res = [0] * 6

    for i in range(6):
        # 킹, 퀸
        if i == 0 or i == 1:
            res[i] = 1 - arr[i]
        # 폰
        elif i == 5:
            res[i] = 8 - arr[i]
        else:
            res[i] = 2 - arr[i]

    print(*res)