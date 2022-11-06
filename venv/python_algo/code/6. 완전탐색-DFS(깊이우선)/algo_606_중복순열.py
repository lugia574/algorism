# 중복순열 구하기
# 1부터 N까지 번호가 적힌 구슬이 있습니다. 이 중 중복을 허락하여 M번을 뽑아 일렬로 나열
# 하는 방법을 모두 출력합니다.
# ▣ 입력설명
# 첫 번째 줄에 자연수 N(3<=N<=10)과 M(2<=M<=N) 이 주어집니다.
# ▣ 출력설명
# 첫 번째 줄에 결과를 출력합니다. 맨 마지막 총 경우의 수를 출력합니다.
# 출력순서는 사전순으로 오름차순으로 출력합니다.
# ▣ 입력예제 1
# 3 2
# ▣ 출력예제 1
# 1 1
# 1 2
# 1 3
# 2 1
# 2 2
# 2 3
# 3 1
# 3 2
# 3 3
# 9
import sys

# input= sys.stdin.readline()
# s = input.rstrip()

def DFS_PR(length):
    global cnt
    if length == M:
        for i in check:
            print(i, end=" ")
        cnt += 1
        print()

    else:
        for i in range(1,N+1):
            check[length] = i
            DFS_PR(length+1)

if __name__ == "__main__":
    N, M = map(int, input().split())
    check = [0] * M
    cnt = 0
    DFS_PR(0)
    print(cnt)