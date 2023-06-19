# 입력수도 작겠다 (2500) 그냥 2중 포문 돌려서 [i : j] 슬라이싱해서 팰린드롬인지 확인함
# 함수 안에도 1/2 포문 돌아가니까 사실상 3중 포문이라고 할수 있음
# 그래도 잘됐음 근데 아쉽게도 효율성 검사에서 조짐
# 이건 투 포인트 탐색으로 풀어야하나봄
# max(answer, palin(n, s, i, i+1), palin(n, s, i, i+2)) 이렇게 하는 이유는
# 짝수일때 홀수일때 다 대응할려고

def palin(n, arr, lt, rt):
    if rt - lt == 1:
        length = 0
    else:
        length = 1

    while lt >= 0 and rt < n:
        if arr[lt] == arr[rt]:
            lt -= 1
            rt += 1
            length += 2
        else:
            break

    return length

def solution(s):
    answer = 1
    n = len(s)
    if n == 1 or s == s[::-1]:
        return n

    for i in range(n - 2):
        answer = max(answer, palin(n, s, i, i+1), palin(n, s, i, i+2))
    return answer

if __name__ == "__main__":
    # s = "abcdcba"
    # res = 7
    # answer = solution(s)
    # print(res == answer, answer)

    s = "abacde"
    res = 3
    answer = solution(s)
    print(res == answer, answer)