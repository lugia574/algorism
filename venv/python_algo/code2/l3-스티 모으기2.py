# N개의 스티커가 원형으로 연결되어 있습니다.
# 원형으로 연결된 스티커에서 몇 장의 스티커를 뜯어내어 뜯어낸 스티커에 적힌 숫자의 합이 최대가 되도록 하고 싶습니다.
# 단 스티커 한 장을 뜯어내면 양쪽으로 인접해있는 스티커는 찢어져서 사용할 수 없게 됩니다.
# 제한 사항
# sticker는 원형으로 연결된 스티커의 각 칸에 적힌 숫자가 순서대로 들어있는 배열로, 길이(N)는 1 이상 100,000 이하입니다.
# sticker의 각 원소는 스티커의 각 칸에 적힌 숫자이며, 각 칸에 적힌 숫자는 1 이상 100 이하의 자연수입니다.
# 원형의 스티커 모양을 위해 sticker 배열의 첫 번째 원소와 마지막 원소가 서로 연결되어있다고 간주합니다.

# https://school.programmers.co.kr/questions/24769

# 그러네 뭐가 문제인지 이제 이해했어
# 그냥 단순히 얼마나 많이 뽑냐로만 생각해서 단순히 시작 지점에서 index + 2 만 돌려서 sum 값 했는데
# 그럼 안되지 시이발 막말로 1, 2, 4, 999999, 8, 5, 88888888, 9  이렇다고 했을때 
# 원래 0부터 시작하거나 1 부터 시작해서 index +2 하는 경우 999~ 나 8888~ 둘중에 하나밖에 못챙겨
# 근데 그럴 필요가 없자나 그냥 999999  88888888 이거 두개만 챙겨도 다른것들 다 합친것보다 안되자나
# 이걸 전혀 염두에 두지 않았어
# 그래서 안된거야
# 이걸 할려면 dp  방식으로 풀어야해

import math




def solution(sticker):
    n = len(sticker)
    answer = 0

    if n == 1:
        return sticker[0]

    for i in range(2):
        numSum = 0
        index = i
        while index < n:
            numSum += sticker[index]
            index += 2

        if numSum > answer:
            answer = numSum

    return answer

if __name__ == "__main__":
    sticker = [14, 6, 5, 11, 3, 9, 2, 10]
    answer = 36

    ans = solution(sticker)
    print(ans)
    print("True" if ans == answer else "False")

    sticker2 = [1, 3, 2, 5, 4]
    answer2 = 8

    ans2 = solution(sticker2)
    print(ans2)
    print("True" if ans2 == answer2 else "False")

    sticker3 = [1, 2, 4, 999999, 8, 5, 88888888, 9]
    answer3 = 999999 + 88888888 + 2

    ans3 = solution(sticker3)
    print(ans3)
    print("True" if ans3 == answer3 else "False")