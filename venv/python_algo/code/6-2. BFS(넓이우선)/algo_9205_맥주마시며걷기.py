# https://dogsavestheworld.tistory.com/210
# 처음에는 맵 이동하듯이 50씩 이동하면 되지 않을까 생각했는데
# 근데 뭐가 좀 안맞는거 같아서 찾아보니까 이렇게 푸네
# 역시 사람은 머리가 좋아야 하는뎈
# 20병을 50미터에 하나씩이면 총 1000미터 안에 있는 위치면 해당 위치에 무조건 도착 가능임
# 그걸 이용해서 도착지점에 접근 가능하냐 따져보고
# 안되면 편의점은 도착가능하냐? 가능하면 리셋 쌉가능이니까 편의점 좌표를 q 에 박아 넣어
import sys
from collections import deque

def distance(xa, yb, xc, yd):
    return abs(xa-xc) + abs(yb-yd)

def bfs(x, y):
    global end_x, end_y
    deq = deque([(x, y)])
    visited = set()

    while deq:
        x, y = deq.popleft()
        if distance(x, y, end_x, end_y) <= 1000:
            return True
        for i in range(s):
            store_x, store_y = store[i]
            if (store_x, store_y) not in visited:
                if distance(x, y, store_x, store_y) <= 1000:
                    visited.add((store_x, store_y))
                    deq.append((store_x, store_y))
    return False
if __name__ == "__main__":
    input = sys.stdin.readline
    for _ in range(int(input())):
        s = int(input())
        start_x, start_y = map(int, input().split())
        store = [tuple(map(int, input().split())) for _ in range(s)]
        end_x, end_y = map(int, input().split())
        check = bfs(start_x, start_y)
        print('happy' if check else 'sad')