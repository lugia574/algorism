import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    seq = list(map(int, input().split()))

    dp = [1] * n
    # valDP = [[i] for i in seq]
    for i in range(n):
        for j in range(i):
            if seq[i] > seq[j]:
                dp[i] = max(dp[i], dp[j]+1)


    maxVal = max((dp))
    print(maxVal)

    result = []
    for i in range(n - 1, -1, -1):
        if dp[i] == maxVal:
            result.append(seq[i])
            maxVal -= 1
    result.reverse()
    for r in result:
        print(r, end=' ')