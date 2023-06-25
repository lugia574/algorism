# 이거 dp 자너
# 하 시바 dp 어떻게 풀었는지 다 까먹었네
# 모지리 새끼 ㄹㅇ ㅋㅋㅋ

def solution(n, money):
    dp = [0] * (n+1)
    dp[0] = 1
    for c in money:
        for i in range(c, n+1):
            dp[i] += dp[i - c]

    return dp[n] % 1000000007

if __name__ == "__main__":
    n = 5
    money = [1, 2, 5]
    result = 4

    ans = solution(n, money)
