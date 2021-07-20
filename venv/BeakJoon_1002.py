import math
# 터렛


T = int(input())

for i in range(T):

    x_1,y_1,r_1,x_2,y_2,r_2 = map(int,input().split())

    def sol (x_1, y_1, r_1, x_2, y_2, r_2):
        ans = 0
        d = math.sqrt(float((x_1 - x_2) ** 2 + (y_1 - y_2) ** 2))
        if d == 0:
            return  ans
        # 점이 두 점일때
        #  r_1 - r_2 < d < r_1 + r_2
        if abs(r_1-r_2) < d and d < abs(r_1 + r_2):
            ans = 2

        # 점이 하나 일때 _ 1
        elif d == (r_1 + r_2):
            ans= 1


        # 점이 하나 일때 _ 2
        elif d == abs(r_1 - r_2) :
            ans = 1


        return ans

    print(sol(x_1, y_1, r_1, x_2, y_2, r_2))