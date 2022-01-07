# N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.
# N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.

# 푸는 방법 생각하기
# 좌표 찍기 전용 펑션을 하나 더 만들자
# 그리고 해당 N 번 펑션 재귀로 ㄱㄱ

#


def queen_of_cases(N):

    ans_cnt = 0

    for x in range(len(board)):
        for y in range(len(board)):
            board = [[0 for col in range(N)] for row in range(N)]
            cnt = board_check(N, board,x,y,0)
            sum_cnt += cnt



    return ans_cnt

def board_check(N, board, x,y , tr):
    if board[x][y] == 1:
        return 0

    # x, y 해당 값과 퀸의 동선 부분을 전부다 '1' 만들어
    for i in range(len(board)):
        board[x][y+i] = 1
        board[x+i][y] = 1
        board[x+i][y+i] = 1

    for x in range(len(board)):
        for y in range(len(board)):
            board_check(N, board, x,y, tr+1)



    return board

N = int(input())
ans = queen_of_cases(N)

print(ans)