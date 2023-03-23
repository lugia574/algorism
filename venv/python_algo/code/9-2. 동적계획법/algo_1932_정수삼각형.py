import sys

def dfs(l, idx, s):
    if l == n:
        dp[idx] = max(dp[idx], s)
        return
    else:
        for i in range(2):
            dfs(l + 1, idx+i, s + triangle[l][idx+i])

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    trg = []

    for i in range(n):
        trg.append(list(map(int, input().split())))
    node = 2
    for i in range(1, n):
        for j in range(node):
            if j == 0:
                trg[i][j] = trg[i][j] + trg[i-1][j]
            elif i == j:
                trg[i][j] = trg[i][j] + trg[i - 1][j - 1]
            else:
                trg[i][j] = max(trg[i-1][j-1], trg[i - 1][j]) + trg[i][j]

        node += 1

    print(max(trg[n-1]))

