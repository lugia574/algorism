import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    el = []
    for i in range(n):
        el.append(list(map(int, input().split())))

    el.sort(key= lambda x: x[0])
    b = [i[1] for i in el]
    dp = [1] * n

    for i in range(n):
        for j in range(i):
            if b[i] > b[j]:
                dp[i] = max(dp[j] + 1, dp[i])

    #print(dp)
    print(n-max(dp))