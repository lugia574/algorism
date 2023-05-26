import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    k, n = map(int, input().split())
    line = []
    for _ in range(k):
        line.append(int(input()))

    lt, rt = 1, min(line)

    while lt < rt:
        mid = (lt + rt) // 2
        cnt = 0
        for i in line:
            cnt += i // mid

        if cnt >= n:
            lt = mid + 1
        else:
            rt = mid - 1

    print(rt)
    # 그러니까 주어진 리스트들을 잘 나눠서 총 n 개 만큼 만드는게 핵심이지? 이건 이분탐색으로 가능할듯