# 카드 역배치(정올 기출)

# 너무 길어 걍 생략
# 정리하면 1~20 정렬된 리스트에 a~b 까지는 역순으로 재배열하고
# 그 상태에서 a2 ~ b2 범위를 또 역순으로 재배열 함 이걸 10번 반복함

# ▣ 입력예제 1
# 5 10
# 9 13
# 1 2
# 3 4
# 5 6
# 1 2
# 3 4
# 5 6
# 1 20
# 1 20
# ▣ 출력예제 1
# 1 2 3 4 10 9 8 7 13 12 11 5 6 14 15 16 17 18 19 20

# card = [0 + i for i in range(21)]
card = [range(21)]

def Rearrangement (x, y):
    for i in range((y-x+1)//2):
        tmp = card[x+i]
        card[x+i] = card[y-i]
        card[y-i] = tmp

        # card[x+i], card[y-i] = card[y-i], card[x-i]



for _ in range(10):
    x, y = map(int ,input().split())
    Rearrangement(x, y)

card.pop(0)
for i in card:
    print(i, end=" ")