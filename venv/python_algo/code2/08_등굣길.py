# 계속되는 폭우로 일부 지역이 물에 잠겼습니다.
# 물에 잠기지 않은 지역을 통해 학교를 가려고 합니다.
# 집에서 학교까지 가는 길은 m x n 크기의 격자모양으로 나타낼 수 있습니다.
#
# 아래 그림은 m = 4, n = 3 인 경우입니다.
# 가장 왼쪽 위, 즉 집이 있는 곳의 좌표는 (1, 1)로 나타내고 가장 오른쪽 아래, 즉 학교가 있는 곳의 좌표는 (m, n)으로 나타냅니다.
#
# 격자의 크기 m, n과 물이 잠긴 지역의 좌표를 담은 2차원 배열 puddles이 매개변수로 주어집니다.
# 오른쪽과 아래쪽으로만 움직여 집에서 학교까지 갈 수 있는 최단경로의 개수를 1,000,000,007로 나눈 나머지를
# return 하도록 solution 함수를 작성해주세요.


# 제한사항
# 격자의 크기 m, n은 1 이상 100 이하인 자연수입니다.
# m과 n이 모두 1인 경우는 입력으로 주어지지 않습니다.
# 물에 잠긴 지역은 0개 이상 10개 이하입니다.
# 집과 학교가 물에 잠긴 경우는 입력으로 주어지지 않습니다.
answer = 0
minCnt = 2147483647
dy = [0, 1]
dx = [1, 0]

def DFS(m, n, puddles, board,  l, cnt):
    global answer
    global minCnt
    if cnt > minCnt:
        return
    if l == (n, m):
        if cnt < minCnt:
            answer = 1
            minCnt = cnt
        elif cnt == minCnt:
            answer += 1

    else:
        y, x = l
        for i in range(2):
            yy = y + dy[i]
            xx = x + dx[i]
            if 0 < xx <= m and 0 < yy <= n:
                if [[xx,yy]] != puddles and board[yy][xx] == 0:
                    board[yy][xx] = 1
                    DFS(m, n, puddles, board, (yy, xx), cnt+1)
                    board[yy][xx] = 0

def solution(m, n, puddles):
    board = [[0] * (m+1) for _ in range(n+1)]
    board[1][1] = 1
    # DFS(m, n, puddles, board, (1,1), 0)

    for i in range(n+1):
        for j in range(m+1):
            if i == 1 and j ==1:
                continue
            if [j, i] in puddles:
                board[i][j] = 0
            else:
                board[i][j] = board[i-1][j] + board[i][j-1]
    for i in board:
        print(i)

    return answer%1000000007


if __name__ == "__main__":

    m = 4
    n = 3
    puddles = [[2, 2]]
    res = 4
    
    result = solution(m, n, puddles)
    print(result)
    print("정답입니다." if res == result else "틀렸습니다. 모지리새끼야")