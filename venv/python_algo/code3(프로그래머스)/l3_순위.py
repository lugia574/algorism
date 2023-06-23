# 아니 ㅋ 난 애내가 문제를 뭔소리 하면서 내는지 바로 이해가 안돼 ㅋㅋ
# 한 8할이 그래 ㅋㅋ
# 결과를 알수 있는 사람 수를 리턴하라는데
# 토너먼트같은게 아니라 다전제인거 같은데
#  A 선수가 B 선수보다 실력이 좋다면 A 선수는 B 선수를 항상 이깁니다.
# 이거때문에 무조건 파워게임이라는 소린가?
# 그래서 2번이 4위고 그 2번이 5번응을 이겼으니가 5번은 5위라고?
# 5번은 다른 애들이랑 어떻게 싸워도 무조건 질꺼니까?
# 흠
# 대충 설명을 하자면

def solution(n, results):
    # 2중 배열을 선언해 이 배열이 경기판임
    total = [['?' for i in range(n)] for j in range(n)]
    # 자기자신의 경우는 self 로 퉁쳐
    for i in range(n):
        total[i][i] = 'S'
    # 이제 result 배열 값을 받아서 경기판에 박아넣어
    # 1,2 일시 1번이 2번을 이겼다는 소리니까 [1][2] = 'W', [2][1] = 'L' 라고 박아 넣으면 됨
    for res in results:
        total[res[0]-1][res[1]-1] = 'W'
        total[res[1]-1][res[0]-1] = 'L'

    # 자 이게 유추의 시간임
    # 자 1 - 2 야 그리고 2 - 3 이야
    # 문제에서는 무조건 파워겜이라고 그랬음
    # 그럼 당연히 1- 3 도 맞는 말이지
    # 여기서 주의할점은 1 - 2, 3 - 2 와 같은 경우는 안된다는거임
    # 플로이드 와샬과 비슷하게 구현 되는데 다른점은 계속 갱신을 안해도 되는 점 ㅎㅎ
    # 그러니까 한번 값을 넣기만 하면 이후 해당 얘는 안건드려도 됨 ㅎㅎ 그래서 i, j == '?' 일때만으로 조건절을 추가함 ㅎ
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if total[i][j] == '?':
                    if total[i][k] == 'W' and total[k][j] == 'W':
                        total[i][j] = 'W'
                    elif total[i][k] == 'L' and total[k][j] == 'L':
                        total[i][j] = 'L'
    answer = 0

    for p in total:
        if '?' not in p:
            answer += 1
    return answer

if __name__ == "__main__":
    n = 5
    arr = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
    res = 2

    ans = solution(n, arr)
    print(res == ans, ans)