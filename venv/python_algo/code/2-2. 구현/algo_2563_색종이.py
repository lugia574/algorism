# 그냥 단순하게 생각하면
# 100*100 이중 boolean 배열을 만들고 x, y 직사각형으로 해당범위 True 로 바꿔주고 그것들을 cnt 해주면 그게 넓이 일텐데
# 너무 완전탐색형식이라 좀 별로임 시간복잡도 n^2 이라 좀 마니 별로야 근데 뭐 만약 아니면 계산으로 해야할꺼 같은데 이거 힘들거든? n 이 100 까지라? 쌉에바임 걍 배열로 조져야지 뭐

import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    loc = [list(map(int, input().split())) for _ in range(n)]

    board = [[0] * 101 for _ in range(101)]
    cnt = 0

    for x, y in loc:
        for i in range(x, x+10):
            for j in range(y, y+10):
                if board[i][j] == 0:
                    board[i][j] = 1
                    cnt += 1

    print(cnt)