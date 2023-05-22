# 이 문제는 다익스트라 or 플로이드와샬 방식으로 풀어야한데
# 이게 난 뭔소린지 이해가 안갔거든?
# 아니 각 x-y 까지의 최단거리를 구하는거긴한데
# 합승구간, 따로 떨어져서 각자 가는 구간 구별해야하니까 감이 안잡히는거야

# 근데 구별해야하니까 각각의 x-y 최단거리를 구하는게 맞음
# start - i 까지 구간을 합승 구간이라고 가정하면
# i - a, i - b 까지의 최단 거리가 바로 합승 이후 각자 가는 구간이 되는거지
# for 문을 돌려서 min((start - i) + (i - a) + (i - b), 기존의 res)으로 하면 최단거리를 찾을 수 있다~~
# 그렇기에 각 노드간 x - y 까지의 최단 거리를 구하는 방식인 다익스트라 or 플로이드와샬이 최고다~
# 그중에서 이 문제는 플로이드와샬 방식을 사용했다~
# https://www.youtube.com/watch?v=leXszEFCKWM

# 플로이드와샬
# https://www.youtube.com/watch?v=9574GHxCbKc&t=764s

# 난 이게 이해가 약간 안가는게
# 보면 항상 하나의 간선으로 타서 가는것만을 상정하듯 포문을 돌거든?
# 가령 1-3-2 로 갈게 아니라 1-3-4-2 로 거쳐서 가는게 더 빠르면 어쩔껀데
# 이게 이전에 3-2 의 최단거리를 이미 구해져 있음 모르는데 아닐꺼 아녀 이제 1- 2 최단 거리 찾는 포문이 돌고 있는데
# 3-4-2 로 가는 최단 거리를 알리가 없자나
# 잉 됐네 예제 만들어 하니까 딱 알아차리는데???

import math

# cost = [[0, 999, 5, math.inf],
#             [999, 0, 4, 2],
#             [5, 4, 0, 1],
#             [math.inf, 2, 1, 0]]

def floyd_warshallTest(n, cost):
    # k 는 경유지
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i == j:
                    cost[i][j] = 0
                else:
                    cost[i][j] = min(cost[i][k] + cost[k][j], cost[i][j])
        print("=====",k+1,"를 거쳐=====")
        for x in cost:
            print(x)

    return cost

def floyd_warshall(n, cost):
    # k 는 경유지
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if i == j:
                    cost[i][j] = 0
                else:
                    cost[i][j] = min(cost[i][k] + cost[k][j], cost[i][j])

    return cost

def solution(n, s, a, b, fares):
    answer = math.inf
    cost = [[math.inf] * (n + 1) for _ in range(n + 1)]

    for i, j, c in fares:
        cost[i][j] = c
        cost[j][i] = c
    cost = floyd_warshall(n, cost)
    
    # s-i 까지가 합승 구간 i-a, i-b 합승구간에서 각자 집까지의 거리
    for i in range(1, n + 1):
        answer = min(cost[s][i] + cost[i][a] + cost[i][b], answer)
    return answer

if __name__ == "__main__":
    n = 4
    cost = [[0, 999, 5, math.inf],
            [999, 0, 4, 2],
            [5, 4, 0, 1],
            [math.inf, 2, 1, 0]]
    cost = floyd_warshallTest(n, cost)
    print("====last====")
    for x in cost:
        print(x)
    # n = 6
    # s = 4
    # a = 6
    # b = 2
    # fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
    # res = 82
    #
    # ans = solution(n, s, a, b, fares)
    # print(res == ans)
    #
    # n = 7
    # s = 3
    # a = 4
    # b = 1
    # fares = [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]
    # res = 14
    #
    # ans = solution(n, s, a, b, fares)
    # print(res == ans)
    #
    # n = 6
    # s = 4
    # a = 5
    # b = 6
    # fares = [[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]
    # res = 18
    #
    # ans = solution(n, s, a, b, fares)
    # print(res == ans)