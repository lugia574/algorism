# dp 라고 무조건 계산된 값을 저장하는게 아님
# 계산됐는지 안됐는지 여부를 저장할 수 있음
# 이 문제의 경우
# 추를 왼쪽에 올린다, 오른쪽에 올린다, 올리지 않는다 로 할 수 있음

import sys
sys.setrecursionlimit(int(1e9))

def dfs(cur, leftW, rightW):
    newW = abs(leftW - rightW)

    if newW not in resSet:
        resSet.add(newW)

    if cur == n: return

    if dp[cur][newW] == False:
        dp[cur][newW] = True
        dfs(cur + 1, leftW + weight[cur], rightW)
        dfs(cur + 1, leftW, rightW + weight[cur])
        dfs(cur + 1, leftW, rightW)

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    weight = list(map(int, input().split()))
    sumW = sum(weight)

    dp = [[False] * (sumW+1) for _ in range(n)]
    resSet = set()
    m = int(input())
    targets = list(map(int, input().split()))
    dfs(0, 0, 0)
    for t in targets:
        print("Y" if t in resSet else "N", end=" ")