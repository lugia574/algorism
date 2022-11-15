# 등산경로(DFS)
# 마을 뒷산의 형태를 나타낸 지도는 N*N 구역으로 나뉘어져 있으며, 각 구역에는 높이가 함께 나타나 있습니다.
# N=5이면 아래와 같이 표현됩니다.
# 2 23 92 78 93
# 59 50 48 90 80
# 30 53 70 75 96
# 94 91 82 89 93
# 97 98 95 96 100
# 어떤 구역에서 다른 구역으로 등산을 할 때는 그 구역의 위, 아래, 왼쪽, 오른쪽 중 더 높은 구역으로만 이동할 수 있도록 등산로를 설계하려고 합니다.
# 등산로의 출발지는 전체 영역에서 가장 낮은 곳이고, 목적지는 가장 높은 곳입니다. 출발지와 목적지는 유일합니다.
# 지도가 주어지면 출발지에서 도착지로 갈 수 있는 등산 경로가 몇 가지 인지 구하는 프로그
# 램을 작성하세요.
# ▣ 입력설명
# 첫 번째 줄에 N(5<=N<=13)주어지고, N*N의 지도정보가 N줄에 걸쳐 주어진다.
# ▣ 출력설명
# 등산경로의 가지수를 출력한다.
# ▣ 입력예제 1
# 5
# 2 23 92 78 93
# 59 50 48 90 80
# 30 53 70 75 96
# 94 91 82 89 93
# 97 98 95 96 100
# ▣ 출력예제 1
# 5

def minMaxIndex():
    minM = min(map(min,mountaion))
    maxM = max(map(max,mountaion))
    s = []
    e = []

    for i in range(n):
        for j in range(n):
            if mountaion[i][j] == minM:
                s = [i,j]
            if mountaion[i][j] == maxM:
                e = [i,j]


    return minM,s,maxM, e

def mDFS(l):
    global cnt

    if l == e:
        cnt +=1
    else:
        for i in range(4):
            x = l[0] + dx[i]
            y = l[1] + dy[i]
            if 0<= x <n and 0<= y <n:
                if check[x][y] == 0:
                    if mountaion[l[0]][l[1]] < mountaion[x][y]:
                        check[x][y] = 1
                        mDFS([x,y])
                        check[x][y] = 0



if __name__ == "__main__":
    n = int(input())
    mountaion = []
    for _ in range(n):
        tmp = list(map(int,input().split()))
        mountaion.append(tmp)
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    minM,s,maxM,e = minMaxIndex()
    check = [[0] * n for _ in range(n)]
    cnt = 0
    check[s[0]][s[1]] = 1
    mDFS(s)
    print(cnt)

