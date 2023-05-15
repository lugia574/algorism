# 게임 캐릭터를 4가지 명령어를 통해 움직이려 합니다. 명령어는 다음과 같습니다.
# U: 위쪽으로 한 칸 가기
# D: 아래쪽으로 한 칸 가기
# R: 오른쪽으로 한 칸 가기
# L: 왼쪽으로 한 칸 가기
# 캐릭터는 좌표평면의 (0, 0) 위치에서 시작합니다.
# 좌표평면의 경계는 왼쪽 위(-5, 5), 왼쪽 아래(-5, -5),
# 오른쪽 위(5, 5), 오른쪽 아래(5, -5)로 이루어져 있습니다.'
# 게임 캐릭터가 지나간 길 중 캐릭터가 처음 걸어본 길의 길이를 구하려고 합니다.
# 예를 들어 위의 예시에서 게임 캐릭터가 움직인 길이는 9이지만, 캐릭터가 처음 걸어본 길의 길이는 7이 됩니다.

# def solution(dirs):
#     dirsArr = []
#     for i in list(dirs):
#         if i == "U":
#             dirsArr.append(0)
#         elif i == "R":
#             dirsArr.append(1)
#         elif i == "D":
#             dirsArr.append(2)
#         elif i == "L":
#             dirsArr.append(3)
#
#     board = [[0,0]]
#
#     dx = [0, 1, 0, -1]
#     dy = [-1, 0, 1, 0]
#     currentY = 0
#     currentX = 0
#     answer = 0
#
#     for i in dirsArr:
#
#         print(currentY + dy[i], "////", currentX + dx[i])
#         if -6 < currentY + dy[i] < 6 and -6 < currentX + dx[i] < 6:
#             currentY += dy[i]
#             currentX += dx[i]
#             if [currentY, currentX] not in board:
#                 answer += 1
#                 board.append([currentY, currentX])
#
#         print(board)
#
#
#     return answer
#

def solution(dirs):
    visit = set()
    x = 0; y = 0
    for d in dirs:
        if d == 'U' and y < 5:
            visit.add(((x, y), (x, y+1)))
            y += 1

        elif d == 'D' and y > -5:
            visit.add(((x, y-1), (x, y)))
            y -= 1

        elif d == 'R' and x < 5:
            visit.add(((x, y), (x+1, y)))
            x += 1

        elif d == 'L' and x > -5:
            visit.add(((x-1, y), (x, y)))
            x -= 1
    return len(visit)

if __name__ == "__main__":
    dirs = "ULURRDLLU"
    result = 7

    res = solution(dirs)
    print(res)
    print("정답입니다." if res == result else "틀렸습니다 모지리새끼야")

    # dirs2 = "LULLLLLLU"
    # dirs2 = "LULLLLLLUUULLRDLDDL"
    # dirs2 = "LRLRL"
    # result2 = 7
    # result2 = 12
    # result2 = 1

    # res2 = solution(dirs2)
    # print(res2)
    # print("2 정답입니다." if res2 == result2 else "틀렸습니다 모지리새끼야")