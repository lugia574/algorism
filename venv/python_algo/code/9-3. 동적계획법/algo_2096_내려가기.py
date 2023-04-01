import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())

    maxDP = [[0] * n for _ in range(n)]
    minDP = [[0] * n for _ in range(n)]


    for i in range(n):
        x, y, z = map(int, input().split())
        for j in range(3):
            if j == 0:
                maxDP[i][j] = max(maxDP[i - 1][j], maxDP[i - 1][j + 1]) + x
                minDP[i][j] = min(minDP[i - 1][j], minDP[i - 1][j + 1]) + x

            elif j == n-1:
                maxDP[i][j] = max(maxDP[i - 1][j], maxDP[i - 1][j - 1]) + z
                minDP[i][j] = min(minDP[i - 1][j], minDP[i - 1][j - 1]) + z
            else:
                maxDP[i][j] = max(maxDP[i - 1][j], maxDP[i - 1][j - 1], maxDP[i - 1][j + 1]) + y
                minDP[i][j] = min(minDP[i - 1][j], minDP[i - 1][j - 1], minDP[i - 1][j + 1]) + y

    print(max(maxDP[n-1]), min(minDP[n-1]))






    n = int(input())

    max_dp = [0] * 3
    min_dp = [0] * 3

    max_tmp = [0] * 3
    min_tmp = [0] * 3

    for i in range(n):
        a, b, c = map(int, input().split())
        for j in range(3):
            if j == 0:
                max_tmp[j] = a + max(max_dp[j], max_dp[j + 1])
                min_tmp[j] = a + min(min_dp[j], min_dp[j + 1])
            elif j == 1:
                max_tmp[j] = b + max(max_dp[j - 1], max_dp[j], max_dp[j + 1])
                min_tmp[j] = b + min(min_dp[j - 1], min_dp[j], min_dp[j + 1])
            else:
                max_tmp[j] = c + max(max_dp[j], max_dp[j - 1])
                min_tmp[j] = c + min(min_dp[j], min_dp[j - 1])

        for j in range(3):
            max_dp[j] = max_tmp[j]
            min_dp[j] = min_tmp[j]

    print(max(max_dp), min(min_dp))