# 안전영역
# ▣ 입력설명
# 첫째 줄에는 어떤 지역을 나타내는 2차원 배열의 행과 열의 개수를 나타내는 수 N이
# 입력된다. N은 2 이상 100 이하의 정수이다. 둘째 줄부터 N 개의 각 줄에는 2차원 배열의 첫
# 번째 행부터 N번째 행까지 순서대로 한 행씩 높이 정보가 입력된다. 각 줄에는 각 행의 첫
# 번째 열부터 N번째 열까지 N 개의 높이 정보를 나타내는 자연수가 빈 칸을 사이에 두고
# 입력된다. 높이는 1이상 100 이하의 정수이다.
# ▣ 출력설명
# 첫째 줄에 장마철에 물에 잠기지 않는 안전한영역의 최대 개수를 출력한다.
# ▣ 입력예제 1
# 5
# 6 8 2 6 2
# 3 2 3 4 6
# 6 7 3 3 2
# 7 2 5 3 6
# 8 9 5 2 7
# ▣ 출력예제 1
# 5
from collections import deque


# BFS
def safeSearchBFS(cutLine):
    cnt = 0
    while q:
        s = q.popleft()
        cnt += 1
        for i in range(4):
            x = s[0] + dx[i]
            y = s[1] + dy[i]
            if 0 <= x < n and 0 <= y < n:
                if arr[x][y] > cutLine and check[x][y] == 0:
                    check[x][y] = index
                    q.append([x,y])
    return cnt



if __name__ == "__main__":
    n = int(input())
    arr = []
    res = []
    maxCnt = -2147000000
    maxIndex = -2147000000

    q = deque()
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    index = 2
    for _ in range(n):
        tmp = list(map(int, input().split()))
        arr.append(tmp)

    maxNum = max(map(max, arr))

    for x in range(maxNum):
        check = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if arr[i][j] > x:
                    if check[i][j] == 0:
                        q.append([i,j])
                        check[i][j] = index
                        cnt = safeSearchBFS(x)
                        index += 1
                        res.append(cnt)
                else:
                    check[i][j] = 1

        if len(res) > maxCnt:
            maxCnt = len(res)
            maxIndex = x

        index = 2
        cnt = 0
        res = []

    print(maxCnt)
    #print(maxIndex)