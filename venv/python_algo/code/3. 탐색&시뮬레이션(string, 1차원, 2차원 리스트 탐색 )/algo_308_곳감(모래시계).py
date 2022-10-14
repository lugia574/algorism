# 곳감(모래시계)
# N * N 격자판에 M 번의 이동 num1(행번호), num2(도는 방향), num3(이동칸수) 만큼 이동하고
# 그 격자판의 모래시계 모양에 해당하는 영역의 값을 구하시오.
#
# ▣ 입력설명
# 첫 줄에 자연수 N(3<=N<=20) 이 주어며, N은 홀수입니다.
# 두 번째 줄부터 N줄에 걸쳐 각 줄에 N개의 자연수가 주어진다.
# 이 자연수는 각 격자안에 있는 감의 개수이며, 각 격자안의 감의 개수는 100을 넘지 않는다.
# 그 다음 줄에 회전명령의 개수인 M(1<=M<=10)이 주어지고, 그 다음 줄부터 M개의 회전명령
# 정보가 M줄에 걸쳐 주어집니다.
# ▣ 출력설명
# 총 감의 개수를 출력합니다.
# ▣ 입력예제 1
# 5
# 10 13 10 12 15
# 12 39 30 23 11
# 11 25 50 53 15
# 19 27 29 37 27
# 19 13 30 13 19
# 3
# 2 0 3
# 5 1 2
# 3 1 4
# ▣ 출력예제 1
# 362
import copy

def rotaingNumPad (arr, move):
    for row , dir , m in move:
        for _ in range(m):
            if dir == 0:
               arr[row-1].append(arr[row-1].pop(0))
            else:
                arr[row - 1].insert(0, arr[row - 1].pop())


    return  arr

def hourglass(n,arr):
    res = 0
    s = 0
    e = n-1

    for i in range(n):
        for j in range(s, n):
            res += arr[i][j]
        if i < n//2:
            s += 1
            e -= 1
        else:
            s -= 1
            e += 1


    return res


N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]

tr = int(input())
move = [list(map(int, input().split())) for _ in range(tr)]

resultArr = rotaingNumPad(arr, move)


ans = hourglass(N,resultArr)

print(ans)
