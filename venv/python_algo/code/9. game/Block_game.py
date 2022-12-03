import turtle as t
import random as r
import time
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

# 움직이는 픽셀 객체 class
class Brick():
    # 생성자
    def __init__(self):
        self.y = 0
        self.x = 6
        self.color = r.randint(1,6)

    # 방향키조정 함수
    # 왼쪽으로 이동
    def move_left(self, grid):
        if grid[self.y][self.x-1] == 0 and grid[self.y+1][self.x-1] == 0:
            grid[self.y][self.x] = 0
            self.x -= 1

    # 오른쪽을 이동
    def move_right(self, grid):
        if grid[self.y][self.x + 1] == 0 and grid[self.y+1][self.x+1] == 0:
            grid[self.y][self.x] = 0
            self.x += 1



def draw_grid(block, grid):
    block.clear()
    top = 250
    left = -150
    colors = ["#2d3436", "#d63031", "#0984e3","#e17055", "#fdcb6e", "#00b894", "#6c5ce7", "#dfe6e9"] #블랙, 레드, 블루, 오렌지, 엘로우, 그린, 퍼플, 화이트
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            sc_x = left + (x * 22)
            sc_y = top - (y * 22)
            block.goto(sc_x, sc_y) # 위치 이동
            block.color(colors[grid[y][x]]) # 해당 그리디 위치값이 0이면 블랙 7이면 화이트
            block.stamp() # 그 위치 그래픽 찍기

# 해당 블록의 인접한 블록들이 동일한지 찾는 함수
def DFS(y, x, grid, color):
    global ch, blank
    ch[y][x] = 1
    blank.append((y,x))
    for i in range(4):
        yy = y + dy[i]
        xx = x + dx[i]
        if 0 < yy < 24 and 0 < xx < 13:
            if grid[yy][xx] == color and ch[yy][xx] == 0:
                DFS(yy, xx, grid, color)
                if len(blank) >= 4:
                    grid_update(grid, blank)
                    
# 블록이 있는 최고 높이 y 값 구하기 함수
def max_height(grid):
    for y in range(1,24):
        for x in range(1, 13):
            if grid[y][x] != 0:
                return y

# 인접한 동일한 블록들을 없애는 함수
def grid_update(grid, blank):
    # blank 튜플에 있는 값들 0으로 바꾸기
    for y, x in blank:
        grid[y][x] = 0
    height = max_height(grid) # 블록이 있는 최고 높이 y 값
    # 그러고 나서 빈칸으로 인해 공중에 떠 있는 것들 찾아서 아래로 내리기 (중력 작용)
    for y in range(23, height, -1):
        for x in range(1, 13):
            if grid[y][x] == 0:
                tmp_y = y
                while grid[tmp_y-1][x] == 0 and tmp_y > 0:
                    tmp_y -= 1
                grid[y][x] = grid[tmp_y-1][x]
                grid[tmp_y-1][x] = 0



if __name__ == "__main__":
    sc = t.Screen()
    sc.tracer(False) #빠르게 그려줌
    sc.bgcolor("#2d3436")
    sc.setup(width=600, height=700)

    # 격자판 >> 우리가 가지고 놀 게임판임
    # 0 은 빈공간
    grid = [[0]* 12 for _ in range(24)]
    
    # 벽은 7로 표현할꺼임
    for i in range(24):
        grid[i].insert(0, 7)
        grid[i].append(7)
    grid.append([7] * 14)

    for y in range(23, 20, -1):
        for x in range(1, 13):
            grid[y][x] = r.randint(1, 6)
    # 그래픽 객체
    block = t.Turtle()
    block.penup() # 이렇게 하면 이동선상의 줄 생략 가능
    block.speed(0)
    block.shape("square") # 픽섹은 가로 세로 20 씩임
    block.color("#d63031") # red
    block.setundobuffer(None) # 버퍼량 누적 X >> 속도 빨라짐

    # 벽돌 객체 인스턴스 생성
    brick = Brick()
    # 해당 벽돌 객체를 격자판에 기록
    grid[brick.y][brick.x] = brick.color
    # 격자판 그리기 함수 실행
    draw_grid(block, grid)

    # 방향키에 따른 함수 실행
    sc.onkeypress(lambda : brick.move_left(grid), "Left")
    sc.onkeypress(lambda: brick.move_right(grid), "Right")
    sc.listen()
    # 벽돌 움직이게 하기
    while True:
        sc.update() # 화면 갱신
        # 아래 더 못내려가게, 아래에 블록이 없을때만 로직 실행
        if grid[brick.y+1][brick.x] == 0:
            grid[brick.y][brick.x] = 0
            brick.y += 1
            grid[brick.y][brick.x] = brick.color
        else:
            ch = [[0] * 14 for _ in range(25)]
            blank = []
            DFS(brick.y, brick.x, grid, brick.color)
            brick = Brick()

        #격자판 그리기 함수 실행
        draw_grid(block, grid)
        time.sleep(0.05)

    # for x in grid:
    #     print(x)
    sc.mainloop()