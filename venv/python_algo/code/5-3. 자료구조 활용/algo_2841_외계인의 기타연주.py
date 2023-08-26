# 그냥 1~ 6 번까지 있는 배열 만들고 각 플렛에 해당해는 번호 박다가
# 지금 있는 번호보다 작은 번호 들어오면 갱신해주면 되는거 아녀?
# 손가락으로 프렛을 한 번 누르거나 떼는 것을 손가락을 한 번 움직였다고 한다 니까
# 허접~
import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    n, p = map(int, input().split())

    guitar = [[] for _ in range(7)]
    cnt = 0
    for _ in range(n):
        num, fret = map(int, input().split())
        while guitar[num] and guitar[num][-1] > fret:
            guitar[num].pop()
            cnt += 1

        if not guitar[num] or guitar[num][-1] != fret:
            guitar[num].append(fret)
            cnt += 1
    print(cnt)
