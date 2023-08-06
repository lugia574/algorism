import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    arr = list(map(int, input().split()))
    answer = []
    for i, x in enumerate(arr):
        num = i + 1
        if x == 0:
            answer.append(num)
        else:
            answer.insert(i - x, num)

    print(*answer)