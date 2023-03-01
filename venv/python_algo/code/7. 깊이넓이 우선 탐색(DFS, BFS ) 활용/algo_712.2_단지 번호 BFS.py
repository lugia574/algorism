from collections import deque
import sys
# ▣ 입력예제 1
# 7
# 0110100
# 0110101
# 1110101
# 0000111
# 0100000
# 0111110
# 0111000
# ▣ 출력예제 1
# 3
# 7
# 8
# 9
def groupBFS(x,y):
    global group
    global apart

    cnt = 0
    q = deque()
    q.append((x,y))
    while q:
        x, y = q.popleft()
        cnt += 1
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx < n and 0 <= yy < n:
                if apart[xx][yy] == 1:
                    apart[xx][yy] = groupNum
                    q.append([xx,yy])
    group.append(cnt)

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    apart = [list(map(int, input().rstrip())) for _ in range(n)]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    group = []
    groupNum = 2


    for i in range(n):
        for j in range(n):
            if apart[i][j] == 1:
                apart[i][j] = groupNum
                groupBFS(i,j)
                groupNum += 1

    print(len(group))
    group.sort()
    for i in group:
        print(i)

    # for i in range(n):
    #     for j in range(n):
    #         if apartment[i][j] > 0:
    #             apartment[i][j] -= 1
    #
    # for i in apartment:
    #     print(i)