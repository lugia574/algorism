# 흠 흠 흠 처음게 무조건 알라봉이라느 ㄴ소린데
# 지금 알라친구 등수만 알면 되자너
# https://sundryy.tistory.com/109
# https://www.ai-bio.info/programmers/152995
# 나 심각한데 ㄹㅇ루 이거 딱봐도 별거 아닌 문젠데 이걸 모르자너
# 무슨 플로이드 와샬알고리즘을 쓰냐 최소 신장트리를 묻냐 깊이 탐색을 하냐?
# 정렬이라는 것도 제대로 못해가지고 아주 ㅋ

# 기본적으로 뭐를 비교해서 등수를 매긴다? 그냥 정렬이 짜세야
# 그리고 그 항목이 2개 이상이면 첫번째 요소는 정렬로 하고 두번째 요소부턴
# 그 정렬된 값을 반복문으로 돌면서 해당 조건에 맞는지 비교 판단 해야하는거지
# 이 문제는 총합을 기준으로 등수를 나누고 두개의 요소 모두 남보다 낮은 놈이 있는 경우 아예 제외버려
# 총합을 기준으로 등수를 나누니까 먼가 총합으로 정렬해야하나 라고 생각 할 수 있는데
# 흠 그래도 될꺼 같은데 흠흠흠
# 우선 첫번재 요소를 내림차순으로 정렬 하고 두번째 요소는 오름차순으로 정렬해
# 
def solution(scores):
    answer = 1

    target = scores[0]
    target_score = sum(scores[0])
    scores.sort(key=lambda x: (-x[0], x[1])) # 첫번째는 내림차순 두번째는 오름차순으로 정렬한다는 소리

    threshold = 0 # 한계점
    for score in scores:
        # 대상보다 둘다 높은 놈이 있을땐 아예 제외됨
        if target[0] < score[0] and target[1] < score[1]:
            return -1
        # threshold보다 크거나 같은 경우에만 석차를 증가
        # 나중에 탐색하는 학생의 두 번째 점수가 먼저 탐색하는 학생의 두 번째 점수보다 작은 경우가 단 하나라도 있으면 해당 학생보다 두 점수가 높은 학생이 있음이 보장되게 됩니다.
        # 즉 제외 되는 놈을 말하는거임
        if threshold <= score[1]:
            if target_score < score[0] + score[1]:
                answer += 1
            threshold = score[1]
            
    return answer

if __name__ == "__main__":
    # scores = [[2,2],[1,4],[3,2],[3,2],[2,1]]
    # res = 4
    #
    # answer = solution(scores)
    # print(res == answer, answer)

    scores = [[3, 1], [1, 4], [2, 3], [2, 3], [1, 5], [1, 0], [1, 0]]
    res = 5

    answer = solution(scores)
    print(res == answer, answer)