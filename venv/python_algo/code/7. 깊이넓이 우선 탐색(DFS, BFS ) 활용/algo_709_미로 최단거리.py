# 7*7 격자판 미로를 탈출하는 최단경로의 경로수를 출력하는 프로그램을 작성하세요. 경로수는
# 출발점에서 도착점까지 가는데 이동한 횟수를 의미한다. 출발점은 격자의 (1, 1) 좌표이고, 탈
# 출 도착점은 (7, 7)좌표이다. 격자판의 1은 벽이고, 0은 도로이다.
# 격자판의 움직임은 상하좌우로만 움직인다. 미로가 다음과 같다면

# 출 0 0 0 0 0 0
# 0 1 1 1 1 1 0
# 0 0 0 1 0 0 0
# 1 1 0 1 0 1 1
# 1 1 0 1 0 0 0
# 1 0 0 0 1 0 0
# 1 0 1 0 0 0 도

# 위와 같은 경로가 최단 경로이며 경로수는 12이다.
# ▣ 입력설명
# 7*7 격자판의 정보가 주어집니다.
# ▣ 출력설명
# 첫 번째 줄에 최단으로 움직인 칸의 수를 출력한다. 도착할 수 없으면 -1를 출력한다.
# ▣ 입력예제 1
# 0 0 0 0 0 0 0
# 0 1 1 1 1 1 0
# 0 0 0 1 0 0 0
# 1 1 0 1 0 1 1
# 1 1 0 1 0 0 0
# 1 0 0 0 1 0 0
# 1 0 1 0 0 0 0
# ▣ 출력예제 1
# 12
from collections import deque

def mazeBFS():
    l = 0
    while q:
        length = len(q)
        for x in range(length):
            node = q.popleft()
            for i in range(4):
                if 0 <= node[0] + dx[i] < 7 and 0 <= node[1] + dy[i] < 7:
                    if [node[0] + dx[i], node[1] + dy[i]] == [6,6]:
                        l += 1
                        return l
                    if board[node[0] + dx[i]][node[1] + dy[i]] == 0:
                        q.append([node[0]+dx[i], node[1]+dy[i]])
                        board[node[0] + dx[i]][node[1] + dy[i]] = 2
        l += 1
    return -1

if __name__ == "__main__":
    board = []
    dx = [1, -1, 0 , 0]
    dy = [0, 0, 1, -1]
    for _ in range(7):
        tmp = list(map(int,input().split()))
        board.append(tmp)
    dis = [[0] * 7 for _ in range(7)]
    q = deque()
    board[0][0] = 1
    q.append([0,0])
    res = mazeBFS()
    print(res)



