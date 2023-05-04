# 0과 1로 이루어진 어떤 문자열 x에 대한 이진 변환을 다음과 같이 정의합니다.
#
# x의 모든 0을 제거합니다.
# x의 길이를 c라고 하면, x를 "c를 2진법으로 표현한 문자열"로 바꿉니다.

# 예를 들어, x = "0111010"이라면, x에 이진 변환을 가하면 x = "0111010" -> "1111" -> "100" 이 됩니다.
#
# 0과 1로 이루어진 문자열 s가 매개변수로 주어집니다.
# s가 "1"이 될 때까지 계속해서 s에 이진 변환을 가했을 때,
# 이진 변환의 횟수와 변환 과정에서 제거된 모든 0의 개수를 각각 배열에 담아 return 하도록 solution 함수를 완성해주세요.

def solution_sol(s):
    a, b = 0, 0
    while s != '1':
        a += 1
        num = s.count('1')
        b += len(s) - num
        s = bin(num)[2:]
    return [a, b]

def binaryScale(len):
    result = []
    while len != 0:
        if len % 2 == 1:
            result.insert(0, "1")
            len = (len-1)/2
        else:
            result.insert(0, "0")
            len = len/2
    return result


def solution(s):
    conversion = 0
    zeroCount = 0
    arr = list(s)

    while len(arr) > 1:
        conversion += 1
        tmp = []
        for i in arr:
            if i == "1":
                tmp.append(i)
            else:
                zeroCount += 1
        arr = binaryScale(len(tmp))


    return [conversion, zeroCount]

if __name__ == "__main__":
    s = "110010101001"
    result = [3,8]
    ans = 0
    res = solution(s)
    for i in range(len(result)):
        if res[i] != result[i]:
            ans = 1
    print("True" if ans == 0 else "False")

    s = "01110"
    result = [3, 3]
    ans = 0
    res = solution(s)
    for i in range(len(result)):
        if res[i] != result[i]:
            ans = 1
    print("True" if ans == 0 else "False")

    s = "1111111"
    result = [4, 1]
    ans = 0
    res = solution(s)
    for i in range(len(result)):
        if res[i] != result[i]:
            ans = 1
    print("True" if ans == 0 else "False")
