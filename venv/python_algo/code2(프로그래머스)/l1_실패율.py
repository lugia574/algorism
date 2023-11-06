# 하 시바 안될꺼 같애 하 시바 ㅈ같네 진짜
# 아 우울하다 시발 안될꺼 같으니까 존나 우울해 그냥 유튜브나 쳐 보면서 시각 죽이고 있는듯
# 이런 시바알ㅇㅂ
def solution(N, stages):
    answer = []
    arr = [0] * (N+2)
    rank = []
    player = len(stages)
    for i in stages:
        arr[i]+= 1

    for i in range(1, N+1):
        rate = arr[i]/ player if arr[i] > 0 else 0
        rank.append((rate, i))
        player -= arr[i]

    rank.sort(key=lambda x: (-x[0], x[1]))
    for _, idx in rank:
        answer.append(idx)
    return answer

if __name__ == "__main__":
    n = 5
    stages = [2, 1, 2, 6, 2, 4, 3, 3]
    res = [3,4,2,1,5]
    answer = solution(n, stages)
    print(res == answer, answer)

    n = 4
    stages = [4,4,4,4,4]
    res = [4,1,2,3]
    answer = solution(n, stages)
    print(res == answer, answer)