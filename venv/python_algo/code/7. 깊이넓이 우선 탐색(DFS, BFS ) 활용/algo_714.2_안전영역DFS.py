# ▣ 입력예제 1
# 5
# 6 8 2 6 2
# 3 2 3 4 6
# 6 7 3 3 2
# 7 2 5 3 6
# 8 9 5 2 7
# ▣ 출력예제 1
# 5


def safeSearchDFS(l):
    global cnt
    cnt += 1
    for i in range(4):
        x = l[0] + dx[i]
        y = l[1] + dy[i]
        if 0 <= x < n and 0 <= y < n:
            if arr[x][y] > cutLine and check[x][y] == 0:
                check[x][y] = groupNum
                safeSearchDFS([x, y])

if __name__ == "__main__":
    n = int(input())
    arr = []
    res = []
    maxCnt = -2147000000
    check = [[0] * n for _ in range(n)]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    groupNum = 2
    for _ in range(n):
        tmp = list(map(int, input().split()))
        arr.append(tmp)

    maxNum = max(map(max, arr))
    for cutLine in range(maxNum):
        for i in range(n):
            for j in range(n):
                cnt = 0
                if arr[i][j] > cutLine:
                    if check[i][j] == 0:
                        check[i][j] = groupNum
                        safeSearchDFS([i,j])
                        groupNum += 1
                        res.append(cnt)
                else:
                    check[i][j] = 1

        if len(res) > maxCnt:
            maxCnt = len(res)


        groupNum = 2
        check = [[0] * n for _ in range(n)]
        res = []

    print(maxCnt)