# 위와 같은 삼각형의 꼭대기에서 바닥까지 이어지는 경로 중,
# 거쳐간 숫자의 합이 가장 큰 경우를 찾아보려고 합니다.
# 아래 칸으로 이동할 때는 대각선 방향으로 한 칸 오른쪽 또는 왼쪽으로만 이동 가능합니다.
# 예를 들어 3에서는 그 아래칸의 8 또는 1로만 이동이 가능합니다.

def DFS(length, triangle, l, scoreSum, index):
    global highScore
    if l == length:
        if highScore < scoreSum:
            highScore = scoreSum
    else:
        for i in range(index, index+2):
            if 0 <= i < length:
                score = triangle[l][i]
                DFS(length, triangle, l+1, scoreSum+score, i)

def solDFS(triangle):
    global highScore
    length= len(triangle)
    DFS(length, triangle, 1, triangle[0][0], 0)
    return highScore



def solution(triangle):
    length = len(triangle)
    highScore = 0
    for i in range(1, length):
        triangle[i][0] += triangle[i - 1][0]
        triangle[i][i] += triangle[i - 1][i - 1]

    for i in range(1, length):
        for j in range(1, i):
            triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])
            if triangle[i][j] > highScore:
                highScore = triangle[i][j]

    return highScore

if __name__ == "__main__":
    triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
    result = 30
    
    res = solution(triangle)
    print(res)
    print("정답입니다." if result == res else "틀렸습니다. 모지리새끼야")