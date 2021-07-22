#Factorization
# 정수 N이 주어졌을 때, 소인수분해하는 프로그램을 작성하시오.
#
# 첫째 줄에 정수 N (1 ≤ N ≤ 10,000,000)이 주어진다.
import math


def Factorization(num):
    small_number_list=[]
    #sqrt = int(math.sqrt(num))+1 #왜인지 몰겟는데 시간초과 뜸
    while num != 1:
        for i in range(2,num+1):
            if num % i == 0:
                small_number_list.append(i)
                num = int(num/i)
                break
    return small_number_list

num = int(input())
small_number_list=Factorization(num)
for small_number in small_number_list:
    print(small_number)