# https://velog.io/@qweadzs/프로그래머스-다단계-칫솔-판매Python 참고삼아 함 보자
def divide(m, a, rel, money):
    while True:
        if a == "center":
            money[a] += m
            return
        # 이익금 줘야하는 놈
        b = rel[a]
        tax = m // 10
        money[a] += m - tax

        if tax == 0:
            break
        m = tax
        a = b

def solution(enroll, referral, seller, amount):
    answer = []
    rel = {}
    money = {"center": 0}
    length = len(enroll)
    # 딕셔너리에 박기

    for i in range(length):
        if referral[i] == "-":
            rel[enroll[i]] = "center"
        else:
            rel[enroll[i]] = referral[i]
        money[enroll[i]] = 0


    #확인
    # print(rel)
    # print(money)

    # 셀러 값
    sellLength = len(seller)
    for i in range(sellLength):
        divide(amount[i] * 100, seller[i], rel, money)


    # 값 넣기
    # print(money)
    for k in money.keys():
        if k == "center":
            continue
        answer.append(money[k])

    return answer

if __name__ == "__main__":
    enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
    referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
    seller = ["young", "john", "tod", "emily", "mary"]
    amount = [12, 4, 2, 5, 10]
    res = [360, 958, 108, 0, 450, 18, 180, 1080]

    ans = solution(enroll, referral, seller, amount)
    print(ans)
    print(res == ans)

    enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
    referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
    seller = ["sam", "emily", "jaimie", "edward"]
    amount = [2, 3, 5, 4]
    res = [0, 110, 378, 180, 270, 450, 0, 0]

    ans = solution(enroll, referral, seller, amount)
    print(ans)
    print(ans == res)