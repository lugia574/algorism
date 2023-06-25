# https://velog.io/@mrbartrns/프로그래머스-파괴되지-않은-건물-python
# 이게 그냥 쳐하면 안돼
# 효율성에서 터져버려
# 누적합으로 풀어야함

# 뭐가 포인트냐면
# skill을 하나하나 값 박을게 아니라
# 그냥 미리 다 계산해서 정리된 값을 바로 박아야해
# 값이 음수까지 갈수 있고 더하고 빼고 순서가 의미 없는 결과값만 중요하기 때문에
# 하나하나 어디부터 어디까지 값을 더하고 빼고 이 ㅈㄹ을 할 여유가 없음

# 시작 부분과 끝 부분이 정해져있을 때, 시작 부분에 더하고자 하는 값을 더해준다.
# 마지막 부분 + 1번째 인덱스에 더한 값을 빼준다.
# 가령 1 1 1 1 1 이라는 배열이 있다고 했을때
# 1번 인덱스부터 3번 인덱스까지 +2 된다고 치면
# 0 2 0 0 -2 이렇게 배열을 선언하고 앞 배열을 누적해서 값을 더해주는거임
# 그럼 실질적으로는 0 2 2 2 0 이라는 값을 더하게 되는거임

# 이건 1차원 배열 누적합이고 이걸 2차원 배열은 행과 열로 기록을 해야함
# 0 0 0 0
# 0 0 0 0
# 0 0 0 0 이라고 했을때 0,0 부터 2,2 까지 2만큼 더한다고 하면

# 2  0  0  -2
# 0  0  0   0
# -2 0  0   2 이렇게 됨
# 와 근데 어렵다 ㅋㅋ
def solution(board, skill):
    answer = 0
    n = len(board)
    m = len(board[0])
    check = [[0] * (m+1) for _ in range(n+1)]

    for type, r1, c1, r2, c2, degree in skill:
        damage = degree if type == 2 else -degree

        check[r1][c1] += damage
        check[r1][c2+1] -= damage
        check[r2 + 1][c1] -= damage
        check[r2 + 1][c2 + 1] += damage

    # 행 누적합
    for i in range(n):
        for j in range(m):
            check[i][j+1] += check[i][j]
    # 열 누적합
    for j in range(m):
        for i in range(n):
            check[i+1][j] += check[i][j]
            
    # print("누적합 결과값 함 보자")
    # for x in check:
    #     print(x)
    
    # 누적값 대입
    for i in range(n):
        for j in range(m):
            board[i][j] += check[i][j]
            if board[i][j] > 0:
                answer += 1
    return answer

if __name__ == "__main__":
    board = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]
    skill = [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]
    res = 10

    ans = solution(board, skill)
    print(res == ans, ans)

    board = [[1,2,3],[4,5,6],[7,8,9]]
    skill = [[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]
    res = 6

    ans = solution(board, skill)
    print(res == ans, ans)