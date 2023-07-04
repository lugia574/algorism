# 이 문제는 음수가 있기 때문에 다익스트라 알고리즘을 적용해서 풀수가 없음
# 왜 음수가 있으면 안되냐?
# https://www.youtube.com/watch?v=Ppimbaxm8d8
# 대충 요약하면 음수가 있으면 음의 순환에 빠질수 있기 때문임
# 순환에 빠지게 되면 if ditance[now] < dist: continue 이런 필터링도 의미 없게 되고 존나 돌다가 터져버림
# 그래서 푸는 방법이 벨만 포드 알고리즘임
# 해당 알고리즘 시간복잡도는 V * E 만큼 보는거라 다익스트라보다는 좀더 오래 걸림
import sys

def bf(start):
    distance[start] = 0

    for i in range(n):
        for j in range(m):
            now, nextNode, cost = graph[j]

            if distance[now] != INF and distance[nextNode] > distance[now] + cost:
                distance[nextNode] = distance[now] + cost

                # n번째에도 값이 갱신된다면 음수순환이 있다는 소리
                if i == n - 1:
                    return True
    return False

if __name__ == "__main__":
    input = sys.stdin.readline
    n, m = map(int, input().split())
    graph = []
    INF = sys.maxsize
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph.append((a, b, c))

    distance = [INF] * (n+1)
    cycle = bf(1)

    if cycle: print("-1")
    else:
        for i in range(2, n+1):
            if distance[i] == INF:
                print("-1")
            else:
                print(distance[i])