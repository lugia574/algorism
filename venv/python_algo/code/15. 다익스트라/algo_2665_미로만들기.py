# 힝 졸려요
# 이거 알고스팟 문제랑 같아용
# 입력값 다닥다닥 붙혀놓은거까지 똑같네 ㅋ
# 캬캬캬쿄쿄쿄쿄쿄 졸려룔요요요요용를레이히~ 졸려~
import sys, heapq

def dijkstra():
    hq = []
    heapq.heappush(hq, [0, 0, 0])

    while hq:
        w, x, y = heapq.heappop(hq)
        if x == n-1 and y == n-1:
            return w
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 > nx or nx >= n or 0 > ny or ny >= n or visited[nx][ny]: continue
            visited[nx][ny] = True
            if board[nx][ny] == '0':
                heapq.heappush(hq, [w+1, nx, ny])
            else:
                heapq.heappush(hq, [w, nx, ny])

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    board = [list(input().strip()) for _ in range(n)]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    visited = [[False] * n for _ in range(n)]
    res = dijkstra()
    print(res)