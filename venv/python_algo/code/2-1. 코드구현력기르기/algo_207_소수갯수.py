# 소수(에라토스테네스 체)
# 자연수 N이 입력되면 1부터 N까지의 소수의 개수를 출력하는 프로그램을 작성하세요.
# 만약 20이 입력되면 1부터 20까지의 소수는 2, 3, 5, 7, 11, 13, 17, 19로 총 8개입니다.
# 제한시간은 1초입니다.
# ▣ 입력설명
# 첫 줄에 자연수의 개수 N(2<=N<=200,000)이 주어집니다.
# ▣ 출력설명
# 첫 줄에 소수의 개수를 출력합니다.
# ▣ 입력예제 1
# 20
# ▣ 출력예제 1
# 8
import math


n = int(input())

def PrimeNumber (num):
    PNumberCnt = 1
    PNumberBoolean = True

    for i in range(3, num+1) :
        for j in range(2,  round(math.sqrt(i))+1 ):

            # print(i,"%",j,"값은 : ",i%j)
            if (i % j == 0) :
                PNumberBoolean = False
                break

        if PNumberBoolean == True:
            # print("😎 i 값: ", i)
            PNumberCnt += 1
        PNumberBoolean = True

    return PNumberCnt

# solution
def Sieve_of_Eratosthenes (num):
    ch = [0] * (num + 1)
    cnt = 0

    for i in range(2, num + 1):
        if ch[i] == 0:
            cnt += 1

            for j in range(i, num +1 , i):
                ch[j] == 1

    return cnt

ans = PrimeNumber(n)
print(ans)
