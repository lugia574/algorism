# 이건 좀 신기하게 좌표간의 거리로 장난질
# 이제까지는 다 주어진 것들에 간단히 sort 하고 유니온 합집합 했음
# 되는 문제들이였지만
# 이 문제는 직접 데이터 가공을 해서 해야한다는 문제임
# 딱 프로그래머스에서 좋아할만한 형태의 문제 여기서 하나 요소 하나 더 들어가면 딱임
# https://jjangsungwon.tistory.com/92

# 보니까 요소가 하나 더 있음 ㅋㅋ 이제 보니 이거 문제 난도 플레5인데 딱 프로그래머스 취향이네 ㅋ
# https://developmentdiary.tistory.com/450
# 행성 갯수가 존나 많아서 이걸 다 계산하고 있으면 시초가 날꺼라는거야
# 즉 시초를 피하고 싶으면 전부 다 돌아보지 말라는거야
# 근데 솔직히 아직 잘 이해가 안감 ㅋ

# https://baejinsoo.github.io/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%20%EB%AC%B8%EC%A0%9C%ED%92%80%EA%B8%B0/BOJ_2887/
# 이 방식대로 하면
import sys

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

if __nam__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    parent = [i for i in range(n + 1)]

    x_list = []
    y_list = []
    z_list = []
    for i in range(1, n + 1):
        x, y, z = map(int,input().split())
        x_list.append((x, i))
        y_list.append((y, i))
        z_list.append((z, i))

    x_list.sort()
    y_list.sort()
    z_list.sort()

    count_list = []
    for i in range(1, n):
        count_list.append((abs(x_list[i][0] - x_list[i-1][0]), x_list[i][1], x_list[i-1][1]))
        count_list.append((abs(y_list[i][0] - y_list[i-1][0]), y_list[i][1], y_list[i-1][1]))
        count_list.append((abs(z_list[i][0] - z_list[i-1][0]), z_list[i][1], z_list[i-1][1]))
    count_list.sort()

    res = 0
    answer = 0
    for co in count_list:
        cost, a, b = co
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            answer += cost
            res += 1
        if res == n:
            break

    print(answer)