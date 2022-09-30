# 뒤집은 소수
# N개의 자연수가 입력되면 각 자연수를 뒤집은 후 그 뒤집은 수가 소수이면 그 수를 출력하는
# 프로그램을 작성하세요. 예를 들어 32를 뒤집으면 23이고, 23은 소수이다. 그러면 23을 출력
# 한다. 단 910를 뒤집으면 19로 숫자화 해야 한다. 첫 자리부터의 연속된 0은 무시한다.
# 뒤집는 함수인 def reverse(x) 와 소수인지를 확인하는 함수 def isPrime(x)를 반드시 작성하
# 여 프로그래밍 한다.
# ▣ 입력설명
# 첫 줄에 자연수의 개수 N(3<=N<=100)이 주어지고, 그 다음 줄에 N개의 자연수가 주어진다.
# 각 자연수의 크기는 100,000를 넘지 않는다.
# ▣ 출력설명
# 첫 줄에 뒤집은 소수를 출력합니다. 출력순서는 입력된 순서대로 출력합니다.
# ▣ 입력예제 1
# 5
# 32 55 62 3700 250
# ▣ 출력예제 1
# 23 73
import math

T = int(input())
numList = list(map(int, input().split()))

def reverse(T, numList):
    reverseList = []
    for i in range(T):
        reverseNum = 0
        digit_num = list(map(int, list(str(numList[i]))))

        # print("나눈 숫자 리스트 : ",digit_num)

        for j in range(len(digit_num)-1, -1, -1):
            # print("j 값을 말해라:" , j)
            if j == 0 :
                reverseNum += digit_num[j]
            else:
                reverseNum += digit_num[j] * (10 ** j)

        # print("리버스된 숫자: ",reverseNum)
        reverseList.append(reverseNum)


    return reverseList

def isPrime(X):
    PrimeList = []
    PNumberBoolean = True

    for i in X:
        if i == 2:
            PrimeList.append(i)
            continue

        elif i == 1:
            continue

        for j in range(2 ,round(math.sqrt(i))+1):
            if (i % j == 0):
                PNumberBoolean = False
                break
        if PNumberBoolean == True:
            # print("😎 i 값: ", i)
            PrimeList.append(i)
        PNumberBoolean = True


    return PrimeList


numList = reverse(T, numList)
# print(numList)

PrimeList = isPrime(numList)

for i in PrimeList:
    print(i, end=" ")


#################### solution ##########################

def solutionReverse (num):
    res = 0
    while num> 0:
        t = num % 10
        res = res * 10 + t
        num = num // 10

    return res

def solutionIsPrime (num):

    if num == 1:
        return False

    for i in range(2, round(math.sqrt(num))+1):
        if num % i == 0:
            return False

    return True

n = int(input())
a = list(map(int, input().split()))

for x in a:
    tmp = solutionReverse(x)
    if solutionIsPrime(tmp):
        print(tmp, end=" ")

