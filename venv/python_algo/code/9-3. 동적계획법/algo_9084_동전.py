import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        n = int(input()) # 동전의 가짓수
        coin = list(map(int, input().split())) # 동전
        target = int(input())

        dp = [0] * (target + 1)
        dp[0] = 1
        for c in coin:
            for i in range(1, target + 1):
                if i - c >= 0:
                    dp[i] += dp[i - c]

        print(dp[target])