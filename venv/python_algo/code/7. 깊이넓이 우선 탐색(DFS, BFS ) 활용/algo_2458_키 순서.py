# 어려운데? 이게 왜 정답률 50% 임?
# 이걸 워샬로 푼다고 한들 어떻게 키 판별이 되는지 안되는지를 알아냄??
# https://bbbyung2.tistory.com/87 이 풀이가 그나마 알만툴
# 근데 이 문제 원래 DFS 로 풀려고 했음 ㅋㅋㅋ
# https://alpyrithm.tistory.com/105 이렇게 풀면 될듯
# 대충 어떻게 돌아가는지 알았으니까 안보고 자바로 한번 풀어보자
import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    n, m = map(int, input().split())
    graph = [[0] * (n+1) for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a][b] = 1

    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if graph[i][k] + graph[k][j] == 2:
                    graph[i][j] = 1

    answer = [0] * (n+1)
    for a in range(1, n+1):
        for b in range(1, n+1):
            if graph[a][b] == 1:
                answer[a] += 1
                answer[b] += 1

    # print(answer)
    print(answer.count(n-1))