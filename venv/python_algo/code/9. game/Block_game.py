import turtle as t
import random as r
import time

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
colors = ["#2d3436", "#d63031", "#0984e3","#fab1a0", "#fdcb6e", "#00b894", "#6c5ce7", "#dfe6e9"] #블랙, 레드, 블루, 오렌지, 엘로우, 그린, 퍼플, 화이트

# 움직이는 픽셀 객체 class
class Brick():
    # 생성자
    def __init__(self):
        self.y = 0
        self.x = 6
        self.y2 = 0
        self.x2 = 5
        self.y3 = 0
        self.x3 = 7
        self.color = r.randint(1,6)
        self.turn = False

    # 방향키조정 함수
    # 왼쪽으로 이동
    def move_left(self, grid):
        if self.turn:
            if grid[self.y3][self.x3-1] == 0 and grid[self.y2][self.x2-1] == 0 and grid[self.y][self.x-1] == 0 and grid[self.y3+1][self.x3-1] == 0:
                grid[self.y][self.x] = 0
                grid[self.y2][self.x2] = 0
                grid[self.y3][self.x3] = 0
                self.x -= 1
                self.x2 -= 1
                self.x3 -= 1
        else:
            if grid[self.y2][self.x2-1] == 0 and grid[self.y2+1][self.x2 - 1] == 0:
                grid[self.y][self.x] = 0
                grid[self.y2][self.x2] = 0
                grid[self.y3][self.x3] = 0
                self.x -= 1
                self.x2 -= 1
                self.x3 -= 1

    # 오른쪽을 이동
    def move_right(self, grid):
        if self.turn:
            if grid[self.y][self.x3 + 1] == 0 and grid[self.y2][self.x2 + 1] == 0 and grid[self.y][self.x + 1] == 0 and grid[self.y3+1][self.x3+1] == 0:
                grid[self.y][self.x] = 0
                grid[self.y2][self.x2] = 0
                grid[self.y3][self.x3] = 0

                self.x += 1
                self.x2 += 1
                self.x3 += 1
        else:
            if grid[self.y3][self.x3 + 1] == 0 and grid[self.y3+1][self.x3+1] == 0:
                grid[self.y][self.x] = 0
                grid[self.y2][self.x2] = 0
                grid[self.y3][self.x3] = 0

                self.x += 1
                self.x2 += 1
                self.x3 += 1

    # 턴
    def move_trun(self,grid):
        if self.turn:
            # 세로
            grid[self.y2][self.x2] = 0
            grid[self.y3][self.x3] = 0

            self.y2 += 1
            self.x2 -= 1
            self.y3 -= 1
            self.x3 += 1
            self.turn = False
        else:
            # 가로
            grid[self.y2][self.x2] = 0
            grid[self.y3][self.x3] = 0

            self.y2 -= 1
            self.x2 += 1
            self.y3 += 1
            self.x3 -= 1
            self.turn = True


# 뿌요뿌요 판 기본 그리기
def draw_grid(block, grid):
    global colors
    block.clear()
    top = 250
    left = -150
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            sc_x = left + (x * 22)
            sc_y = top - (y * 22)
            block.goto(sc_x, sc_y) # 위치 이동
            if y == 3 and grid[y][x] == 7:
                block.color("#d63031")
            else:
                block.color(colors[grid[y][x]]) # 해당 그리디 위치값이 0이면 블랙 7이면 화이트
            block.stamp() # 그 위치 그래픽 찍기

# 기록 및 타이틀 타이핑
def draw_score():
    global score
    str_score = str(score)
    for _ in range(4-len(str_score)):
        str_score = "0" + str_score
    pen.clear()
    pen.goto(-80, 290)
    pen.write("Puyo Puyo Game", font=("courier", 20, "normal"))  # 글 쓰기
    pen.goto(180, 200)
    pen.write("Score", font=("courier", 15))
    pen.goto(190, 170)
    pen.write(f"{str_score}", font=("courier", 15))


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


                    
# 블록이 있는 최고 높이 y 값 구하기 함수
def max_height(grid):
    for y in range(1,24):
        for x in range(1, 13):
            if grid[y][x] != 0:
                return y

