# 낮에 A 만큼 올라 가고
# 밤에 B 만큼 미끄러짐
# 높이는 V
# 정상 도착하면 미끄러지지 않음

# (A-B)X >= V
# X >= V/ (A-B)
# 근데 정상 도착 염두
# X = (V-B)/(A-B)
import math


def Snail (A, B , V):
    ans = 0
    Snail_V = (A-B)
    if V <= Snail_V:
        pass
    else :
        ans = math.ceil((V-B)/Snail_V)

    return ans


A, B, V = map(int,input().split())
print(Snail(A, B, V))