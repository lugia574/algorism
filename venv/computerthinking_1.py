# 수열이 주어지고 어떤 수 X 를 고른 경우 X+1 , X-1 값을 가진 숫자 모두 사라진다
# 수열에는 같은 값이 여러개 복수로 주어질수 있다.
# 이때 얻을 수 있는 가장 높은 점수를 구하시오
import copy

def sol (arr):
    size =len(arr)
    sum_arr = 0

    for i in range(size):
        sample = copy.deepcopy(arr)
        ans_arr =  []

        for j in range(size):

            if arr[j] in sample:
                standard_num = arr[j]
                ans_arr.append(standard_num)

                for _ in range(size):
                    if standard_num+1 in sample:
                        sample.remove(standard_num+1)
                    if standard_num -1 in sample:
                        sample.remove(standard_num -1)
                sample.remove(standard_num)

        if sum(ans_arr) > sum_arr:
            sum_arr= sum(ans_arr)

    return sum_arr

arr = list(map(int,input().split()))

ans = sol(arr)

print(ans)