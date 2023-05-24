import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    atmTime = list(map(int, input().rsplit()))
    atmTime.sort()
    wTime = 0
    answer = 0
    for x in atmTime:
        wTime += x
        answer += wTime
    print(answer)