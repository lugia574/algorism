# 문제
# 세 점이 주어졌을 때, 축에 평행한 직사각형을 만들기 위해서 필요한 네 번째 점을 찾는 프로그램을 작성하시오.
#
# 입력
# 세 점의 좌표가 한 줄에 하나씩 주어진다. 좌표는 1보다 크거나 같고, 1000보다 작거나 같은 정수이다.
#
# 출력
# 직사각형의 네 번째 점의 좌표를 출력한다.

def fourth(first, second , third):
    max_x = max(first[0], second[0], third[0])
    min_x = min(first[0], second[0], third[0])
    max_y = max(first[1], second[1], third[1])
    min_y = min(first[1], second[1], third[1])

    coordinate = [[min_x, min_y], [min_x, max_y],[max_x, min_y], [max_x, max_y]]
    if first in coordinate:
        coordinate.remove(first)
    if second in coordinate:
        coordinate.remove(second)
    if third in coordinate:
        coordinate.remove(third)

    return coordinate


first = list(map(int,input().split()))
second = list(map(int,input().split()))
third = list(map(int,input().split()))

ans = fourth(first, second , third)
for x, y in ans:
    print(x, y)

###################################################################################3

def fourth2 (x_list, y_list):
    ans_x = 0
    ans_y = 0
    for i in range(3):
        if x_list.count(x_list[i]) == 1:
            ans_x = x_list[i]
        if y_list.count(y_list[i]) == 1:
            ans_y = y_list[i]

    return ans_x, ans_y

x_list = []
y_list = []

for _ in range(3):
    x, y = map(int,input().split())
    x_list.append(x)
    y_list.append(y)

ans_x, ans_y = fourth2(x_list, y_list)
print(ans_x, ans_y)