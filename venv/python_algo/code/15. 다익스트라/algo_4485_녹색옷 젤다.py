# 따아악 다익스트라에 어울리는 최소로 어쩌구 내용이네
# 근데 이러면 사실상 BFS 문제는 거진 다익스트라로 대체 되는거 아닌가??
# 한번 BFS 문제들 좀 봐야할꺼 같은데
# 대충 딱 한번만 벽깨기 가능하고 나서 최단루트 이런거는 힘들꺼 같은데 뭐 굳이 할려면 할 순 있긴데
import sys, heapq

def dijkstra():
    heap = []
    heapq.heappush(heap, [board[0][0], 0, 0])

    while heap:
        point, x, y = heapq.heappop(heap)
        if x == n-1 and y == n-1:
            return point
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 > nx or nx >= n or 0 > ny or ny >= n or visited[nx][ny]: continue
            visited[nx][ny] = True
            newPoint = point + board[nx][ny]
            heapq.heappush(heap, [newPoint, nx, ny])


if __name__ == "__main__":
    input = sys.stdin.readline
    idx = 1
    while True:
        n = int(input())
        if n == 0: break
        board = [list(map(int, input().split())) for _ in range(n)]
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        visited = [[False] * n for _ in range(n)]
        visited[0][0] = True
        res = dijkstra()
        print("Problem %d: %d"%(idx,res))
        idx += 1

# 3
# 5 5 4
# 3 9 1
# 3 2 7
# 0