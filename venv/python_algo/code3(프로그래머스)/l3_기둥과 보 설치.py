# 보니까마리야 커맨드를 하나씩 처리하면서
# 조건이 충족되면 answer에 넣고
# 안되면 값을 버리고 뭐 이런 형태로 진행이 될꺼 같은데
# 가령말이야 기둥을 삭제했어 그럼 그 위에 있는 보 도 있을수가 없자너
# 그럼 보 도 삭제해야하니까 결국 2개가 없어지는 결과가 나오겠네???
# 그런것도 생각하고 짜야할것 같은데 말이지
# 이것도 링크드리스트처럼 클래스 구조체 만들어서 막 해야하나??
# 라고 생각했는데 예제2 를 보니까 그럴 경우 삭제가 안됨

# 그니까 만약에 보가 달린 기둥을 삭제하는 커맨드가 있다고 치면
# 보가 기둥이 없어져도 살 수 있는 따져보고 살 수 있음 없애고 안되면 무시됨
# 흠 결국 비슷한거 같긴한데 결국 연결된 보를 신경 써야한다는거니까

# 그럼 이걸 어떻게 구현하냐~
# https://blackon29.tistory.com/65
# 와 난 왤캐 구현을 못하냐, 전체탐색 해야겠다라는 생각도 못했어


def check(answer):
    for x, y, stuff in answer:
        if stuff == 0: #기둥 체크
            #'바닥 위' or '보의 한쪽 끝 위' or '또 다른 기둥 위'
            if y == 0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y-1, 0] in answer:
                continue
            return False
        elif stuff == 1: #보 체크
            #'한쪽 끝 부분이 기둥 위' or '양쪽 끝 부분이 다른 보와 동시 연결'
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                continue
            return False
    return True

def solution(n, build_frame):
    answer = []
    for build in build_frame:
        x, y, stuff, operation = build
        if operation == 1: # 설치
            answer.append([x, y, stuff])
            if not check(answer): answer.remove([x, y, stuff])
        elif operation == 0: # 삭제
            answer.remove([x, y, stuff])
            if not check(answer): answer.append([x, y, stuff])
    answer.sort()
    #print(answer)
    return answer

if __name__ == "__main__":
    n = 5
    build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
    result = [[1,0,0],[1,1,1],[2,1,0],[2,2,1],[3,2,1],[4,2,1],[5,0,0],[5,1,0]]

    answer = solution(n, build_frame)
    print(answer == result, answer)

    # n = 5
    # build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
    # result = [[0,0,0],[0,1,1],[1,1,1],[2,1,1],[3,1,1],[4,0,0]]
    #
    # answer = solution(n, build_frame)
    # print(answer == result, answer)