# 코딩 테스트 공부
# 코딩 테스트 문제를 풀기 위해서는 알고리즘에 대한 지식과 코드를 구현하는 능력이 필요합니다.
# 알고리즘에 대한 지식은 알고력, 코드를 구현하는 능력은 코딩력이라고 표현합니다. 알고력과 코딩력은 0 이상의 정수로 표현됩니다.
# 문제를 풀기 위해서는 문제가 요구하는 일정 이상의 알고력과 코딩력이 필요합니다.
#
# 예를 들어, 당신의 현재 알고력이 15, 코딩력이 10이라고 가정해보겠습니다.
#
# A라는 문제가 알고력 10, 코딩력 10을 요구한다면 A 문제를 풀 수 있습니다.
# B라는 문제가 알고력 10, 코딩력 20을 요구한다면 코딩력이 부족하기 때문에 B 문제를 풀 수 없습니다.
#
# 풀 수 없는 문제를 해결하기 위해서는 알고력과 코딩력을 높여야 합니다. 알고력과 코딩력을 높이기 위한 다음과 같은 방법들이 있습니다.
#
# 알고력을 높이기 위해 알고리즘 공부를 합니다. 알고력 1을 높이기 위해서 1의 시간이 필요합니다.
# 코딩력을 높이기 위해 코딩 공부를 합니다. 코딩력 1을 높이기 위해서 1의 시간이 필요합니다.
# 현재 풀 수 있는 문제 중 하나를 풀어 알고력과 코딩력을 높입니다. 각 문제마다 문제를 풀면 올라가는 알고력과 코딩력이 정해져 있습니다.
# 문제를 하나 푸는 데는 문제가 요구하는 시간이 필요하며 같은 문제를 여러 번 푸는 것이 가능합니다.
# 당신은 주어진 모든 문제들을 풀 수 있는 알고력과 코딩력을 얻는 최단시간을 구하려 합니다.


# 1 ≤ problems의 길이 ≤ 100
# problems의 원소는 [alp_req, cop_req, alp_rwd, cop_rwd, cost]의 형태로 이루어져 있습니다.
# alp_req는 문제를 푸는데 필요한 알고력입니다.
# 0 ≤ alp_req ≤ 150
# cop_req는 문제를 푸는데 필요한 코딩력입니다.
# 0 ≤ cop_req ≤ 150
# alp_rwd는 문제를 풀었을 때 증가하는 알고력입니다.
# 0 ≤ alp_rwd ≤ 30
# cop_rwd는 문제를 풀었을 때 증가하는 코딩력입니다.
# 0 ≤ cop_rwd ≤ 30
# cost는 문제를 푸는데 드는 시간입니다.
# 1 ≤ cost ≤ 100


def solution(alp, cop, problems):
    answer = 0
    problems.sort(key=lambda x: (x[0] + x[1]))
    print(problems)
    check = [0] * len(problems)
    completedCnt = len(problems)
    cnt = 0
    while cnt < completedCnt:
        for i in range(cnt,len(problems)):
            al, co, getAl, getCo, cost = problems[i]
            if alp >= al and cop >= co:
                alp += getAl
                cop += getCo
                answer += cost
                cnt += 1

            else:

                alpPlus = al - alp if alp < al else 0
                copPlus = co -cop if cop < co else 0
                answer += alpPlus + copPlus
                alp += alpPlus
                cop += copPlus

    return answer

if __name__ == "__main__":
    # alp 알고력
    # cop 코딩력

    # alp = 10
    # cop = 10
    # problems = [[10,15,2,1,2],[20,20,3,3,4]]
    # ans = 15

    alp = 0
    cop = 0
    problems = [[0,0,2,1,2],[4,5,3,1,2],[4,11,4,0,2],[10,4,0,4,2]]
    ans = 13


    answer = solution(alp, cop, problems)
    print("맞았습니다." if ans == answer else "틀렸습니다. 쓰레기새끼야")