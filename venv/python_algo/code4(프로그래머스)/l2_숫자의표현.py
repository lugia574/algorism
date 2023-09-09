# https://velog.io/@younge/Python-프로그래머스-숫자의-표현-연습문제Level-2

def solution(n):
    answer = 0
    for i in range(1, n+1):
        sumVal = 0
        for j in range(i, n+1):
            sumVal += j
            if sumVal == n:
                answer += 1
                break
            elif sumVal > n:
                break
    return answer


if __name__ == "__main__":
    answer = solution(15)
    res = 4
    print(answer == res)