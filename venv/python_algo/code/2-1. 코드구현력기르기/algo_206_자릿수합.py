# 자릿수의 합
# N개의 자연수가 입력되면 각 자연수의 자릿수의 합을 구하고, 그 합이 최대인 자연수를 출력
# 하는 프로그램을 작성하세요. 각 자연수의 자릿수의 합을 구하는 함수를 def digit_sum(x)를
# 꼭 작성해서 프로그래밍 하세요.
# ▣ 입력설명
# 첫 줄에 자연수의 개수 N(3<=N<=100)이 주어지고, 그 다음 줄에 N개의 자연수가 주어진다.
# 각 자연수의 크기는 10,000,000를 넘지 않는다.
# ▣ 출력설명
# 자릿수의 합이 최대인 자연수를 출력한다. 자릿수의 합이 같을 경우 입력순으로 먼저인 숫자
# 를 출력합니다.
# ▣ 입력예제 1
# 3
# 125 15232 97
# ▣ 출력예제 1
# 97
import sys
N = input()
numList = map(int, input().split())



def Py_digit_sum(numList):
    maxNum = 0
    ans = 0

    for num in numList:
        digit_num = list(map(int, list(str(num))))
        # print(digit_num, sum(digit_num))
        if maxNum < sum(digit_num):
            maxNum = sum(digit_num)
            ans = num

    return  ans

def sol_digit_sum(numList):
    maxNum = 0
    sum = 0
    ans = 0

    for num in numList:
        while num > 0:
            sum += num % 10
            num = num // 10
        if maxNum < sum:
            maxNum = sum
            ans = num
        sum = 0

    return  ans

print(Py_digit_sum(numList))
