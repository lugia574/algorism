# 회장뽑기(플로이드-워샬 응용)
# 회장을 선출하려고 한다.
# 각 회원은 다른 회원들과 가까운 정도에 따라 점수를 받게 된다.
# 예를 들어 어느 회원이 다른 모든 회원과 친구이면, 이 회원의 점수는 1점이다. 어느 회원의
# 점수가 2점이면, 다른 모든 회원이 친구이거나, 친구의 친구임을 말한다. 또한, 어느 회원의
# 점수가 3점이면, 다른 모든 회원이 친구이거나, 친구의 친구이거나, 친국의 친구의 친구임을
# 말한다.4점, 5점등은 같은 방법으로 정해진다.
# 각 회원의 점수를 정할 때 주의할 점은 어떤 두 회원이 친구 사이이면서 동시에 친구의 친구
# 사이이면, 이 두 사람은 친구사이라고 본다. 회장은 회원들 중에서 점수가 가장 작은 사람이
# 된다.
# 회장의 점수와 회장이 될 수 있는 모든 사람을 찾는 프로그램을 작성하시오.
# ▣ 입력설명
# 입력의 첫째 줄에는 회원의 수가 있다.
# 단, 회원의 수는 50명을 넘지 않는다. 둘째 줄 이후로는 한 줄에 두 개의 회원번호가 있는데,
# 이것은 두 회원이 서로 친구임을 나타낸다. 회원번호는 1부터 회원의 수만큼 번호가 붙어있다.
# 마지막 줄에는 -1이 두 개 들어있다
# ▣ 출력설명
# 첫째 줄은 회장 후보의 점수와 회장후보 수를 출력하고 두 번째 줄은 회장 후보를 모두 출력
# 한다.
# ▣ 입력예제 1
# 5
# 1 2
# 2 3
# 3 4
# 4 5
# 2 4
# 5 3
# -1 -1
# ▣ 출력예제 1
# 2 3
# 2 3 4

if __name__ =="__main__":
    n = int(input())
    dis = [[100] * (n+1) for _ in range(n+1)]

    check = [0] * (n+1)
    minV = 100
    cnt = 0
    ans = []

    # 값 박기
    for i in range(1, n+1):
        dis[i][i] = 0
    while True:
        x, y = map(int,input().split())
        if x == -1 and y == -1:
            break
        dis[x][y] = 1
        dis[y][x] = 1
    # 플로이 워샬 박기 ㄱㄱ
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])

    for i in range(1, n+1):
        for j in range(1, n+1):
            if dis[i][j] == 100:
                dis[i][j] = 0
    # print()
    # for i in range(1, n+1):
    #     for j in range(1, n+1):
    #         print(dis[i][j], end=" ")
    #     print()

    # 작은 값 찾기
    for i in range(1, n+1):
        for j in range(1, n+1):
            check[i] = max(check[i], dis[i][j])
        minV = min(minV, check[i])

    # 해당 정답 찾기
    for i in range(1, n+1):
        if minV == check[i]:
            ans.append(i)

    print(minV, len(ans))
    for i in ans:
        print(i, end=" ")
