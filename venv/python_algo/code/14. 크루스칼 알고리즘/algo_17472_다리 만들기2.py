# 다리의 길이는 2 이상이어야 한다.
# 방향이 가로인 다리는 다리의 양 끝이 가로 방향으로 섬과 인접해야 하고, 방향이 세로인 다리는 다리의 양 끝이 세로 방향으로 섬과 인접
# 먼가 제약이 많네
# 1. 우선 BFS 를 이용해서 섬을 구별하고 cnt 해줘
# 2. 해당 번호를 기점으로 한칸씩 앞으로 가면서 다른 섬을 만날때까지 거리를 재
# 3. 다른 섬을 만나면 그게 union 되어 있는지 보고 안되있음 union 하고 해당 거리값을 뱉어
# 4. 그 뱉은 값들은 sum 해서 출력
# 여기서 제약사항인 다리 길이가 2 이상 이건 쉬움
# 문제는 가로인 다리는 가로로 쭉 가야하고 세로면 세로로 쭉 가야함
# 라고 했는데 개같이 틑려서 그냥 딴사람꺼 봐야할듯
# https://one10004.tistory.com/250
# https://www.youtube.com/watch?v=Vop0L7vU1-0
# 접근방식은 같았음
# 근데 내가 막 마구잡이로 할려고해서 그런듯?
# 근데 이게 난이도 플레가 왜 아니지 ㅋㅋ 골1 이라고? 그런거 같기도하고 ㅋ

import sys
import heapq

input = sys.stdin.readline
dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
INF = 987654321


def find(a):
    if parent[a] < 0:
        return a

    parent[a] = find(parent[a])
    return parent[a]


def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def isRange(x, y):
    return 0 <= x < N and 0 <= y < M


# 섬에 번호 붙이기
def checkIsland(x, y, num):
    q = [(x, y)]
    visited[x][y] = True
    board[x][y] = num

    while q:
        x, y = q.pop(0)

        for (dx, dy) in dir:
            nx = x + dx
            ny = y + dy

            if not isRange(nx, ny) or visited[nx][ny] or board[nx][ny] == 0:
                continue

            board[nx][ny] = num
            visited[nx][ny] = True
            q.append((nx, ny))


# startIsland에서 다른 섬으로 가는 다리를 만들면서 그 중 최소 길이를 갖는 다리의 정보를 기록하기 위한 함수
def checkBridge(x, y, startIsland):
    for (dx, dy) in dir:
        nx, ny = x, y
        bridgeLength = 0

        # 한 쪽으로 쭉 뻗어 나가면서 다리를 만들 수 있는지를 체크한다.
        while True:
            nx += dx
            ny += dy

            # 범위를 벗어났거나 자기 자신을 만나면 탐색 종료
            if not isRange(nx, ny) or board[nx][ny] == startIsland:
                break

            # 다른 섬을 만났으나 다리의 길이가 1이면 탐색 종료
            if bridgeLength == 1 and board[nx][ny] != 0:
                break

            # 길이가 2 이상인 다리를 만들 수 있다면 가장 짧은 다리인가를 체크하여 업데이트한다.
            if board[nx][ny] != 0 and bridgeLength != 1:
                endIsland = board[nx][ny]
                birdgeInfo[startIsland][endIsland] = min(birdgeInfo[startIsland][endIsland], bridgeLength)
                break

            bridgeLength += 1


if __name__ == '__main__':
    N, M = map(int, input().split())  # 세로 크기, 가로 크기
    board = []

    for _ in range(N):
        board.append(list(map(int, input().split())))

    islandNum = 1  # 섬에 붙일 번호
    visited = [[False for _ in range(M)] for _ in range(N)]

    # 각 섬에 번호를 붙여주는 작업을 한다.
    for i in range(N):
        for j in range(M):
            if visited[i][j] or board[i][j] == 0:
                continue
            checkIsland(i, j, islandNum)
            visited[i][j] = True
            islandNum += 1

    # 각 섬에서 섬까지 가는 다리 중 최소 길이 (ex. bridgeInfo[1][2] -> 1번 섬에서 2번 섬으로 가는 다리의 최소 길이)
    birdgeInfo = [[INF for _ in range(islandNum)] for _ in range(islandNum)]

    # a섬에서 b섬으로 가기 위한 다리 중 최소 길이를 구한다.
    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:
                continue
            checkBridge(i, j, board[i][j])

    bridgeList = []  # 만들어둔 다리들을 다리의 길이를 기준으로 최소 힙을 만든다. (다리의 길이, 시작 섬, 도착 섬) 형태의 튜플

    for i in range(1, islandNum):
        for j in range(i + 1, islandNum):
            if birdgeInfo[i][j] == INF:
                continue

            heapq.heappush(bridgeList, (birdgeInfo[i][j], i, j))

    # 크루스칼 알고리즘을 사용하여 사용할 다리를 선택한다.
    parent = [-1 for _ in range(islandNum)]
    bridgeCount = 0  # 사용된 다리의 수
    totalBridgeLength = 0  # 선택된 다리의 길이 합

    while bridgeList:
        bridgeLength, startIsland, endIsland = heapq.heappop(bridgeList)

        if find(startIsland) != find(endIsland):
            union(startIsland, endIsland)
            bridgeCount += 1
            totalBridgeLength += bridgeLength

        if bridgeCount == islandNum - 2:  # (섬의 개수 - 1)개의 다리를 사용했다면 탐색 종료
            break

    # 만약 사용된 다리의 수가 (섬의 개수 - 1)이 되지 않는다면 이는 모든 섬이 연결되지 않았다는 뜻이므로 -1을 출력한다.
    if bridgeCount != islandNum - 2:
        print(-1)
    else:
        print(totalBridgeLength)