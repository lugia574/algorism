# 나 이게 어떻게 dp 로 한지 모르겠는데??
# https://maivve.tistory.com/322
# 부모 노드가 얼리어답터가 아니면 자식 노드들은 전부 얼리어답터여야 하지만,
# 부모 노드가 얼리어답터이면 자식 노드들은 반드시 얼리어답터여야 하지 않아도 됩니다.

# 이걸 말하는게  dp[l][0] += dp[i][1] 이부분인듯?
# 이럼 무조건 부모노드가 얼리가 아닐때 자식 노드는 얼리라는 소리자너
# 그리고 부모노드가 얼리가 맞다면 이제 자식노드가 얼리일때랑 아닐때랑 비교를 해서 더 낮은값을 더해주는거지

# 자식의 자식 노드가 얼리냐 아니냐를 따지기 위해서
# BFS 가 아닌 DFS 로 깊이 들어가서 마지막 노드부터 하나씩 위로 올라가는 형태로 구현한거고
import sys
sys.setrecursionlimit(10 ** 9)

def DFS(l):
    visited[l] = 1
    # dp[l][0] = 0
    # dp[l][1] = 1
    
    for i in nodes[l]:
        if visited[i] == 0:
            DFS(i)
            dp[l][0] += dp[i][1]
            dp[l][1] += min(dp[i][0], dp[i][1])

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    nodes = [[] for _ in range(n+1)]
    dp = [[0,1] for _ in range(n+1)]
    visited = [0] * (n+1)

    for _ in range(n-1):
        a, b = map(int, input().rsplit())
        nodes[a].append(b)
        nodes[b].append(a)

    DFS(1)
    print(min(dp[1][0], dp[1][1]))