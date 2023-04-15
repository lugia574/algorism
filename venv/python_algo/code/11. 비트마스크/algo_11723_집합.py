# 일단 비트마스크를 대충 다뤄보자
# 비트마스크는 각 자리의 비트를 이용해 bool형 list 를 만드는 것.
# 보니까 시간제한 보다는 메모리에 제한이 있음
# 4mb 면 마니 적은 편인거 같은데
# https://www.youtube.com/watch?v=dTnuHZYgpaI
import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    m = int(input())
    bit = 0
    all = (1 << 20) - 1
    for _ in range(m):
        command = input().split()
        if len(command) == 2:
            command[1] = int(command[1]) - 1 # 비트를 0 ~ 19까지 쓸꺼니까

        if command[0] == "all":
            bit = all
        elif command[0] == "add":
            bit |= 1<<command[1]
        elif command[0] == "remove":
            bit &= ~(1<<command[1])
        elif command[0] == "check":
            print(1 if bit &(1<<command[1]) else 0)
        elif command[0] == "toggle":
            bit ^= 1 << command[1]
        else:
            bit = 0