# https://velog.io/@rlaalswn3282/프로그래머스-아이템-줍기
#  2배를 주고 테두리를 잡았다 그 이유는 2배를 안주면 길이 아니여도 1칸 차이가 날 수 있기 때문에 경로가 되어 버린다.
from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0

    # 제한사항에서 모든 좌표값은 1 이상 50 이하라고 했고 2배의 좌표를 그려야 하므로 102*102 크기의 2차원 배열 선언
    field = [[-1] * 102 for i in range(102)]

    # 직사각형 그리기
    for r in rectangle:
        # 모든 좌표값 2배
        x1, y1, x2, y2 = map(lambda x: x * 2, r)

        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                # x1, x2, y1, y2는 테두리이므로 제외하고 내부만 0으로 채움
                if x1 < i < x2 and y1 < j < y2:
                    field[i][j] = 0
                # 다른 직사각형의 내부가 아니면서 테두리일 때 1로 채움
                elif field[i][j] != 0:
                    field[i][j] = 1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 큐에 캐릭터 출발지점 추가 & 최단거리를 적어줄 visited 배열 선언
    q = deque()
    q.append([characterX * 2, characterY * 2])
    visited = [[1] * 102 for i in range(102)]

    while q:
        x, y = q.popleft()
        # 도착한 곳이 아이템이 있는 장소라면 현재의 최단거리(나누기 2)를 answer로 하고 while문을 빠져나옴
        if x == itemX * 2 and y == itemY * 2:
            answer = visited[x][y] // 2
            break
        # 아니라면 상하좌우 네 방향을 체크하면서
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            # 현재 좌표가 테두리이고 아직 방문하지 않은 곳이라면 q에 추가 후 visited 최단거리로 갱신
            if field[nx][ny] == 1 and visited[nx][ny] == 1:
                q.append([nx, ny])
                visited[nx][ny] = visited[x][y] + 1

    return answer

if __name__ == "__main__":
    rectangle = [[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]]
    characterX = 1
    characterY = 3
    itemX = 7
    itemY = 8
    res = 17

    ans = solution(rectangle, characterX, characterY, itemX, itemY)
    print(res == ans)