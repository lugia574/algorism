# 자 오랜만에 dp 풀어서 약간 머리가 안돌아가는데
# 공통 부분 수열임 별거 없음
# 두 문자열을 기준으로 이중 포문을 돌려서
# i 는 첫번째 문자열
# j 는 두번째 문자열을 해서 돌려
# i == j 이면 dp[i][j] 에 저장을 하는거지
# dp[i][j] = dp[i-1][j-1] + 1 해서 전에 값에 덧붙혀서 하는거야
# 단순히 한글자만 맞는 경우는 단순히 1 만 될것이고 2자리수 이상이면 dp[i-1][j-1] 로 차근 차근 쌓이겠지
import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    str1 = input().rstrip()
    str2 = input().rstrip()

    str1Length = len(str1)
    str2Length = len(str2)
    dp = [[0] * str2Length for _ in range(str1Length)]
    answer = 0

    for i in range(str1Length):
        for j in range(str2Length):
            if str1[i] == str2[j]:
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j-1] + 1
                answer = max(answer, dp[i][j])

    print(answer)