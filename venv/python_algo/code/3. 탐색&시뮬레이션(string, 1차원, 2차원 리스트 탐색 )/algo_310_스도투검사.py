# 스도쿠가 주어지고 해당 표가 완벽한 스도쿠가 맞는지 판단하는 function 을 만들어라
#
# ▣ 입력설명
# 첫 번째 줄에 완성된 9×9 스도쿠가 주어집니다.
# ▣ 출력설명
# 첫째 줄에 “YES" 또는 ”NO"를 출력하세요.
#
# ▣ 입력예제 1
# 1 4 3 6 2 8 5 7 9
# 5 7 2 1 3 9 4 6 8
# 9 8 6 7 5 4 2 3 1
# 3 9 1 5 4 2 7 8 6
# 4 6 8 9 1 7 3 5 2
# 7 2 5 8 6 3 9 1 4
# 2 3 7 4 8 1 6 9 5
# 6 1 9 2 7 5 8 4 3
# 8 5 4 3 9 6 1 2 7
# ▣ 출력예제 1
# YES

def sudokuChecker (arr):

    for i in range(9):
        checkRow = [False] * 10
        checkColumn = [False] * 10
        for j in range(9):
            print("행 : arr",i,j," >> ",arr[i][j],"::", checkRow[arr[i][j]],"행 전체" ,checkRow)
            print("열 : arr", j, i, " >> ",arr[j][i],"::", checkColumn[arr[j][j]],"열 전체", checkColumn)

            if not checkRow[arr[i][j]]:
                checkRow[arr[i][j]] = True
            else:
                return "NO"
            if not checkColumn[arr[j][i]]:
                checkColumn[arr[j][i]] = True
            else:
                return "NO"

    for i in range(3):
        for j in range(3):
            checkGroup = [False] * 10
            for i2 in range(3):
                for j2 in range(3):
                    print("그룹 : arr", i * 3 + i2, j * 3 + j2, " >> ",arr[i * 3 + i2][j * 3 + j2],"::", checkGroup[arr[i * 3 + i2][j * 3 + j2]],"그룹 전체", checkGroup)
                    if not checkGroup[arr[i * 3 + i2][j * 3 + j2]]:
                        checkGroup[arr[i * 3 + i2][j * 3 + j2]] = True
                    else:
                        return "NO"

    return "YES"


def solution (arr):
    for i in range(9):
        ch1 = [0] * 10
        ch2 = [0] * 10
        for j in range(9):
            ch1[arr[i][j]] = 1
            ch2[arr[j][i]] = 1
        print(i,"행",ch1)
        print(i,"열",ch2)
        if sum(ch1) != 9 or sum(ch2) !=9:
            return "NO"

    for i in range(3):
        for j in range(3):
            ch3 = [0] * 10
            for k in range(3):
                for s in range(3):
                    ch3[arr[i * 3 + k][j * 3 + s]] = 1
            print(i,"그룹", ch3)
            if sum(ch3)!= 9:
                return "NO"
    return "YES"

sudoku = [list(map(int,input().split())) for _ in range(9)]

ans = sudokuChecker(sudoku)
# ans = solution(sudoku)

print(ans)
