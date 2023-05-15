# 지형 편집 기능을 이용하여 플레이어가 직접 게임 속 지형을 수정할 수 있습니다.
# 플레이어는 N x N 크기의 지역에 자신만의 별장을 만들고 싶어졌습니다.
# 이를 위해서는 울퉁불퉁한 지형의 모든 칸의 높이가 같아지도록 만들어야 합니다.
# 이때, 블록 한 개를 추가하려면 P의 비용이, 제거하려면 Q의 비용이 들게 됩니다.
# 모든 칸에 쌓여있는 블록의 높이가 같아지도록 하는 데 필요한 비용의 최솟값을 return 하도록 solution 함수를 완성해 주세요.


# 제한사항
# land는 N x N 크기의 2차원 배열이며, N의 범위는 1 ≤ N ≤ 300입니다.
# land의 각 원소는 각 칸에 놓여 있는 블록의 수를 나타내며, 0 이상 10억 이하의 정수입니다.
# 각 칸에 블록 하나를 추가하는 데는 P, 제거하는 데는 Q의 비용이 들며, P, Q의 범위는 1 ≤ P, Q ≤ 100인 자연수입니다.

# 평탄화 작업임
# 단순히 튀어 나와있는걸 싹다 조지고 채우고 해서 값이 몇이냐를 return 하는게 아닌
# 최솟값을 return 하는거니까 음음


def solution_sol(land, P, Q):
    lst = []
    for i in land:
        lst += i
    lst = sorted(lst)

    n = len(lst)
    answer = sum(lst) * Q
    cost = (sum(lst) - lst[0] * n) * Q
    answer = min(answer, cost)

    for i in range(1, n):
        if lst[i] != lst[i - 1]:
            cost += (P * i * (lst[i] - lst[i - 1])) - (Q * (n - i) * (lst[i] - lst[i - 1]))

            answer = min(answer, cost)

    return answer

def solution(land, P, Q):
    arr = []
    for e in land:
        arr += e
    arr.sort()
    n = len(arr)
    prev = -1
    cost = (sum(arr) - arr[0] * n) * Q
    res = 1000000001

    for i in range(1,n):
        if arr[i] == prev:
            continue

        prev = arr[i]

        pAppendCost = i * P
        qBackCost = (n-i) * Q
        cost += pAppendCost - qBackCost

        if res < cost:
            break
        res = min(res, cost)

    return res

if __name__ =="__main__":
    land = [[1, 2], [2, 3]]
    p = 3
    q = 2
    result = 5

    res = solution(land, p, q)
    print(res)
    print("True" if res == result else "False")

    land = [[4, 4, 3], [3, 2, 2], [ 2, 1, 0 ]]
    p = 5
    q = 3
    result = 33

    res = solution(land, p, q)
    print(res)
    print("True" if res == result else "False")
