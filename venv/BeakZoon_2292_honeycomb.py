# 벌집
# 1(1), 234567(2), 8~19(3), 20~ 37(4), 38~61(5), 62~91(6)  >> 6의 배수만큼 증가 6+ 12+ 18+ 24+ 30+

def honeycomb(num):
        d= 1
        start = 1
        if num == 1:
            return  1

        else:
            while True:
                #print(d,'::',start,'< num <=' ,start+(6*d))
                if num<= start+(6*d):
                    return d+1
                else :
                    start = start +(6*d)
                d += 1
                    # 2 + 6 = 8
                    # 8 + 12 = 20
                    # 20 + 18 = 38
                    # 38 + 24 = 62
                    # 62 + 30 = 92


num = int(input())
print(honeycomb(num))




