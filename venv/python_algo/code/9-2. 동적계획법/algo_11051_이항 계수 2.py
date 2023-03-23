# 이거 사실상 이항 계수 1 (11050) 이랑 다를게 하나도 없음
# 단 입력 값이 다르다는것
# 이항계수 N, K 는 nCk 이라는 소리임 그러니까 n! / k! 이니까 각각 dp 값을 가지고 있으면 되는거 아닐까??

import sys
from math import factorial

if __name__ == "__main__":
    input = sys.stdin.readline
    n, k = map(int, input().split())

    facDP = [i for i in range(1, n+1)]
    for i in range(1, n):
        facDP[i] *= facDP[i-1]

    facDP.insert(0, 1)

    res = facDP[n] // (facDP[k] * facDP[n - k])
    print(res % 10007)

    # result = factorial(n) // (factorial(k) * factorial(n - k))
    # print(result % 10007)


    # 5! // (2! * 3!)
    # 5 4 3 2 1 // (2 1 * 3 2 1)