# 중력기능
def gravity(height):
    for y in range(23, height, -1):
        for x in range(1, 13):
            if grid[y][x] == 0:
                tmp_y = y
                while grid[tmp_y - 1][x] == 0 and tmp_y - 1 > 0:
                    tmp_y -= 1
                grid[y][x] = grid[tmp_y - 1][x]
                grid[tmp_y - 1][x] = 0

# 인접한 동일한 블록들을 없애는 함수
def grid_update(grid, blank):
    # blank 튜플에 있는 값들 0으로 바꾸기
    for y, x in blank:
        grid[y][x] = 0
    height = max_height(grid) # 블록이 있는 최고 높이 y 값
    
    # 그러고 나서 빈칸으로 인해 공중에 떠 있는 것들 찾아서 아래로 내리기 (중력 작용)
    gravity(height)

# 연쇄 없애기
def continual_remove():
    global ch, blank, score
    while True:
        flag = 1
        for y in range(23, 15, -1):
            for x in range(1, 13):
                if grid[y][x] != 0:
                    ch = [[0] * 14 for _ in range(25)]
                    blank = []
                    DFS(y, x, grid, grid[y][x])
                    if len(blank) >= 6:
                        grid_update(grid, blank)
                        flag = 0
                        score += len(blank) * 100 if len(blank) >= 10 else len(blank) * 25
                        draw_score()
                        draw_grid(block, grid) # 판 갱신
        if flag == 1:
            break



def game_over():
    pen.up()
    pen.goto(-120,100)
    pen.write("Game Over", font=("courier", 30))

def you_win():
    pen.up()
    pen.goto(-100, 100)
    pen.write("You Win", font=("courier", 30))


if __name__ == "__main__":
    sc = t.Screen()
    sc.tracer(False) #빠르게 그려줌
    sc.bgcolor("#2d3436")
    sc.setup(width=600, height=700)
    score = 0

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
    grid[brick.y2][brick.x2] = brick.color
    grid[brick.y3][brick.x3] = brick.color
    # 격자판 그리기 함수 실행
    draw_grid(block, grid)

    pen = t.Turtle() # 터틀 새객체
    pen.penup()
    pen.ht() # 숨기기
    pen.color("#b2bec3") # 회색
    # 그리기 함수 실행
    draw_score()

    # 방향키에 따른 함수 실행
    sc.onkeypress(lambda : brick.move_left(grid), "Left")
    sc.onkeypress(lambda: brick.move_right(grid), "Right")
    sc.onkeypress(lambda: brick.move_trun(grid), "space")
    sc.listen()
    # 벽돌 움직이게 하기
    while True:
        sc.update() # 화면 갱신

        # 아래 더 못내려가게, 아래에 블록이 없을때만 로직 실행
        if (brick.turn.__eq__(False) and grid[brick.y+1][brick.x] == 0 and grid[brick.y2+1][brick.x2] == 0 and grid[brick.y3+1][brick.x3] == 0) or (brick.turn and  grid[brick.y3+1][brick.x3] == 0):
            grid[brick.y][brick.x] = 0
            grid[brick.y2][brick.x2] = 0
            grid[brick.y3][brick.x3] = 0

            brick.y += 1
            brick.y2 += 1
            brick.y3 += 1

            grid[brick.y][brick.x] = brick.color 
            grid[brick.y2][brick.x2] = brick.color # 왼쪽
            grid[brick.y3][brick.x3] = brick.color # 오른쪽
        else:
            ch = [[0] * 14 for _ in range(25)]
            blank = []
            DFS(brick.y, brick.x, grid, brick.color)

            if len(blank) >= 6:
                grid_update(grid, blank)
                score += len(blank) * 100 if len(blank) >= 10 else len(blank) * 25
                draw_score()
                continual_remove() # 중력작용 이후 같은 블록들 연속 삭제

            height = max_height(grid)
            gravity(height) # 중력시스템
            if height <= 3:
                game_over()
                break
            if score >= 2000:
                draw_grid(block, grid)
                you_win()
                break
            brick = Brick()

        #격자판 그리기 함수 실행
        draw_grid(block, grid)
        time.sleep(0.1)

    sc.mainloop()