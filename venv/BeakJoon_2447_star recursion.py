# 문제
# 재귀적인 패턴으로 별을 찍어 보자. N이 3의 거듭제곱(3, 9, 27, ...)이라고 할 때, 크기 N의 패턴은 N×N 정사각형 모양이다.
#
# 크기 3의 패턴은 가운데에 공백이 있고, 가운데를 제외한 모든 칸에 별이 하나씩 있는 패턴이다.

# ***
# * *
# ***
import math


def star(row, col, num):
    global arr

    if (num == 1):
        arr[row][col] = "*";
        return

    s=int(num/3)
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1 :
                continue

            star(row + (s * i), col + (s * j), s)




num = int(input())
#num = 9 #(3^3) 3^n = 27

arr = [[' ' for col in range(num)]for row in range(num)]
star(0,0,num)

for i in range(len(arr)):
    for j in range(len(arr)):
        print(arr[i][i], end="")

    print()

