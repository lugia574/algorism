# 터렛
import math


def turret(x_1, y_1, r_1, x_2, y_2, r_2):
    ans = 0
    d = math.sqrt(float((x_1 - x_2) ** 2 + (y_1 - y_2) ** 2))

    # 점이 무한대 일때
    if x_1 == x_2 and y_1 == y_2 and r_1 == r_2:
        ans = -1
        return ans


    elif d == 0:
        return ans


    # 점이 두 점일때
    #  r_1 - r_2 < d < r_1 + r_2
    if abs(r_1 - r_2) < d and d < abs(r_1 + r_2):
        ans = 2

    # 점이 하나 일때 _ 1
    elif d == (r_1 + r_2):
        ans = 1


    # 점이 하나 일때 _ 2
    elif d == abs(r_1 - r_2):
        ans = 1



    return ans

Tr = int(input())
for _ in range(Tr):

    x_1,y_1,r_1,x_2,y_2,r_2 = map(int,input().split())

    print(turret(x_1, y_1, r_1, x_2, y_2, r_2))