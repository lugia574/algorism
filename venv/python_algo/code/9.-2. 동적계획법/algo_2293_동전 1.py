#  (1 ≤ n ≤ 100, 1 ≤ k ≤ 10,000)
import sys

if __name__ == "__main__":
    input = sys.stdin.readline

    n, k = map(int, input().split())
    coin = []
    for _ in range(n):
        coin.append(int(input()))


    # 1     1
    # 2     11      2
    # 3     111     21
    # 4     1111    211 22
    # 5     11111   2111 221     5
    #