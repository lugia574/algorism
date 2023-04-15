# https://hongcoding.tistory.com/127
# 아래껀 챗gpt 한태 물어봤는데 이렇게 짜줌

import sys
from collections import deque

if __name__ == "__main__":
    input = sys.stdin.readline
    # 보드의 크기 N
    N = int(input())

    # 사과의 개수 K
    K = int(input())

    # 사과의 위치 정보
    apples = []
    for _ in range(K):
        apple = tuple(map(int, input().split()))
        apples.append(apple)

    # 뱀의 방향 변환 횟수 L
    L = int(input())

    # 뱀의 방향 변환 정보
    directions = {}
    for _ in range(L):
        X, C = input().split()
        directions[int(X)] = C

    # 뱀의 현재 위치와 방향
    snake = deque([(1, 1)])  # 시작 위치는 (1, 1)
    dx = [0, 1, 0, -1]  # 동, 남, 서, 북
    dy = [1, 0, -1, 0]
    direction = 0  # 초기 방향은 동쪽
    time = 0  # 게임 시작 시간

    while True:

        time += 1

        # 뱀의 다음 위치
        head = snake[0]
        next_x = head[0] + dx[direction]
        next_y = head[1] + dy[direction]

        # 벽 또는 자기자신의 몸과 부딪힌 경우 게임 종료
        if next_x < 1 or next_x > N or next_y < 1 or next_y > N or (next_x, next_y) in snake:
            break

        # 사과가 있는 경우 뱀의 길이를 늘려주고 사과를 없앰
        if (next_x, next_y) in apples:
            apples.remove((next_x, next_y))
        else:
            snake.pop()  # 사과가 없는 경우 꼬리를 줄여줌

        snake.appendleft((next_x, next_y))  # 뱀의 머리를 다음 위치로 이동

        # 뱀의 방향 변경 확인
        if time in directions:
            if directions[time] == 'D':  # 오른쪽으로 90도 회전
                direction = (direction + 1) % 4
            else:  # 왼쪽으로 90도 회전
                direction = (direction - 1) % 4
    print(time)

