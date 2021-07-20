# 자연수 M과 N이 주어질 때 M이상 N이하의 자연수 중 소수인 것을 모두 골라 이들 소수의 합과 최솟값을 찾는 프로그램을 작성하시오.
#
# 예를 들어 M=60, N=100인 경우 60이상 100이하의 자연수 중
# 소수는 61, 67, 71, 73, 79, 83, 89, 97 총 8개가 있으므로, 이들 소수의 합은 620이고, 최솟값은 61이 된다.

# M이상 N이하의 자연수 중 소수인 것을 모두 찾아 첫째 줄에 그 합을, 둘째 줄에 그 중 최솟값을 출력한다.
#
# 단, M이상 N이하의 자연수 중 소수가 없을 경우는 첫째 줄에 -1을 출력한다.
import math


def PrimeNumber (num):
    true = 1
    standard = int(math.sqrt(num))
    if num != 1:
        for i in range(2, standard + 1):
            if num % i ==0:
                true = 0
    else:
        true = 0

    if true == 1:
        return num
    else:
        num = 0
        return num


def PrimeNumberSerach (M, N):
    PrimeNumSum = 0
    PrimeNumMin = N
    for i in range(M,N+1):
        prnum = PrimeNumber(i)
        PrimeNumSum += prnum
        if prnum != 0:
            if PrimeNumMin > prnum:
                PrimeNumMin = prnum

    return PrimeNumSum, PrimeNumMin

M = int(input())
N = int(input())


sum, min = PrimeNumberSerach(M,N)
if sum != 0:
    print(sum)
    print(min)
else:
    print(-1)



