# 사다리 표현은 2차원 평면은 0으
# 로 채워지고, 사다리는 1로 표현합니다. 현수는 특정도착지점으로 도착하기 위해서는 몇 번째
# 열에서 출발해야 하는지 알고싶습니다. 특정 도착지점은 2로 표기됩니다. 여러분이 도와주세
# 요. 사다리의 지도가 10*10이면
# 특정목적지인 2에 도착하려면 7번 열 출발지에서 출발하면 됩니다.
# ▣ 입력설명
# 10*10의 사다리 지도가 주어집니다.
# ▣ 출력설명
# 출발지 열 번호를 출력하세요.
# ▣ 입력예제 1
# 1 0 1 0 0 1 0 1 0 1
# 1 0 1 1 1 1 0 1 0 1
# 1 0 1 0 0 1 0 1 0 1
# 1 0 1 0 0 1 0 1 1 1
# 1 0 1 0 0 1 0 1 0 1
# 1 0 1 1 1 1 0 1 0 1
# 1 0 1 0 0 1 0 1 1 1
# 1 1 1 0 0 1 0 1 0 1
# 1 0 1 0 0 1 1 1 0 1
# 1 0 1 0 0 2 0 1 0 1
# ▣ 출력예제 1
# 7
import sys


def ladderDFS(loc):
    global start
    x, y = loc
    if x == 9:
        if board[x][y] == 2:
            print(start)
            sys.exit(0)

    else:
        y1 = y - 1
        y2 = y + 1

        if 0 <= y1 < 10 and board[x][y1] == 1 and check[x][y1] == 0:
            y = y1
        elif 0 <= y2 < 10 and board[x][y2] == 1 and check[x][y2] == 0:
            y = y2
        else:
            x += 1

        check[x][y] = 1
        ladderDFS([x,y])



if __name__ == "__main__":
    board = [list(map(int, input().split())) for _ in range(10)]
    for i in range(10):
        if board[0][i] == 1:
            check = [[0]*10 for _ in range(10)]
            start = i
            ladderDFS([0,i])


