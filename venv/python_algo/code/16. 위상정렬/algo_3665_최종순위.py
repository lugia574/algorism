# 이 문제는 일반 위상정렬이랑 좀 다름
# 먼저 위상정렬을 만들고 나서 변경하는 것임
# https://hongcoding.tistory.com/96
# 어렵다 이거
from collections import deque
import sys


if __name__ == "__main__":
    input = sys.stdin.readline
    for i in range(int(input())):
        n = int(input())

        graph = [[] for _ in range(n + 1)]
        inDegree = [0 for _ in range(n + 1)]
        queue = deque()
        answer = []

        team = list(map(int, input().split()))

        for j in range(n - 1):
            for k in range(j + 1, n):
                graph[team[j]].append(team[k])
                inDegree[team[k]] += 1

        m = int(sys.stdin.readline())
        for j in range(m):
            first, second = map(int, sys.stdin.readline().rstrip().split())
            changed = False

            for k in graph[first]:
                if k == second:
                    graph[first].remove(second)
                    inDegree[second] -= 1
                    graph[second].append(first)
                    inDegree[first] += 1
                    changed = True

            if not changed:
                graph[second].remove(first)
                inDegree[first] -= 1
                graph[first].append(second)
                inDegree[second] += 1

        for j in range(1, n + 1):
            if inDegree[j] == 0:
                queue.append(j)

        if not queue:
            print("IMPOSSIBLE")
            continue

        result = True
        while queue:
            if len(queue) > 1:
                result = False
                break

            tmp = queue.popleft()
            answer.append(tmp)
            for j in graph[tmp]:
                inDegree[j] -= 1
                if inDegree[j] == 0:
                    queue.append(j)
                elif inDegree[j] < 0:
                    result = False
                    break

        if not result or len(answer) < n:
            print("IMPOSSIBLE")
        else:
            print(*answer)