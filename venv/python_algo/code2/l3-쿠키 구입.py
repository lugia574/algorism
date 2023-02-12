# 과자를 바구니 단위로 파는 가게가 있습니다.
# 이 가게는 1번부터 N번까지 차례로 번호가 붙은 바구니 N개가 일렬로 나열해 놨습니다.

# 두 아들에게 줄 과자를 사려합니다.
# 첫째 아들에게는 l번 바구니부터 m번 바구니까지, 둘째 아들에게는 m+1번 바구니부터 r번 바구니까지를 주려합니다
# 단, 두 아들이 받을 과자 수는 같아야 합니다(1 <= l <= m, m+1 <= r <= N).
# 즉, A[i] 를 i번 바구니에 들어있는 과자 수라고 했을 때, A[l]+..+A[m] = A[m+1]+..+A[r] 를 만족해야 합니다.

# 각 바구니 안에 들은 과자 수가 차례로 들은 배열 cookie가 주어질 때,
# 조건에 맞게 과자를 살 경우 한 명의 아들에게 줄 수 있는 가장 많은 과자 수를 return 하는 solution 함수를 완성해주세요.

# 제한사항
# cookie의 길이는 1 이상 2,000 이하입니다.
# cookie의 각각의 원소는 1 이상 500 이하인 자연수입니다.

def solution(cookie):
    n = len(cookie)
    answer = 0
    for i in range(n-1):
        leftLoc = i
        rightLoc = i + 1
        leftSum = cookie[leftLoc]
        rightSum = cookie[rightLoc]

        while leftLoc >= 0 and rightLoc < n:
            if leftSum == rightSum:
                answer = max(leftSum, answer)


            if leftSum <= rightSum and leftLoc > 0:
                leftLoc -= 1
                leftSum += cookie[leftLoc]


            elif leftSum >= rightSum and rightLoc < n-1:
                rightLoc += 1
                rightSum += cookie[rightLoc]

            else:
                break



    return answer

if __name__ == "__main__":
    cookie = [1,1,2,3]
    result = 3

    res = solution(cookie)
    print(res)
    print("True" if res == result else "False")

    cookie2 = [1,2,4,5]
    result2 = 0

    res2 = solution(cookie2)
    print(res2)
    print("True" if res2 == result2 else "False")

    cookie3 = [0, 3, 3, 3, 3, 3, 5, 5, 5, 6]
    result3 = 15

    res3 = solution(cookie3)
    print(res3)
    print("True" if res3 == result3 else "False")