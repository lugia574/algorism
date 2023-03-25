# 어떤 큰 도화지에 그림이 그려져 있을 때, 그 그림의 개수와, 그 그림 중 넓이가 가장 넓은 것의 넓이를 출력하여라.
# 단, 그림이라는 것은 1로 연결된 것을 한 그림이라고 정의하자. 가로나 세로로 연결된 것은 연결이 된 것이고
# 대각선으로 연결이 된 것은 떨어진 그림이다. 그림의 넓이란 그림에 포함된 1의 개수이다.

# 첫째 줄에 도화지의 세로 크기 n(1 ≤ n ≤ 500)과 가로 크기 m(1 ≤ m ≤ 500)이 차례로 주어진다.
# 두 번째 줄부터 n+1 줄 까지 그림의 정보가 주어진다.
# (단 그림의 정보는 0과 1이 공백을 두고 주어지며, 0은 색칠이 안된 부분, 1은 색칠이 된 부분을 의미한다)

# 첫째 줄에는 그림의 개수, 둘째 줄에는 그 중 가장 넓은 그림의 넓이를 출력하여라. 단, 그림이 하나도 없는 경우에는 가장 넓은 그림의 넓이는 0이다.

# 어떻게 풀것인가
# 해당 문제는 예전에 풀었던 섬 갯수 구하기와 비슷함 DFS 로도 풀수 있고 BFS 로도 풀 수 있음
# 이번에는 BFS 로 풀자

# 1. 아이디어
# >> h x w check 배열을 선언하고 for 문을 돌려서 하나하나 들여봄
# 1이 있으면 check 를 하고 그걸 BFS 에 돌림

# 2. 시간 복잡도
# BFS 는 O(V + E ) 임
# V 는 m * n
# E 는 V * 4
# O(V + E ) == 5V == 5(m * n) == 5 * 500 * 500 == 5 * 250000 == 125만 < 2억 >>>> 쌉가능

# 3. 자료구조
# 그래프 전체 지도: int[][]
# 체크 : int [][]
# Q (BFS)
import sys
from collections import deque
def pictureCheck(dq, check, picture):
    dy = [1, 0, -1, 0]
    dx = [0, 1, 0, -1]
    pictureScale = 1
    while dq:
        y, x = dq.popleft()
        for i in range(4):
            yy = dy[i] + y
            xx = dx[i] + x
            if 0 <= yy < h and 0 <= xx < w and check[yy][xx] == 0 and picture[yy][xx]== 1:
                check[yy][xx] = 1
                dq.append([yy,xx])
                pictureScale += 1
    return pictureScale


def Solution(h, w, picture):
    dq = deque()
    check = [[0] * w for _ in range(h)]
    cnt = 0
    maxScale = 0

    for i in range(h):
        for j in range(w):
            if picture[i][j] == 1 and check[i][j] != 1:
                check[i][j] = 1
                dq.append([i,j])
                pictureScale = pictureCheck(dq, check, picture)
                cnt += 1
                if pictureScale > maxScale:
                    maxScale = pictureScale

    return [cnt, maxScale]


if __name__ == "__main__":
    h, w = map(int, input().split())
    picture = [list(map(int,input().split())) for _ in range(h)]

    # n = 6
    # m = 5
    # picture = [[1,1,0,1,1],[0,1,1,0,0],[0,0,0,0,0],[1,0,1,1,1],[0,0,1,1,1],[0,0,1,1,1]]
    # result = [4, 9]

    cnt, maxScale = Solution(h,w,picture)
    print(cnt)
    print(maxScale)
    # print("정답입니다." if cnt == result[0] and maxScale == result[1] else "틀렸습니다 모지리 새끼야")
