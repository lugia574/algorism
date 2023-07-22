import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    a, b, c = map(int, input().split())
    answer = 0
    if a == b == c:
        answer += 10000 + (a * 1000)
    elif a != b and a != c and b != c:
        answer += max(a, b, c) * 100
    else:
        x = a if a == b or a == c else b
        answer += 1000 + (x * 100)

    print(answer)
