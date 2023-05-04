from collections import deque

def solution(maps):
    answer = -1
    q = deque()
    n = len(maps)
    m = len(maps[0])
    q.append((0, 0))

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    check = [[0] * m for _ in range(n)]
    check[0][0] = 1

    while q:
        x, y = q.popleft()

        if x == n-1 and y == m-1: answer = max(answer, check[x][y])

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if maps[nx][ny] == 1 and check[nx][ny] == 0:
                    q.append((nx, ny))
                    check[nx][ny] += check[x][y] + 1
    return answer

if __name__ == "__main__":
    maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
    res = 11

    ans = solution(maps)
    print(ans)
    print(ans == res)

    maps2 = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]
    res2 = -1

    ans2 = solution(maps2)
    print(ans2)
    print(ans2 == res2)