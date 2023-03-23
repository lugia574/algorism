import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    dp = [-1] * (n+1)

    for i in (3, 5):
        for j in range(3, n+1):
            if j >= i:
                if j % i == 0:
                    dp[j] = j // i
                elif dp[j-i] != -1:
                    dp[j] = dp[j-i] + 1


    print(dp[n])

    # 1  ~   3      4       5       6       7       8       9       10      11      12      13      14      15      16      17      18
    # 3>     1      -1      -1      2       -1      -1      3       -1      -1      4       -1      -1      5       -1      -1      6
    # 5>     1      -1      1       2       -1      2       3       2       3      4       3       4       3        4       5      4