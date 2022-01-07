# 손익 분기점
# 매년 A 만큼 값이 나가고
# 만들때마다 한 대 당 B 만큼 값이 나감
# 노트북 한 대 가격이 C 라고 했을때
# 몇대를 팔아야 손익 분기점을 넘는가?


# A+ BX < CX
# X > A/(C-B)
def bep (ann,cost,sel):
    x = 0

    # 제조값이 판매값보다 높을경우
    if cost >= sel:
        x= -1

    # 아닌 경우
    else:
        if ann == 0:
            x = 1
        else:
            x = int(ann/(sel - cost)) + 1

    return x


ann, cost, sel =  map(int,input().split())
#print(ann,cnt,sel)
print(bep(ann,cost,sel))