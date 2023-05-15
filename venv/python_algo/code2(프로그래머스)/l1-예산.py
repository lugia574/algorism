# 부서별로 물품을 구매하는데 필요한 금액을 조사했습니다.
# 그러나 모든 부서의 물품을 구매해 줄 수는 없습니다.
# 그래서 최대한 많은 부서의 물품을 구매해 줄 수 있도록 하려고 합니다.

# 예를 들어 1,000원을 신청한 부서에는 정확히 1,000원을 지원해야 하며,
# 1,000원보다 적은 금액을 지원해 줄 수는 없습니다.
#
# 부서별로 신청한 금액이 들어있는 배열 d와
# 예산 budget이 매개변수로 주어질 때,
# 최대 몇 개의 부서에 물품을 지원할 수 있는지 return 하도록 solution 함수를 완성해주세요.

# 제한사항
# d는 부서별로 신청한 금액이 들어있는 배열이며, 길이(전체 부서의 개수)는 1 이상 100 이하입니다.
# d의 각 원소는 부서별로 신청한 금액을 나타내며, 부서별 신청 금액은 1 이상 100,000 이하의 자연수입니다.
# budget은 예산을 나타내며, 1 이상 10,000,000 이하의 자연수입니다.

# d	            budget	result
# [1,3,2,5,4]	9	    3
# [2,2,3,3]	    10	    4


# 이것도 조합/ 다만 이건 예산을 넘지 않는 선에서 계속 조합수를 늘려야함
# DFM 로 하니까 타임아웃뜸 점화식으로 해봐야하나? 시이ㅣ이이발


from collections import deque

def DFM(l, cost, budget, arr):
    global r
    global MaxCost
    global lenght

    if cost > budget:
        return
    else:
        if MaxCost < cost:
            r = l
            MaxCost = cost
        for i in range(l, lenght):
            DFM(l+1, cost + arr[i], budget, arr)


def solution(d, budget):
    d.sort()
    answer = 0
    lenght = len(d)

    for i in range(lenght):
        if d[i] > budget:
            break

        budget -= d[i]
        answer += 1

    return answer

if __name__ == "__main__":
    d = [1,3,2,5,4]
    budget = 9
    result = 3

    r = 0
    MaxCost = 0
    lenght = 0


    d2 = [2,2,3,3]
    budget2 = 10
    result2 = 4

    #ans = solution(d, budget)
    ans2 = solution(d2, budget2)

    #print(ans)
    print(ans2)

    #print("정답입니다." if ans == result else "틀렸습니다 모지리 새끼야")
    print("정답입니다." if ans2 == result2 else "틀렸습니다 모지리 새끼야")