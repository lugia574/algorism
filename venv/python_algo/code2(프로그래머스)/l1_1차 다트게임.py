# 존나 귀찮은 문제네
# 아 그보다 졸리다 ㅋ
# 스타상(*) 당첨 시 해당 점수와 바로 전에 얻은 점수를 각 2배
# 아차상(#) 당첨 시 해당 점수는 마이너스


def solution(dartResult):
    point = []
    answer = []
    dartResult = dartResult.replace('10','k')
    point = ['10' if i == 'k' else i for i in dartResult]
    print(point)

    i = -1
    sdt = ['S', 'D', 'T']
    for j in point:
        if j in sdt :
            answer[i] = answer[i] ** (sdt.index(j)+1)
        elif j == '*':
            answer[i] = answer[i] * 2
            if i != 0 :
                answer[i - 1] = answer[i - 1] * 2
        elif j == '#':
            answer[i] = answer[i] * (-1)
        else:
            answer.append(int(j))
            i += 1
    return sum(answer)


if __name__ == "__main__":
    dartResult = "1S2D*3T"
    res = 37
    answer = solution(dartResult)
    print(res == answer, answer)

    # dartResult = "1D2S#10S"
    # res = 9
    # answer = solution(dartResult)
    # print(res == answer, answer)
    #
    # dartResult = "1D2S0T"
    # res = 3
    # answer = solution(dartResult)
    # print(res == answer, answer)
    #
    # dartResult = "1S*2T*3S"
    # res = 23
    # answer = solution(dartResult)
    # print(res == answer, answer)
    #
    # dartResult = "1D#2S*3S"
    # res = 5
    # answer = solution(dartResult)
    # print(res == answer, answer)
    #
    # dartResult = "1T2D3D#"
    # res = -4
    # answer = solution(dartResult)
    # print(res == answer, answer)
    #
    # dartResult = "1D2S3T*"
    # res = 59
    # answer = solution(dartResult)
    # print(res == answer, answer)
