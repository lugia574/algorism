import sys

n = int(sys.stdin.readline().rstrip())
p = list(map(int, sys.stdin.readline().rstrip().split()))

# dp[i] : i개의 카드를 구매하는데 드는 최소 비용
dp = [0] * (n + 1)
dp[1] = p[0]  # 1개의 카드를 구매하는 경우는 카드 1개 포함된 카드팩 가격과 같음

for i in range(2, n + 1):
    dp[i] = p[i - 1]  # 카드 i개가 포함된 카드팩 가격으로 dp[i]를 초기화
    for j in range(1, i):  # j: 구매하는 카드팩에 들어있는 카드의 개수
        dp[i] = min(dp[i], dp[j] + dp[i - j])

print(dp[n])