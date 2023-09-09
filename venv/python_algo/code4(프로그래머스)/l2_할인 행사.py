# 야 이건 진짜 절대 못할꺼 같은데
# 이건 진짜 어떻게 하냐
# https://velog.io/@ssulee0206/프로그래머스-할인-행사파이썬

from collections import Counter

def solution(want, number, discount):
    answer = 0
    check = {}
    for w, n in zip(want, number):
        check[w] = n

    for i in range(len(discount) - 9):
        c = Counter(discount[i:i + 10])

        if c == check:
            answer += 1

    return answer

if __name__ == "__main__":
    want = ["banana", "apple", "rice", "pork", "pot"]
    number = [3, 2, 2, 2, 1]
    discount = ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]
    result = 3
    answer = solution(want, number, discount)
    print(answer)
    print(result == answer)

    # want = ["apple"]
    # number = [10]
    # discount = ["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"]
    # result = 0
    # answer = solution(want, number, discount)
    # print(answer)
    # print(result == answer)