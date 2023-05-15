# 성격 유형 검사하기
# 지표 번호	성격 유형
# 1번 지표	라이언형(R), 튜브형(T)
# 2번 지표	콘형(C), 프로도형(F)
# 3번 지표	제이지형(J), 무지형(M)
# 4번 지표	어피치형(A), 네오형(N)

# 4개의 지표가 있으므로 성격 유형은 총 16(=2 x 2 x 2 x 2)가지가 나올 수 있습니다.
# 예를 들어, "RFMN"이나 "TCMA"와 같은 성격 유형이 있습니다.
# 검사지에는 총 n개의 질문이 있고, 각 질문에는 아래와 같은 7개의 선택지가 있습니다.
# 1.매우 비동의 2.비동의 3.약간 비동의 4.모르겠음 5.약간 동의 6.동의 7.매우 동의

# 질문마다 판단하는 지표를 담은 1차원 문자열 배열 survey와 검사자가
# 각 질문마다 선택한 선택지를 담은 1차원 정수 배열 choices가 매개변수로 주어집니다.
# 이때, 검사자의 성격 유형 검사 결과를 지표 번호 순서대로 return 하도록 solution 함수를 완성해주세요.

# 제한사항
# 1 ≤ survey의 길이 ( = n) ≤ 1,000
# survey의 원소는 "RT", "TR", "FC", "CF", "MJ", "JM", "AN", "NA" 중 하나입니다.
# survey[i]의 첫 번째 캐릭터는 i+1번 질문의 비동의 관련 선택지를 선택하면 받는 성격 유형을 의미합니다.
# survey[i]의 두 번째 캐릭터는 i+1번 질문의 동의 관련 선택지를 선택하면 받는 성격 유형을 의미합니다.
# choices의 길이 = survey의 길이
#
# choices[i]는 검사자가 선택한 i+1번째 질문의 선택지를 의미합니다.
# 1 ≤ choices의 원소 ≤ 7


def solution(survey, choices):
    ans = ""
    obj = {
        "R": 0,
        "T": 0,
        "C": 0,
        "F": 0,
        "J": 0,
        "M": 0,
        "A": 0,
        "N": 0,
    }
    el = [["R","T"], ["C", "F"], ["J", "M"], ["A", "N"]]
    while survey:
        tag,tag2 = list(survey.pop())
        ch = choices.pop()
        point = ch - 4
        title = tag2
        if point < 0:
             point = point * -1
             title = tag
        obj[title] += point

    for x, y in el:
        if obj[x] < obj[y]:
            ans += y
        else:
            ans += x

    return ans

if __name__ == "__main__":
    # survey = ["AN", "CF", "MJ", "RT", "NA"]
    # choices = [5, 3, 2, 7, 5]

    survey = ["TR", "RT", "TR"]
    choices = [7, 1, 3]
    ans = solution(survey, choices)
    print(ans)