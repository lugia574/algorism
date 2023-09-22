# 아 그 뭐냐 권태기 그런 시기다
# 한동안 알고리즘 쳐다도 보기 싫은 시기
# 시기가 와버렸어
# 이럴땐 그냥 전에 풀었던거나 한번식 보는게 나을듯 ㄹㅇ 걍 손 대기가 싫어
# 어차피 계속 머리속에 있는것들 휘발되어버리는데 다시 쑤셔 박는게 좋을듯 
# 라고 해도 우선 이 문제는 풀고 치워버리자 는 존나 하기 싫은데 는 그래도 해야지
# https://velog.io/@sin5015243/백준-14503-로봇-청소기-Python
# 는 심각하다 구현 하나 제대로 못하는 등신입니다!~
import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    ## 북, 동, 하, 서 ( 시계방향 )
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    n, m = map(int, input().split())
    r, c, d = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    ## 방문 쳌
    visited = [[0] * m for _ in range(n)]

    ## 시작지 방문쳌 and 카운트!
    visited[r][c] = 1
    cnt = 1

    while True:
        flag = 0  ## 아직 아무것도 청소 안했음!
        for _ in range(4):  ## 4방향을 돈다!
            d = (d + 3) % 4  ## 왼쪽방향으로 한 칸 돌린다! 중요!!!!!1
            nr = r + dr[d]
            nc = c + dc[d]

            ## 범위 안에 들고, 빈 칸이고, 청소할 수 있다면!
            ## 들려서 청소하고, 카운트하고, 현재 위치를 갱신하고, flag 변경!
            if 0 <= nr < n and 0 <= nc < m and arr[nr][nc] == 0:
                if visited[nr][nc] == 0:
                    visited[nr][nc] = 1
                    cnt += 1
                    r = nr
                    c = nc
                    flag = 1  ## 청소 했다는 뜻
                    break

        if flag == 0:  ## 위의 for문에 들어가지 못했을 때
            ## 즉 네 방향 모두 청소를 할 수 없을 때
            ## 후진 했을 때 벽이면 break
            ## 만약 뒤가 벽이 아니라면! 그 위치를 다시 갱신!!!
            if arr[r - dr[d]][c - dc[d]] == 1:
                print(cnt)
                break
            else:
                r, c = r - dr[d], c - dc[d]