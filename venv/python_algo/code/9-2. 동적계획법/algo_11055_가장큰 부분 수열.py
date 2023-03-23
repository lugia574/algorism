import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    arr = list(map(int, input().split()))

    dp = [0] * n

    for i in range(n):
        dp[i] = arr[i]
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + arr[i])
    #print(dp)
    print(max(dp))

# 12
# 1 100 2 50 30 40 60 3 5 6 7 8

# 답 1 + 2 + 30 + 40 + 60 = 133