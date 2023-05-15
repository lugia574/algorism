# N개의 마을
# 마을은 양방향으로 통행할 수 있는 도로로 연결되어 있는데,
# 서로 다른 마을 간에 이동할 때는 이 도로를 지나야 합니다.
# 도로를 지날 때 걸리는 시간은 도로별로 다름
# 마을의 개수 N, 각 마을을 연결하는 도로의 정보 road, 음식 배달이 가능한 시간 K가 매개변수로 주어질 때,
# 음식 주문을 받을 수 있는 마을의 개수를 return 하도록 solution 함수를 완성해주세요.

# 제한사항
# 마을의 개수 N은 1 이상 50 이하의 자연수입니다.
# road의 길이(도로 정보의 개수)는 1 이상 2,000 이하입니다.
# road의 각 원소는 마을을 연결하고 있는 각 도로의 정보를 나타냅니다.
# road는 길이가 3인 배열이며, 순서대로 (a, b, c)를 나타냅니다.
# a, b(1 ≤ a, b ≤ N, a != b)는 도로가 연결하는 두 마을의 번호이며, c(1 ≤ c ≤ 10,000, c는 자연수)는 도로를 지나는데 걸리는 시간입니다.
# 두 마을 a, b를 연결하는 도로는 여러 개가 있을 수 있습니다.
# 한 도로의 정보가 여러 번 중복해서 주어지지 않습니다.
# K는 음식 배달이 가능한 시간을 나타내며, 1 이상 500,000 이하입니다.
# 임의의 두 마을간에 항상 이동 가능한 경로가 존재합니다.
# 1번 마을에 있는 음식점이 K 이하의 시간에 배달이 가능한 마을의 개수를 return 하면 됩니다.

# https://blog.naver.com/PostView.naver?blogId=ndb796&logNo=221234424646&redirect=Dlog&widgetTypeCall=true&directAccess=false



# float('inf') 양의 무한대 표현이래
from collections import deque


def solution(N, road, K):
    answer = 0
    dis = [500001] * (N + 1)
    dis[1] = 0
    loc = [[] for _ in range(N + 1)]
    for r in road:
        loc[r[0]].append([r[2], r[1]])
        loc[r[1]].append([r[2], r[0]])
    for i in loc:
        print(i)
        print()

    dq = deque()
    dq.append([0, 1])

    while dq:
        cost, node = dq.popleft()
        for c, end in loc[node]:
            if cost + c < dis[end]:
                dis[end] = cost + c
                dq.append([cost + c, end])

    for x in dis:
        if x <= K :
            answer += 1


    return answer

if __name__ == "__main__":
    # road 의 0번째는 시작점 1번째는 도착점 2번째는 소요 시간
    n = 5
    road = 	[[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]
    k = 3
    result = 4

    n2 = 6
    road2 = [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]]
    k2 = 4
    result2 = 4

    res = solution(n,road, k)
    print(res)
    print("정답입니다." if res == result else "틀렸습니다 모지리새끼야")

    res2 = solution(n2, road2, k2)
    print(res2)
    print("정답입니다." if res2 == result2 else "틀렸습니다 모지리새끼야")