import sys
def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    elif dp[a][b][c]:
        return dp[a][b][c]
    elif a < b and b < c:
        dp[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return dp[a][b][c]
    else:
        dp[a][b][c] = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)
        return dp[a][b][c]


if __name__ == "__main__":
    input = sys.stdin.readline
    while True:
        a, b, c = map(int, input().split())
        dp = [[[0]*(21) for _ in range(21)] for _ in range(21)]
        if a == -1 and b == -1 and c == -1: break

        print(f"w({a}, {b}, {c}) = {w(a,b,c)}")