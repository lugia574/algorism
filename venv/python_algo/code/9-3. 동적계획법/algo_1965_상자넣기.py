import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    boxs = list(map(int, input().split()))
    dp = [1] * n
    for i in range(n):
        num = boxs[i]
        for j in range(0, i):
            if boxs[i] > boxs[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    print(max(dp))

    # 8
    # 1 6 2 5 7 3 5 6
    # 1 6 7
    # 1 2 5 7
    # 1 2 3 5 6