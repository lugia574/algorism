# 격자판 회문수
# 1부터 9까지의 자연수로 채워진 7*7 격자판이 주어지면 격자판 위에서 가로방향 또는
# 세로방향으로 길이 5자리 회문수가 몇 개 있는지 구하는 프로그램을 작성하세요.
# 회문수란 121과 같이 앞에서부터 읽으나 뒤에서부터 읽으나 같은 수를 말합니다.
#
# ▣ 입력설명
# 1부터 9까지의 자연수로 채워진 7*7격자판이 주어집니다.
# ▣ 출력설명
# 5자리 회문수의 개수를 출력합니다.
# ▣ 입력예제 1
# 2 4 1 5 3 2 6
# 3 5 1 8 7 1 7
# 8 3 2 7 1 3 8
# 6 1 2 3 2 1 1
# 1 3 1 3 5 3 2
# 1 1 2 5 6 5 2
# 1 2 2 2 2 1 5
# ▣ 출력예제 1
# 3

def palindromeCounter (n,arr):
    cnt = 0
    palindLen = 5

    for i in range(n):
        for j in range(n-palindLen+1):
            rowPalCnt = 0
            columnPalCnt = 0

            for k in range(palindLen//2):
                 if arr[i][j+k] == arr[i][palindLen-1 +j-k]:
                     rowPalCnt += 1

                 if arr[j+k][i] == arr[palindLen-1 + j - k ][i]:
                     columnPalCnt += 1


            if rowPalCnt == 2:
                cnt += 1
            if columnPalCnt == 2:
                cnt += 1

    return cnt

def solution (n,arr):
    cnt = 0

    for i in range(3):
        for j in range(7):
            tmp = arr[j][i:i+5]
            if tmp == tmp[::-1]:
                cnt += 1
            for k in range(2):
                if arr[i+k][j] != arr[i+5-k-1][j]:
                    break
            else:
                cnt+= 1
    return  cnt

N = 7

num_list = [list(map(int, input().split())) for _ in range(N)]


cnt = palindromeCounter(N, num_list)
print(cnt)