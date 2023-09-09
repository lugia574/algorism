# 딱 봐도 dp 문제 인거 같은뎁쇼ㅛ쇼쇼쇼
# 1 1
# 2 11/ 2
# 3 111/ 21/ 12
# 4 1111/ 112/ 211/ 121/ 22

def solution(n):
    if n == 1:
        return 1

    dp = [0] * (n+1)
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n+1):
        dp[i] = (dp[i-1] + dp[i-2]) % 1234567
    return dp[n]


if __name__ == "__main__":
    answer = solution(1)
    res = 1
    print(answer == res)

    answer = solution(3)
    res = 3
    print(answer == res)