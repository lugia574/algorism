# 이 문제는 위상정렬에 대해 알아야함
# 위상정렬: 순서가 정해져 있는 작업
# https://www.youtube.com/watch?v=qzfeVeajuyc
# https://hongcoding.tistory.com/94
# 설명 듣고 보니 이거 내가 풀었던거 알고리즘임
# dp 3번 폴더에 ACM, 게임개발 보면 나옴

import sys, heapq

def searchInDegree(x):
    if inDegree[x] == 0:
        heapq.heappush(q, i)

if __name__ == "__main__":
    input = sys.stdin.readline
    n, m = map(int, input().split())
    answer = []
    graph = [[] for _ in range(n+1)]
    inDegree = [0] * (n+1)
    q = []

    # 그래프 차수 대입
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        inDegree[b] += 1

    # 차수가 0 인 얘를 heapQ 에 집어넣어
    for i in range(1, n+1):
        searchInDegree(i)

    # 0이 들어간 q 를 돌려서 해당 problemNum 이 뻗은 num 들의 차수를 깍음
    # 깍은 num 의 차수가 0 이면 q 에 추가
    while q:
        prNum = heapq.heappop(q)
        answer.append(prNum)
        for i in graph[prNum]:
            inDegree[i] -= 1
            searchInDegree(i)

    print(*answer)