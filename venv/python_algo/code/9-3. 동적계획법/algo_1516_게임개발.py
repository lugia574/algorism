# 참내 이걸 주석을 안달았네
# 이거 만약에 다시 풀면 나 100퍼 못풀텐데 뭔 자신감으로 안했데? ㅋ
# 자 값을 하나씩 받아
# 여기서 뭐를 사전에 해야한다는게 없는 바로 -1 상태면 바로 dp에 박아버려
# 사전에 필요한것들이 있는 것들은 하나하나 보면서 해당 노드가 필요로하는 노드들을 체크하고 해당 노드는 엣지가 몇개인지도 세
# 그리고 이제 while 문을 도는거야 que 하나씩 빼면서
#
import sys
from collections import deque

def simCity(n):
    seq = [[] for _ in range(n+1)] # 건설 순서 규칙
    inDegree = [0] * n # 진입찻수
    dp = [0] * n
    q = deque()
    cost = []
    # 건설 순서 및 진입차수 없는 애는 바로 dp로 박을 꺼임
    for i in range(n):
        build = list(map(int, input().rsplit()))
        cost.append(build[0])
        if build[1] == -1:
            dp[i] = build[0]
            q.append(i)

        for x in build[1:]:
            if x == -1:
                break
            seq[x-1].append(i)
            inDegree[i] += 1
    # print(seq)
    while q:
        b = q.popleft()
        for x in seq[b]:
            inDegree[x] -= 1
            dp[x] = max(dp[b] + cost[x], dp[x])
            if inDegree[x] == 0:
                q.append(x)

    return dp

if __name__== "__main__":
    input = sys.stdin.readline
    n = int(input())
    res = simCity(n)
    for i in res:
        print(i)
