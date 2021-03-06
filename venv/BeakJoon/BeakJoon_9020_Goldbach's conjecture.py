# 골드바흐의 추측
# 문제
# 1보다 큰 자연수 중에서  1과 자기 자신을 제외한 약수가 없는 자연수를 소수라고 한다. 예를 들어, 5는 1과 5를 제외한 약수가 없기 때문에 소수이다.
# 하지만, 6은 6 = 2 × 3 이기 때문에 소수가 아니다.
# 골드바흐의 추측은 유명한 정수론의 미해결 문제로, 2보다 큰 모든 짝수는 두 소수의 합으로 나타낼 수 있다는 것이다. 이러한 수를 골드바흐 수라고 한다.
# 또, 짝수를 두 소수의 합으로 나타내는 표현을 그 수의 골드바흐 파티션이라고 한다.
# 예를 들면, 4 = 2 + 2, 6 = 3 + 3, 8 = 3 + 5, 10 = 5 + 5, 12 = 5 + 7, 14 = 3 + 11, 14 = 7 + 7이다.
# 10000보다 작거나 같은 모든 짝수 n에 대한 골드바흐 파티션은 존재한다.
# 2보다 큰 짝수 n이 주어졌을 때, n의 골드바흐 파티션을 출력하는 프로그램을 작성하시오.
# 만약 가능한 n의 골드바흐 파티션이 여러 가지인 경우에는 두 소수의 차이가 가장 작은 것을 출력한다.
#
# 입력
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고 짝수 n이 주어진다.
#
# 출력
# 각 테스트 케이스에 대해서 주어진 n의 골드바흐 파티션을 출력한다. 출력하는 소수는 작은 것부터 먼저 출력하며, 공백으로 구분한다.
#
# 제한
# 4 ≤ n ≤ 10,000
import math


def Goldbach2(num):
    Gold_nums = []
    Prime_number_list = [True] *(num+1)
    sqrt = int(math.sqrt(num))

    for i in range(2, sqrt+1):
        if Prime_number_list[i] == True:
            for j in range(2*i, num+1, i):
                Prime_number_list[j] = False

    testnum = int(num/2)
    testnum2 = int(num/2)

    for _ in range(int(num/2)):
        if Prime_number_list[testnum] == True and Prime_number_list[testnum2] == True :
            Gold_nums.append(testnum)
            Gold_nums.append(testnum2)
            break
        else:
            testnum -= 1
            testnum2 += 1


    return Gold_nums

Tr = int(input())
for _ in range(Tr):
    num = int(input())
    Gold_nums = Goldbach2(num)
    for i in Gold_nums:
        print(i, end=" ")
    print()











# 이대로 했는데 시초 남

# def Goldbach(num):
#     Gold_nums = []
#     Prime_number_list = [True] *(num+1)
#     sqrt = int(math.sqrt(num))
#
#     for i in range(2, sqrt+1):
#         if Prime_number_list[i] == True:
#             for j in range(2*i, num+1, i):
#                 Prime_number_list[j] = False
#
#     for i in range(2,num):
#         if i > 1 and Prime_number_list[i] == True:
#             for j in range(i,num):
#                 if Prime_number_list[j] == True and num == i + j:
#                     if Gold_nums:
#                         if Gold_nums[1] - Gold_nums[0] > j - i:
#                             Gold_nums[0] = i
#                             Gold_nums[1] = j
#                     else:
#                         Gold_nums.append(i)
#                         Gold_nums.append(j)
#
#     return Gold_nums