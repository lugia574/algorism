# https://jih3508.tistory.com/50
# 구간 합에 대한 개념임 dp 같은걸로 하나씩 index 의 합들을 구하고
# (st-1) ~ end 번째 를 구하면 되는거임
import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))

    dp = [0] * (n+1)
    for i in range(0, n):
        dp[i+1] = dp[i] + nums[i]
    for _ in range(m):
        st, end = map(int, input().split())
        print(dp[end] - dp[st-1])