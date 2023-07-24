# 이게 물고기들 이동하고 하는거야 대충 뭔소린지 알겠는데
# 상어가 먹을때는 해당 경로에 있는 애들로 가지가 뻗어지는건가??
# 아아아아아아아아
# 내가 무슨 잘못을 저지른지 이제 알겠네
# 나는 우선 물고기들을 좌표를 싹다 q 에 저장한 다음에 q 에서 하나씩 뽑아서 이동을 했단 말이야
# 근데 이럼 안돼 1 이 이동하면서 2 랑 자리를 바꿧는데
# q 에 있는 2 의 좌표는 전혀 갱신되지 않자너
# 하 그럼 어떻게 하지?
# 그냥 심심해서 q 에 다 박고 시작한게 아닌데
# 이럼 매번 board 를 돌면서 해당 시작 번호를 찾아야한다는 소리 아님??
# 와 해당 코드 찾아 보는데 하나하나 다 찾네 ㅋㅋㅋㅋ 1번 물고기 16번 돌고 ㅋㅋ 2번 물고기 16번 돌고 ㅋㅋㅋ
# 물론 최악의 경우에도 1억 코드가 안되긴하는데
# 개 무식하네ㅋㅋ 너무 하드해서 자바는 어떤가 찾아봄
# 자바는 Fish 클래스를 만들어 ArrayList 에 한데 박아서 관리함
# 클래스 안에 x, y 좌표 다 저장해져 있고, 살았냐 죽었냐 체크도 되어 있으니
# 0 부터 15 (1 ~ 16번) index 로 정렬해서 ArrayList.get 으로 불러내면 됨
# 먹힌 새끼도 죽었다라고 체크만 하는거지 ArrayList 에서 사라지는게 아니기때문에 index 가 꼬일것도 없음
# https://bcp0109.tistory.com/215
# 차라리 이 방법을 이용해서 파이썬을 다시 작성하는게 도움 될듯? 이게 훨 깔끔함
# 역시 좀만 복잡해져도 그냥 class 로 만들고 ArrayList 로 관리하는게 좋은듯
import sys, copy
input = sys.stdin.readline

class Shark:
    def __init__(self, x, y, dir, eatSum):
        self.x = x
        self.y = y
        self.dir = dir
        self.eatSum = eatSum


class Fish:
    def __init__(self, x, y, id, dir, isAlive):
        self.x = x
        self.y = y
        self.id = id
        self.dir = dir
        self.isAlive = isAlive


dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]
maxSum = 0


def main():
    arr = [[0 for _ in range(4)] for _ in range(4)]
    fishes = []

    for i in range(4):
        line = list(map(int, input().split()))
        for j in range(4):
            f = Fish(i, j, line[j * 2], line[j * 2 + 1] - 1, True)
            fishes.append(f)
            arr[i][j] = f.id

    fishes.sort(key=lambda x: x.id)

    f = fishes[arr[0][0] - 1]
    shark = Shark(0, 0, f.dir, f.id)
    f.isAlive = False
    arr[0][0] = -1

    dfs(arr, shark, fishes)
    print(maxSum)


def dfs(arr, shark, fishes):
    global maxSum

    if maxSum < shark.eatSum:
        maxSum = shark.eatSum

    for fish in fishes:
        move_fish(fish, arr, fishes)

    for dist in range(1, 4):
        nx = shark.x + dx[shark.dir] * dist
        ny = shark.y + dy[shark.dir] * dist

        if 0 <= nx < 4 and 0 <= ny < 4 and arr[nx][ny] > 0:
            arrCopies = copy_arr(arr)
            fishCopies = copy_fishes(fishes)

            arrCopies[shark.x][shark.y] = 0
            f = fishCopies[arr[nx][ny] - 1]
            new_shark = Shark(f.x, f.y, f.dir, shark.eatSum + f.id)
            f.isAlive = False
            arrCopies[f.x][f.y] = -1

            dfs(arrCopies, new_shark, fishCopies)


def move_fish(fish, arr, fishes):
    if not fish.isAlive:
        return

    for i in range(8):
        nextDir = (fish.dir + i) % 8
        nx = fish.x + dx[nextDir]
        ny = fish.y + dy[nextDir]

        if 0 <= nx < 4 and 0 <= ny < 4 and arr[nx][ny] > -1:
            arr[fish.x][fish.y] = 0

            if arr[nx][ny] == 0:
                fish.x = nx
                fish.y = ny
            else:
                temp = fishes[arr[nx][ny] - 1]
                temp.x = fish.x
                temp.y = fish.y
                arr[fish.x][fish.y] = temp.id

                fish.x = nx
                fish.y = ny

            arr[nx][ny] = fish.id
            fish.dir = nextDir
            return


def copy_arr(arr):
    temp = [[0 for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            temp[i][j] = arr[i][j]
    return temp


def copy_fishes(fishes):
    temp = []
    for fish in fishes:
        temp.append(Fish(fish.x, fish.y, fish.id, fish.dir, fish.isAlive))
    return temp


if __name__ == "__main__":
    main()
