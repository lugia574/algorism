# 섬나라 아일랜드(BFS 활용)
# 섬나라 아일랜드의 지도가 격자판의 정보로 주어집니다. 각 섬은 1로 표시되어 "상하좌우"와 "대각선"으로 연결되어 있으며,
# 0은 바다입니다. 섬나라 아일랜드에 몇 개의 섬이 있는지 구하는
# 프로그램을 작성하세요
# 1 1 0 0 0 1 0
# 0 1 1 0 1 1 0
# 0 1 0 0 0 0 0
# 0 0 0 1 0 1 1
# 1 1 0 1 1 0 0
# 1 0 0 0 1 0 0
# 1 0 1 0 1 0 0
# 만약 위와 같다면
# ▣ 입력설명
# 첫 번째 줄에 자연수 N(3<=N<=20)이 주어집니다.
# 두 번째 줄부터 격자판 정보가 주어진다.
# ▣ 출력설명
# 첫 번째 줄에 섬의 개수를 출력한다.
# ▣ 입력예제 1
# 7
# 1 1 0 0 0 1 0
# 0 1 1 0 1 1 0
# 0 1 0 0 0 0 0
# 0 0 0 1 0 1 1
# 1 1 0 1 1 0 0
# 1 0 0 0 1 0 0
# 1 0 1 0 1 0 0
# ▣ 출력예제 1
# 5
from collections import deque
def islandCnt():
    global cnt

    while q:
        x, y = q.popleft()
        cnt += 1
        for i in range(8):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx < n and 0 <= yy < n:
                if island[xx][yy] == 1:
                    island[xx][yy] = groupNum
                    q.append([xx,yy])


if __name__ == "__main__":
    n = int(input())
    island = []
    q = deque()
    res = []
    dx = [1, 1, 0, -1, -1, -1, 0, 1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]
    groupNum = 2
    for _ in range(n):
        tmp = list(map(int,input().split()))
        island.append(tmp)

    for i in range(n):
        for j in range(n):
            if island[i][j] == 1:
                cnt = 0
                island[i][j] = groupNum
                q.append([i,j])
                islandCnt()
                res.append(cnt)
                groupNum += 1

    print(len(res))
    for i in island:
        print(i)