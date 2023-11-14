# 이 무식한 풀이가 맞나 모르겠네 ㅋ
# 제한사항이 고작 n <= 50 이라 걍 일차원적으로 갈김 ㅋ
def solution(wallpaper):
    n = len(wallpaper)
    m = len(wallpaper[0])
    lux = 51
    luy = 51
    rdx = 0
    rdy = 0
    for x in range(n):
        for y in range(m):
            if wallpaper[x][y] == '#':
                lux = min(lux, x)
                luy = min(luy, y)
                rdx = max(rdx, x + 1)
                rdy = max(rdy, y + 1)

    return [lux, luy, rdx, rdy]


if __name__ == "__main__":
    wallpaper = [".#...", "..#..", "...#."]
    res = [0, 1, 3, 4]
    answer = solution(wallpaper)
    print(res == answer, answer)

    wallpaper = ["..........", ".....#....", "......##..", "...##.....", "....#....."]
    res = [1, 3, 5, 8]
    answer = solution(wallpaper)
    print(res == answer, answer)

    wallpaper = [".##...##.", "#..#.#..#", "#...#...#", ".#.....#.", "..#...#..", "...#.#...", "....#...."]
    res = [0, 0, 7, 9]
    answer = solution(wallpaper)
    print(res == answer, answer)

    wallpaper = ["..", "#."]
    res = [1, 0, 2, 1]
    answer = solution(wallpaper)
    print(res == answer, answer)
