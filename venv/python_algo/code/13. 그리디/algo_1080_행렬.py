# 나 살짝 이해가 안됐던게
# 다르면 무조건 바꿔야하는가???
# 한칸뛰고 난 다음에 바꿔야할수도 있는거 아닌가??
# 되냐 안되냐 유무 따지는거면 상관없을꺼 같은데
# 최솟값을 구하는거자너
# 여기서 난 이해가 안돼

import sys
def reverse(x, y):
    for i in range(x, x + 3):
        for j in range(y, y +3):
            a[i][j] = 1 - a[i][j]


def check():
    for i in range(n):
        for j in range(m):
            if a[i][j] != b[i][j]:
                return False

    return True

if __name__ == "__main__":
    input = sys.stdin.readline
    n, m = map(int, input().split())
    a = [list(map(int, input().rstrip())) for _ in range(n)]
    b = [list(map(int, input().rstrip())) for _ in range(n)]
    cnt = 0
    for i in range(n-2):
        for j in range(m-2):
            if a[i][j] != b[i][j]:
                cnt += 1
                reverse(i, j)

    if check():
        print(cnt)
    else:
        print("-1")