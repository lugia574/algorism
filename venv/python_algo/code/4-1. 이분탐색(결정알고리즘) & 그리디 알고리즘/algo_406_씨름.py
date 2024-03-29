# 씨름 선수(그리디)
# 현수는 씨름 감독입니다. 현수는 씨름 선수를 선발공고를 냈고, N명의 지원자가 지원을 했습
# 니다. 현수는 각 지원자의 키와 몸무게 정보를 알고 있습니다.
# 현수는 씨름 선수 선발 원칙을 다음과 같이 정했습니다.
# “다른 모든 지원자와 일대일 비교하여 키와 몸무게 중 적어도 하나는 크거나, 무거운 지원자
# 만 뽑기로 했습니다.”
# 만약 A라는 지원자보다 키도 크고 몸무게도 무거운 지원자가 존재한다면 A지원자는 탈락입니
# 다.
# ▣ 입력설명
# 첫째 줄에 지원자의 수 N(5<=N<=50)이 주어집니다.
# 두 번째 줄부터 N명의 키와 몸무게 정보가 차례로 주어집니다. 각 선수의 키와 몸무게는 모두
# 다릅니다.
# ▣ 출력설명
# 첫째 줄에 씨름 선수로 뽑히는 최대 인원을 출력하세요.
# ▣ 입력예제 1
# 5
# 172 67
# 183 65
# 180 70
# 170 72
# 181 60
# ▣ 출력예제 1
# 3
# 출력설명
# (183, 65), (180, 70), (170, 72)가 선발됩니다. (181, 60)은 (183, 65) 때문에 탈락하고, (172, 67)은
# (180, 70) 때문에 탈락합니다.

def selectPlayer(n, arr):
    cnt = n
    for w, h in arr:
        for w2, h2 in arr:
            if w < w2 and h < h2:
                cnt -= 1
                break
    return cnt

# 키를 높은 순서대로 싹 정렬을 해
# 그럼 가장 키가 큰 사람은 무조건 확정이야
# 이제 2번째 키큰 사람은 1번째 사람보다 몸무게만 크면 채용이야
# 마찬가지로 3번째도 2번째 보다 몸무게만 크면 됨
# 즉 키 순으로 내림차순으로 정렬하고 몸무게만 비교하면 된다~ 반복문 하나만 써도 된다~~
def solution (arr):
    arr.sort(reverse = True)

    largest = 0
    cnt = 0

    for _, h in arr:
        if h> largest:
            largest = h
            cnt += 1

    return cnt

def dataInput():
    N = int(input())
    playerList = []
    for _ in range(N):
        playerList.append(list(map(int,input().split())))
    return N, playerList

N,playerList = dataInput()
playerList.sort()
ans = selectPlayer(N,playerList)
print(ans)

ans2 = solution(playerList)
print(ans2)

