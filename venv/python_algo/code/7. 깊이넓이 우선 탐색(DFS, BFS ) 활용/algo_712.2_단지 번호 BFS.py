from collections import deque
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
def groupBFS():
    global cnt

    while q:
        cnt += 1
        x, y = q.popleft()


        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx < n and 0 <= yy < n:
                if apartment[xx][yy] == 1:
                    apartment[xx][yy] = groupNum
                    q.append([xx,yy])

if __name__ == "__main__":
    n = int(input())
    apartment = []
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0 ,-1]
    q = deque()
    group = []
    groupNum = 2
    for _ in range(n):
        tmp = list(map(int,input()))
        apartment.append(tmp)

    for i in range(n):
        for j in range(n):
            if apartment[i][j] == 1:
                cnt = 0
                apartment[i][j] = groupNum
                q.append([i,j])
                groupBFS()
                group.append(cnt)
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