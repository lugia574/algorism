# 문제
# 주어진 수열을 재배치하여 수열의 포함된 각각의 숫자가
# 원래 숫자보다 커지는 경우가 가장 많도록 하고,
# 이 때, 기존 수보다 커진 숫자의 개수를 구하시오.

# 예제입력)
# 3, 1, 2
# 예제 결과)
# 2
# 예제 풀이)
# 주어진 3, 1, 2 수열을 1, 2, 3 으로 재배치하면
# 3 > 1 이 되고 1 > 2, 2 > 3 이 되어 원래 값보다 커지게 됨
# 이중 원래 숫자보다 커진 경우는 2개가 되어 답은 2

# 쉽네 이거 그냥 딕셔너리로 해버리면 됨

def solution(arr):
    answer = 0
    dic = {}
    for idx, x in enumerate(arr):
        dic[idx] = x
    arr.sort()
    #print(arr)
    for idx, x in enumerate(arr):
        if dic[idx] != x and dic[idx] < x:
            answer += 1
    return answer

if __name__ == "__main__":
    arr = [3, 1, 2]
    res = 2
    answer = solution(arr)
    print(res == answer, answer)

    arr = [1, 3, 2, 4, 3, 3, 3]
    answer = solution(arr)
    print(answer)

    arr = [4, 6, 3, 4, 4, 4, 6, 7, 4, 5]
    answer = solution(arr)
    print(answer)

    arr = [5, 5, 6, 3, 6, 8, 3, 6, 1, 5, 8, 5]
    answer = solution(arr)
    print(answer)