# 체스 칠하기
# M*N 크기의 보드
# 체스판은 검은색과 흰색이 번갈아서 칠해져 있어야 한다.
# 변을 공유하는 두 개의 사각형은 다른 색으로 칠해져 있어야 한다.

# 입력
# 첫째 줄에 N과 M이 주어진다. N과 M은 8보다 크거나 같고, 50보다 작거나 같은 자연수이다.
# 둘째 줄부터 N개의 줄에는 보드의 각 행의 상태가 주어진다.
# B는 검은색이며, W는 흰색이다.
#
# 출력
# 첫째 줄에 지민이가 다시 칠해야 하는 정사각형 개수의 최솟값을 출력한다.

# 제일 첫번째를 기준으로 j 짝수는 그 반대
# 마찬가지로 i 짝수도 반대

def chess_board(row,col,chess):
    ans = 9999

    if row == 8 and col == 8:
        range_r = 1
        range_c = 1
    else:
        range_r = row-7
        range_c = col-7

    for r_index in range(range_r):
        for c_index in range(range_c):
            standard = 'B'
            for i in range(2):
                cnt = 0
                if i == 1 :
                    standard = 'W'

                for r in range(8):
                    for c in range(8):
                        if r % 2 != 0 : # i 홀수 일 경우
                            if c % 2 != 0 : # j 홀수 일 경우
                                if chess[r+r_index][c+c_index] != standard:
                                    cnt += 1
                            else: # j 짝수
                                if chess[r+r_index][c+c_index] == standard:
                                    cnt += 1

                        else: # i 짝수 일 경우
                            if c % 2 != 0 : # j 홀수
                                if chess[r+r_index][c+c_index] == standard:
                                    cnt += 1
                            else: # j 짝수
                                if chess[r+r_index][c+c_index] != standard:
                                    cnt += 1
                if ans > cnt:
                    ans = cnt

    return ans

row,col = map(int,input().split())

chess = []

for _ in range(row):
    str = list(input())
    chess.append(str)

print(chess_board(row,col,chess))