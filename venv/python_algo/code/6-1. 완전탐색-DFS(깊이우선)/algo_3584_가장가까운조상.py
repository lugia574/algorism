# 어떻게 풀어야할지 모르겠는데??
# 그 뭐지 DFS 로 하면 터질꺼고 
# 유니온 파인드는 애초에 여기 맞는 방법이 아니지
# 에휴 찾아보니 재귀로 안하고 깊이 탐색을 하면 됨
# https://velog.io/@dhelee/백준-3584번-가장-가까운-공통-조상-Python-그래프-탐색
# 각각 while 문으로 노드의 부모들을 찾아 배열에 박아놓고
# 해당 배열의 뒤부터 비교해서 하나하나 내려가다가 달라지면 그때 반복을 그만두면 됨
import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    for _ in range(int(input())):
        n = int(input())
        parent = [0] * (n + 1)  # 각 노드의 부모 저장
        for _ in range(n - 1):
            i, j = map(int, input().split())
            parent[j] = i
        x, y = map(int, input().split())

        findParentX = [x]
        findParentY = [y]

        while parent[x]:
            findParentX.append(parent[x])
            x = parent[x]

        while parent[y]:
            findParentY.append(parent[y])
            y = parent[y]

        sizeX = len(findParentX)
        sizeY = len(findParentY)

        # print(findParentX, findParentY)
        i = 1
        while findParentX[sizeX-i] == findParentY[sizeY-i]:
            i += 1

        print(findParentX[sizeX - i + 1])
