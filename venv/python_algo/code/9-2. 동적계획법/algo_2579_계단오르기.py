# 계단은 한 번에 한 계단씩 또는 두 계단씩 오를 수 있다. 즉, 한 계단을 밟으면서 이어서 다음 계단이나, 다음 다음 계단으로 오를 수 있다.
# 연속된 세 개의 계단을 모두 밟아서는 안 된다. 단, 시작점은 계단에 포함되지 않는다.
# 마지막 도착 계단은 반드시 밟아야 한다.

import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    stairs = [0] * 301
    dp = [0] * 301
    for i in range(n):
        stairs[i]= int(input())


    dp[1] = stairs[0]
    dp[2] = stairs[0] + stairs[1]
    for i in range(3, n+1):
        dp[i] = max(dp[i-3] + stairs[i - 2] + stairs[i - 1], dp[i - 2] + stairs[i - 1])

    print(dp[n])


