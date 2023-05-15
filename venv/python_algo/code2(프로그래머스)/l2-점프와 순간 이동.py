# 한 번에 K 칸을 앞으로 점프하거나,
# (현재까지 온 거리) x 2 에 해당하는 위치로 순간이동을 할 수 있는
# 특수한 기능을 가진 아이언 슈트를 개발하여 판매하고 있습니다.
# 순간이동을 하면 건전지 사용량이 줄지 않지만, 앞으로 K 칸을 점프하면 K 만큼의 건전지 사용량이 듭니다
# 거리 N이 주어졌을 때, 사용해야 하는 건전지 사용량의 최솟값을 return하는 solution 함수를 만들어 주세요.

def solution(n):
    if n == 1:
        return 1
    checklist = [0] * (n+1)
    checklist[1] = 1

    plus = 2
    for i in range(2,n+1):
        if checklist[i] == 0:
            if i % 2 == 0:
                prevIndex = i // 2
                checklist[i] = checklist[prevIndex]
            else:
                checklist[i] = checklist[i-plus] + 1
                plus += 1

    ans = checklist[n]
    return ans


def solution2(n):
    ans = 0
    while n > 0:
        if n % 2 == 0:
            n /= 2
        else:
            n -= 1
            ans += 1

    return ans

if __name__ == "__main__":
    n = 5
    result = 2

    n2 = 6
    result2 = 2

    n3 = 5000
    result3 = 5

    res = solution(n)
    res2 = solution(n2)
    res3 = solution(n3)

    print(res)
    print(res2)
    print(res3)

    print("정답입니다" if res == result else "틀렸습니다 모지리 새끼야")
    print("정답입니다" if res2 == result2 else "틀렸습니다 모지리 새끼야")
    print("정답입니다" if res3 == result3 else "틀렸습니다 모지리 새끼야")





# 1 >> + 1
    # 2 >> + 1 ^ 2
    # 3 >> + 1 ^ 2 + 3 // 2 >>> [1] + 1 이랑 똑같 2차이
    # # 4 >> + 1 ^ 2 ^ 4 >> 2랑 동일
    # 5 >> + 1 ^ 2 ^ 4 + 5 // 2 >>> [2] + 1 이랑 똑같 3차이
    # # 6 >> + 1 ^ 2 + 3 ^ 6 >> 3이랑 동일
    # 7 >> + 1 ^ 2 + 3 ^ 6 + 7 // 3 >>> [3] + 1 이랑 똑같 4차이
    # # 8 >> 4 랑 동일
    # 9 >> + 1 ^ 2 ^ 4 ^ 8 + 9 // 2 >>> [4] + 1 이랑 똑같 5 차이
    # # 10 >> 5랑 동일
    # 11 >> + 1 ^ 2 ^ 4 + 5 ^ 10 + 11 // 3 >>> [5] + 1 이랑 똑같 6 차이
    # # 12 >> 6이랑 동일
    # 13 >> + 1 ^ 2 + 3 ^ 6 ^ 12 + 13 // 3  >>> [6] + 1 이랑 똑같 7 차이