# 문제가 말이 많다
# 봄: 자신의 나이만큼 양분 먹고 나이 1 증가, 한칸에 여러 나무가 있으면 나이가 어린 나무부터 먹음, 양분이 없음 나무 죽음
# 여름: 죽은 나무가 양분이 됨 나이를 2로 나눈 값이 양분 소수점 아래는 버림
# 가을: 나이가 5의 배수면 번식 인접한 8개 칸에서 나이가 1인 나무가 생김
# 겨울: 땅에 양분 추가 양분 양은 입력으로 주어짐
# k 년이 지났을때 나무 갯수
# 시초 뜨네
# https://www.google.com/search?q=16235+py&oq=16235+py&aqs=chrome..69i57.3477j0j7&sourceid=chrome&ie=UTF-8
# 여기 보면 어떻게 막 한게 보이는데 솔직히
# https://velog.io/@hammii/백준-16235-나무-재테크-java 자바 형식으로 한게 더 보기 좋다

import sys
from collections import deque


class Tree:
    def __init__(self, x, y, age):
        self.x = x
        self.y = y
        self.age = age


if __name__ == "__main__":
    input = sys.stdin.readline
    n, m, k = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    data = [[5] * n for _ in range(n)]
    forest = deque()
    new_trees = []  # 가을 단계에서 새로 생긴 나무들을 저장할 리스트
    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, -1, -1, -1, 0, 1, 1, 1]

    for _ in range(m):
        x, y, age = map(int, input().split())
        t = Tree(x-1, y-1, age)
        forest.append(t)

    for _ in range(k):
        forest = deque(sorted(forest, key=lambda t: (t.x, t.y, t.age)))
        length = len(forest)
        if length == 0: break
        trash = deque()
        # 봄
        for i in range(length):
            tmp = forest.popleft()
            x, y = tmp.x, tmp.y
            if data[x][y] >= tmp.age:
                data[x][y] -= tmp.age
                tmp.age += 1
                forest.append(tmp)
            else:
                trash.append(tmp)

        # 여름
        for t in trash:
            data[t.x][t.y] += t.age // 2

        # 가을
        for tree in forest:
            if tree.age % 5 != 0:
                continue
            for i in range(8):
                nx = tree.x + dx[i]
                ny = tree.y + dy[i]
                if 0 > nx or nx >= n or 0 > ny or ny >= n:
                    continue
                tmpTree = Tree(nx, ny, 1)
                new_trees.append(tmpTree)  # 새로 생긴 나무들을 일단 따로 저장

        # 겨울
        for i in range(n):
            for j in range(n):
                data[i][j] += board[i][j]

        # 새로 생긴 나무들을 기존의 나무 리스트에 추가
        forest += new_trees
        new_trees.clear()

    print(len(forest))

