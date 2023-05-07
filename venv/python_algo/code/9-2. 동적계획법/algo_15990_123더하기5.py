# dp[2] = 2 > 1
# dp[3] = 21, 12, 3 >  3
# dp[4] = 121, 13, 31 > 3
# dp[5] = 131, 32, 23, 212 > 4
# dp[6] = 1212, 2121, 321, 123, 132, 213,
# 는 풀이법 보니까 캬 dp 2차원 배열로 하네 ㅋㅋㅋㅋ 아 이럼 못하지 ㅋㅋㅋ ㅌㅌㅌ
# https://kwangkyun-world.tistory.com/entry/Python%ED%8C%8C%EC%9D%B4%EC%8D%AC-15990-%EB%B0%B1%EC%A4%80-1-2-3-%EB%8D%94%ED%95%98%EA%B8%B0-5
# 대충 점화식
# dp[i][0] = dp[i-1][1] + dp[i-2][2] 
# dp[i][1] = dp[i-2][0] + dp[i-2][2]
# dp[i][2] = dp[i-3][0] + dp[i-3][1]
# 참네 이걸 어떻게 알아 시이벌 아니지 이걸 알아야 그 다음을 볼 수 있는 건가 어휴 시이비랑


import sys
if __name__ == "__main__":
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        n = int(input())
        if n == 1 or n == 2:
            print(n)
            continue
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 1
        dp[3] = 3

        for i in range(4, n+1):
            dp[i] = (dp[i-3] + dp[i-2] + dp[i - 1]) % 1000000009
        print(dp[n])

