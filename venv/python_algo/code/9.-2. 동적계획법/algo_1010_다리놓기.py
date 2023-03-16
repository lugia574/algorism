import sys
# https://velog.io/@uoayop/BOJ-1010-%EB%8B%A4%EB%A6%AC-%EB%86%93%EA%B8%B0Python
# https://st-lab.tistory.com/194
#  (0 < N ≤ M < 30)
if __name__ == "__main__":
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        n, m = map(int, input().split())

        if n == m or n == 1:
            print(1 if n == m else m)
            continue

        dp = [[0] * (m+1) for _ in range(n+1)]

        for i in range(1, n+1):
            for j in range(i, m+1):
                if i == 1:
                    dp[i][j] = j
                elif i == j:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i][j-1] + dp[i-1][j-1]


        print(dp[n][m])

