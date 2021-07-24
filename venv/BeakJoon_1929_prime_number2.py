# M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.
#
# 첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000) M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.
import math

#
def Prime_number(M, N):
    Prime_number_list = list(range(M,N+1))
    sqrt = int(math.sqrt(N))
    for i in range(2, sqrt+1):
        for j in Prime_number_list:
            if j != i and j%i ==0:
                    Prime_number_list.remove(j)


    return Prime_number_list

M, N = map(int,input().split())
# Prime_number_list = Prime_number(M,N)
#
# for i in Prime_number_list:
#     print(i)

def Prime_number2(M, N):
    Prime_number_list = [True] * (N+1)
    sqrt = int(math.sqrt(N))
    for i in range(2,sqrt+1):
        if Prime_number_list[i] == True:
            for j in range(2*i, N+1, i):
                Prime_number_list[j] = False

    return Prime_number_list

# M, N = map(int,input().split())
Prime_number_list=Prime_number2(M,N)

for i in range(M, N + 1):
    if i > 1 and Prime_number_list[i] == True:
        print(i)